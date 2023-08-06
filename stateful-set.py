from kubernetes import client, config

config.load_kube_config()

statefulset = client.V1StatefulSet(
    metadata=client.V1ObjectMeta(name="my-statefulset"),
    spec=client.V1StatefulSetSpec(
        selector=client.V1LabelSelector(
            match_labels={"app": "my-app"}
        ),
        replicas=3,
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-container",
                        image="nginx:latest"
                    )
                ]
            )
        )
    )
)

api = client.AppsV1Api()
api.create_namespaced_stateful_set(namespace="default", body=statefulset)
