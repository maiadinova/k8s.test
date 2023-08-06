from kubernetes import client, config

config.load_kube_config()

crd = client.V1beta1CustomResourceDefinition(
    metadata=client.V1ObjectMeta(name="my-crd"),
    spec=client.V1beta1CustomResourceDefinitionSpec(
        group="example.com",
        version="v1",
        names=client.V1beta1CustomResourceDefinitionNames(
            kind="MyCustomResource",
            plural="mycustomresources",
            singular="mycustomresource"
        ),
        scope="Namespaced"
    )
)

api = client.ApiextensionsV1beta1Api()
api.create_custom_resource_definition(body=crd)
