import socket

def get_host_ip():
     host_name = socket.gethostname() 
     host_ip = socket.gethostbyname(host_name) 
     print(host_ip)
print("\x1bc\x1b[47;34m")
get_host_ip()
