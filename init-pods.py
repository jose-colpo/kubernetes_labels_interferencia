from kubernetes import client, config

def create_pod(pod_name, namespace, labels):

    # Definindo a especificação do Pod
    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": pod_name,
            "labels": labels
        },
        "spec": {
            "nodeName": "proj02",
            "containers": [
                {
                    "name": "ct-nt",
                    "image": "josecolpo/node-tiers:v3",
                    "ports": [{"containerPort": 3000}]  # Porta que o contêiner irá escutar
                    # Outros detalhes do contêiner podem ser adicionados aqui, se necessário
                }
            ]
        }
    }

    # Criar um objeto de API do Kubernetes
    v1 = client.CoreV1Api()

    try:
        # Criar o Pod no Kubernetes
        v1.create_namespaced_pod(namespace, pod_manifest)
        print(f"Pod '{pod_name}' criado no namespace '{namespace}'")
    except Exception as e:
        print(f"Erro ao criar o Pod '{pod_name}': {e}")

if __name__ == "__main__":
    config.load_kube_config()

    # Definir o número de Pods que você deseja criar
    num_pods_processor_intensive = 7
    num_pods_memory_intensive = 5

    labels_processor_intensive = {"processor": "high", "memory": "low"}
    labels_memory_intensive = {"processor": "low", "memory": "high"}

    # Nome do namespace onde os Pods serão criados
    namespace = "default"

    pods_count = 0

    # Criar vários Pods usando um loop
    for pods_count in range(num_pods_processor_intensive):
        pod_name = f"pod-node-tiers-{pods_count}"
        create_pod(pod_name, namespace,labels_processor_intensive)

    pods_count += 1 

    for pods_count in range(pods_count, pods_count+num_pods_memory_intensive):
        pod_name = f"pod-node-tiers-{pods_count}"
        create_pod(pod_name, namespace,labels_memory_intensive)