import subprocess
import threading
import time
import sys

def exec_command(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    inicio = time.time()

    # Defina o comando que você deseja executar
    pod_name = "pod-node-tiers-" + sys.argv[1]
    command_to_execute = f"-- curl --header 'Content-Type: application/json' --request POST http://localhost:3000/writeFile"
    #command_to_execute2 = f"-- curl --header 'Content-Type: application/json' --request POST http://localhost:3000/matrix"
    kubectl_command = f"kubectl exec -it {pod_name} {command_to_execute}"
    #kubectl_command2 = f"kubectl exec -it {pod_name} {command_to_execute2}"

    # Defina o número de vezes que deseja executar o comando
    num_executions = 49

    # Execute os comandos em threads separadas para simular execuções paralelas
    threads = []
    for _ in range(num_executions):
        thread = threading.Thread(target=exec_command, args=(kubectl_command,))
        threads.append(thread)
        thread.start()
        #thread2 = threading.Thread(target=exec_command, args=(kubectl_command2,))
        #threads.append(thread2)
        #thread2.start()

    # Aguarde até que todas as threads tenham sido concluídas
    for thread in threads:
        thread.join()

    # Fim do cronômetro
    fim = time.time()

    # Calcula o tempo total
    tempo_total = fim - inicio
    print(f"Tempo total para executar {num_executions} vezes: {tempo_total:.2f} segundos")
    print(f"{pod_name}")