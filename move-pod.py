from kubernetes import client, config
from kubernetes.client.rest import ApiException

def recreate_pod_on_node(pod_name, namespace, node_name):

    # Carregar a configuração do Kubernetes a partir do arquivo de configuração padrão
    config.load_kube_config()

    # Criar um objeto de API do Kubernetes
    v1 = client.CoreV1Api()

    try:
        # Excluir o Pod pelo nome e namespace
        v1.delete_namespaced_pod(pod_name, namespace)
        print(f"Pod '{pod_name}' deletado com sucesso no namespace '{namespace}'")
    except ApiException as e:
        print(f"Ocorreu um erro ao tentar deletar o Pod: {e}")

    pod_name = pod_name + "recreated"
    node_name = "stack04"

    # Criar um objeto de especificação do Pod
    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": pod_name},
        "spec": {
            "containers": [
                {
                    "name": "ct-nt",
                    "image": "josecolpo/node-tiers:tag",
                    # Adicione aqui os detalhes do contêiner conforme necessário
                }
            ],
            "nodeName": node_name  # Define o nó onde o Pod será executado
        }
    }

    try:
        # Criar o Pod no Kubernetes
        v1.create_namespaced_pod(namespace, pod_manifest)
        print(f"Pod '{pod_name}' criado com sucesso no nó '{node_name}' no namespace '{namespace}'")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar criar o Pod: {e}")

if __name__ == "__main__":
    # Chame a função fornecendo o nome do Pod, namespace e nome do novo nó desejado
    recreate_pod_on_node("pod-nt", "default", "stack04")