import os
import click
from indico_install.config import merge_dicts
from indico_install.utils import run_cmd
from indico_install.infra.init import init

DEFAULT_NODE_CONFIGS = {
    "image-type": "UBUNTU",
    "disk-type": "pd-standard",
    "scopes": '"https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append"',
    "no-enable-autorepair": None,
    "min-nodes": 0,
    "max-nodes": 3,
}

NODE_POOL_TYPES = {
    "default-gpu-pool": {
        "machine-type": "n1-standard-8",
        "accelerator": "type=nvidia-tesla-p4,count=1",
    },
    # N2s do not support GPU and are not supported in us-east4-c
    "default-cpu-pool": {"machine-type": "c2-standard-4"},
    "default-mem-pool": {"machine-type": "n1-standard-8"},
    "default-pool": {"machine-type": "n1-standard-8"},
    "default-pvm-pool": {
        "machine-type": "n1-standard-8",
        "preemptible": None,
        "max-nodes": 6,
    },
    "t4-gpu-pool": {
        "machine-type": "n1-highmem-4",
        "accelerator": "type=nvidia-tesla-t4,count=1",
    },
}


autoscale_option = click.option(
    "--autoscale/--no-autoscale",
    help="Cluster autoscaling",
    default=True,
    show_default=True,
)


def nodegroup_args(ng_type, count, pvm=False, **kwargs):
    count = int(count)
    args = merge_dicts(DEFAULT_NODE_CONFIGS, NODE_POOL_TYPES[ng_type])
    args.update(kwargs)
    if pvm:
        args["preemptible"] = None  # Add as flag
    max_nodes = args.get("max-nodes", count)
    args["max-nodes"] = max_nodes if count < max_nodes else count + 1
    if args.pop("autoscale", True):
        args["enable-autoscaling"] = None
    return " ".join([f"--{k}" if v is None else f"--{k}={v}" for k, v in args.items()])


@click.group("gke")
@click.pass_context
def gke(ctx):
    """
    Managing a kubernetes cluster on Google Kubernetes Engine
    """
    pass


gke.command("init")(init(__name__))
environment_abbrev = {"production": "prod", "development": "dev", "staging": "stage"}
environment_colors = {"production": "red", "development": "green", "staging": "blue"}
environment_subnets = {
    "production": {
        "us-central1-f": "production-central1",
        "us-east4-c": "production-east4",
    },
    "staging": {
        "us-central1-f": "production-central1",
        "us-east4-c": "production-east4",
    },
    "development": {
        "us-central1-f": "development-central1",
        "us-east4-c": "development-default",
    },
}


@gke.command("create-nodepools")
@click.pass_context
@click.option(
    "--cluster-name", required=True, help="Name of cluster to attach nodepools to"
)
@click.option(
    "--node-pool",
    help=f"additional pools and counts. EX: --node-pool gpu=3 --node-pool finetune=1. Types are {list(NODE_POOL_TYPES.keys())}",
    multiple=True,
)
@click.option("--pvm", help=f"enable preemptible nodes", is_flag=True)
@autoscale_option
def create_nodepools(
    ctx, cluster_name, autoscale=True, node_pool=None, pvm: bool = False
):
    """
    Creates additional nodepools for existing cluster
    """
    node_pools = {}
    for np in node_pool or []:
        np_type, np_size = np.split("=", 1)
        assert (
            np_type in NODE_POOL_TYPES
        ), f"node_pool type {np_type} is not valid. Please select from {NODE_POOL_TYPES}"
        assert (
            int(np_size) > 0
        ), f"node_pool size {np_size} is not valid. Please specify an int > 0"
        node_pools[np_type] = np_size

    if not node_pools:
        return

    for np, count in node_pools.items():
        count = int(count)
        run_cmd(
            f"gcloud container node-pools create {np}{'-pvm' if pvm else ''} "
            f"--num-nodes={count} --cluster={cluster_name} "
            + nodegroup_args(np, count, pvm)
        )


