from kubernetes import client, config

config.load_kube_config()

autoscale = client.V2beta2HorizontalPodAutoscaler(
    metadata=client.V1ObjectMeta(name="my-hpa"),
    spec=client.V2beta2HorizontalPodAutoscalerSpec(
        scale_target_ref=client.V2beta2CrossVersionObjectReference(
            api_version="apps/v1",
            kind="Deployment",
            name="my-deployment"
        ),
        min_replicas=2,
        max_replicas=10,
        metrics=[
            client.V2beta2MetricSpec(
                type="Resource",
                resource=client.V2beta2ResourceMetricSource(
                    name="cpu",
                    target_average_utilization=50
                )
            )
        ]
    )
)

api = client.AutoscalingV2beta2Api()
api.create_namespaced_horizontal_pod_autoscaler(namespace="default", body=autoscale)
