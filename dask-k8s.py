from dask_kubernetes import KubeCluster
import time

cluster = KubeCluster.from_yaml(
    'worker-spec.yaml', 
    port=8786,
    diagnostics_port=8787)
cluster.adapt(minimum=1, maximum=3)
print("[!] Start loop...")
while True:
    time.sleep(1)
    print("tick")