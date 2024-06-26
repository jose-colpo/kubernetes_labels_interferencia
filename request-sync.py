import subprocess
import time
import sys

def exec_command(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    inicio = time.time()

    # Defina o comando que você deseja executar
    pod_name = "pod-node-tiers-" + sys.argv[2]
    #command_to_execute = f"kubectl exec -it {pod_name} -- curl --header 'Content-Type: application/json' --request POST http://localhost:3000/writeFile"
    command_to_execute = f"kubectl exec -it {pod_name} -- curl --header 'Content-Type: application/json' --request POST http://localhost:3000/" + sys.argv[1]

    # Defina o número de vezes que deseja executar o comando
    num_executions = int(sys.argv[3])

    # Execute os comandos sequencialmente
    for _ in range(num_executions):
        exec_command(command_to_execute)

    # Fim do cronômetro
    fim = time.time()

    # Calcula o tempo total
    tempo_total = fim - inicio
    print(f"Tempo total para executar {num_executions} vezes: {tempo_total:.2f} segundos")
    print(f"{pod_name}")