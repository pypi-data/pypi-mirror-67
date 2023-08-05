import os

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory as DMF
from faker import Faker

fake = Faker()

models_path = "kubernetes_manager."

microk8s_config = os.getenv("MICROK8S_CF", None)


class TargetClusterFactory(DMF):
    class Meta:
        model = models_path + "TargetCluster"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-cluster")
    api_endpoint = "https://127.0.0.1:16443"
    telemetry_endpoint = "https://127.0.0.1:16443"
    telemetry_source = "p"
    config = microk8s_config


class KubernetesNamespaceFactory(DMF):
    class Meta:
        model = models_path + "KubernetesNamespace"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-ns")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = "v1"
    kind = "Namespace"
    exists = False


class KubernetesConfigMapFactory(DMF):
    class Meta:
        model = models_path + "KubernetesConfigMap"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-cm")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    kind = "ConfigMap"
    data = {"data": str(factory.fuzzy.FuzzyText(length=12))}
    namespace = factory.SubFactory(KubernetesNamespaceFactory)


class KubernetesVolumeFactory(DMF):
    class Meta:
        model = models_path + "KubernetesVolume"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-vol")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None


class KubernetesVolumeMountFactory(DMF):
    class Meta:
        model = models_path + "KubernetesVolumeMount"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-mount")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    mount_path = "/media"
    sub_path = None


class KubernetesContainerFactory(DMF):
    class Meta:
        model = models_path + "KubernetesContainer"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    image_name = factory.fuzzy.FuzzyChoice(["debian", "alpine", "busybox"])
    image_tag = "latest"
    image_pull_policy = "IfNotPresent"
    command = "/bin/sh"
    args = "-c,echo SUCCESS"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])


class KubernetesPodTemplateFactory(DMF):
    class Meta:
        model = models_path + "KubernetesPodTemplate"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-pod")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    labels = {"app": fake.word()}
    annotations = None
    restart_policy = "Always"

    @factory.post_generation
    def containers(self, create, containers, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if containers:
            # A list of groups were passed in, use them
            for container in containers:
                self.containers.add(container)

    @factory.post_generation
    def volumes(self, create, volumes, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if volumes:
            # A list of groups were passed in, use them
            for volume in volumes:
                self.volumes.add(volume)



class KubernetesDeploymentFactory(DMF):
    class Meta:
        model = models_path + "KubernetesDeployment"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-dep")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = "apps/v1"
    kind = "Deployment"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = factory.SubFactory(KubernetesNamespaceFactory)
    kuid = None
    selector = labels
    replicas = 1
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)


class KubernetesJobFactory(DMF):
    class Meta:
        model = models_path + "KubernetesJob"

    title = factory.fuzzy.FuzzyText(length=8, suffix="-job")
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    removed = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = "apps/v1"
    kind = "Deployment"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = factory.SubFactory(KubernetesNamespaceFactory)
    kuid = None
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)
    backoff_limit = factory.fuzzy.FuzzyInteger(1, 10)