@gke.command("create")
@click.pass_context
@click.argument("environment")
@click.argument("name")
@click.argument("size", type=int)
@click.option("--subnetwork", help="Network to be used")
@click.option(
    "--version", help="GKE Cluster Version", default="1.15.11-gke.3", show_default=True
)
@click.option(
    "--project", help="GKE Project Name", default="new-indico", show_default=True
)
@click.option("--zone", help="GKE zone", default="us-east4-c", show_default=True)
@click.option(
    "-d",
    "--deployment-root",
    default=os.getcwd(),
    show_default=True,
    help="Root directory for installation files",
)
@click.option(
    "--node-pool",
    help=f"additional pools. EX: --node-pool gpu=3 --node-pool finetune=1. Types are {list(NODE_POOL_TYPES.keys())}",
    multiple=True,
)
@click.option(
    "--optimize/--no-optimize",
    help="Optmize cluster scaling for cost savings",
    default=True,
    show_default=True,
)
@autoscale_option
def create_cluster(
    ctx,
    environment,
    name,
    size,
    subnetwork=None,
    version=None,
    project=None,
    zone=None,
    deployment_root=None,
    node_pool=None,
    optimize=True,
    autoscale=True,
):
    """
    Creates a GKE cluster through gcloud.

    Don't change the kubernetes version unless absolutely necessary for
        security invulnerabilities/necessary feature

    The network used is default to indico-{environment},
        this will need to be created ahead of time with custom subnets (not auto)

    The subnetwork specified needs to be created in the network
        created in the zone desired.

    Development scaling is: default-pool=1, default-gpu-pool=1, default-pvm-pool=1
    """
    environment = next(
        iter(
            env
            for env in {"production", "development", "staging"}
            if environment in env
        )
    )

    name = name.lower()
    assert environment_abbrev[environment] in name

    size = int(size)
    assert size > 0

    subnetwork = subnetwork or environment_subnets[environment][zone]
    network = (
        f"indico-production" if environment is "staging" else f"indico-{environment}"
    )
    optimization_profile = "optimize-utilization" if optimize else "balanced"

    click.secho(
        f"Creating cluster {name} in {environment} with {size} nodes...",
        fg=environment_colors[environment],
    )
    # TODO: Check if we need the python2.7 aliasing.
    # If we do, figure out how to install gcloud for python3

    # TODO: this will probably require components installation and will cause the
    # command to fail since its non-interactive.
    run_cmd(
        f"""
        gcloud beta container clusters create {name} \
            --project "{project}" \
            --zone {zone} \
            --username "admin" \
            --cluster-version "{version}" \
            --num-nodes "{size}" \
            --enable-stackdriver-kubernetes \
            --addons HorizontalPodAutoscaling,HttpLoadBalancing \
            --no-enable-autoupgrade \
            --enable-ip-alias \
            --network "projects/new-indico/global/networks/{network}" \
            --subnetwork "{subnetwork}" \
            --autoscaling-profile "{optimization_profile}" \
        """
        + nodegroup_args("default-pool", size, autoscale=autoscale)
    )

    # TODO: Refactor rbac & switch
    # TODO: ensure this actually persists in current session
    run_cmd(
        f"""
        gcloud config set compute/zone {zone}
        gcloud container clusters get-credentials {name} \
            --zone {zone} \
            --project {project}
        """
    )

    email = run_cmd(
        f"""
        cat {deployment_root}/.config/gcloud/configurations/config_default \
            | grep account \
            | awk -F "=" '{{print $2}}'
        """
    )

    user = email.split("@")[0]

    run_cmd(
        f"""kubectl create clusterrolebinding cluster-admin-binding-{user} \
            --clusterrole cluster-admin \
            --user {email}"""
    )
    if node_pool:
        ctx.invoke(
            create_nodepools,
            cluster_name=name,
            node_pool=node_pool,
            autoscale=autoscale,
        )
