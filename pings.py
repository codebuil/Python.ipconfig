
import subprocess
import time

def ping(host):
    try:
        start_time = time.time()
        result = subprocess.run(['ping', host,'-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3)
        end_time = time.time()
        output = result.stdout.decode()
        if result.returncode == 0:
            print(f"{output}")
        else:
            print(f"{output}")
    except subprocess.TimeoutExpired:
        print(f"Tempo limite de 2 segundos excedido para o host {host}.")
print("\033c\033[47;34m")
if __name__ == "__main__":
    host_to_ping = input("Digite o endereço IP ou nome do host para ping: ")
    ping(host_to_ping)