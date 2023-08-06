from kubernetes import client, config

config.load_kube_config()

configmap = client.V1ConfigMap(
    metadata=client.V1ObjectMeta(name="my-configmap"),
    data={
        "key1": "value1",
        "key2": "value2"
    }
)

api = client.CoreV1Api()
api.create_namespaced_config_map(namespace="default", body=configmap)
