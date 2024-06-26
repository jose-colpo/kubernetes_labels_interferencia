from kubernetes import client, config

def list_pod_labels():
    # Carregar a configuração do Kubernetes a partir do arquivo de configuração padrão
    config.load_kube_config()

    # Criar um objeto de API do Kubernetes
    v1 = client.CoreV1Api()

    # Listar todos os Pods no cluster
    pod_list = v1.list_pod_for_all_namespaces(watch=False)

    # Iterar sobre os Pods e imprimir seus labels
    for pod in pod_list.items:
        if "default" in pod.metadata.namespace:
            print(f"Pod: {pod.metadata.name}")
            print(f"Node: {pod.spec.node_name}")
            for key, value in pod.metadata.labels.items():
                if key != "pod-template-hash" and key != "app":
                    print(f"  {key}: {value}")
            print("\n")

if __name__ == "__main__":
    list_pod_labels()
