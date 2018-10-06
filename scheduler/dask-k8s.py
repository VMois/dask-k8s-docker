from dask_kubernetes import KubeCluster
import os
import time

cluster = KubeCluster.from_yaml(
    'worker-spec.yaml', 
    port=8786,
    diagnostics_port=8787)

# Get ENV variables for cluster scaling config
# More info: https://github.com/dask/distributed/blob/master/distributed/deploy/adaptive.py
min_workers_number = os.getenv('DASK_CLUSTER_MIN_WORKERS', 1)
max_workers_number = os.getenv('DASK_CLUSTER_MAX_WORKERS', 8)
startup_cost = os.getenv('DASK_CLUSTER_STARTUP_COST', '10s')
target_duration = os.getenv('DASK_CLUSTER_TARGET_DURATION', '10s')

cluster.adapt(
    minimum=min_workers_number,
    maximum=max_workers_number,
    startup_cost=startup_cost,
    target_duration=target_duration
)
while True:
    time.sleep(0.1)
