
import subprocess
import time

def ping(host):
    
        
    result = subprocess.call('ping '+host+' -c '+'1', shell=True) 
host_to_ping =""
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    host_to_ping = raw_input("Digite o endereco IP ou nome do host para ping: ")
    ping(host_to_ping)
