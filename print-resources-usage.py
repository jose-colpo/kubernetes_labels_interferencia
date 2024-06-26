import subprocess
import re
import time
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_io_values():
    try:
        output = subprocess.check_output(['sudo', 'iotop', '-b', '-n', '1'])
        output_lines = output.decode('utf-8').split('\n')
        
        # Encontrar a linha que contém os valores de IO
        io_line = [line for line in output_lines if 'Total DISK' in line]
        
        # Extrair os valores de IO da linha encontrada
        io_values = [float(val) for val in re.findall(r'[\d.]+', io_line[0])]
        
        return io_values
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar iotop: {e}"

def calculate_io_usage(last_values, current_values):
    if last_values is None:
        return None
    
    read_usage = current_values[0] - last_values[0]
    write_usage = current_values[1] - last_values[1]
    
    return read_usage, write_usage

def main():
    last_io_values = None
    while True:
        current_io_values = get_io_values()
        
        io_usage = calculate_io_usage(last_io_values, current_io_values)
        if io_usage is not None:
            read_usage, write_usage = io_usage
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            print(f"{cpu_usage},{memory_usage},{write_usage}")
            with open("resource-report.txt", "a") as file:  # "a" para abrir o arquivo em modo de adição (append)
                file.write(f"{cpu_usage},{memory_usage},{write_usage}\n")
        else:
            print("Não foi possível obter os valores de I/O.")
        
        last_io_values = current_io_values
        time.sleep(1)

if __name__ == "__main__":
    main()
acaddr@sta