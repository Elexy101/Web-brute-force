import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "IPV4 address"
port = 80
def portscanner(port):
    if sock.connect_ex((host,port)):
        print("Port ",port," is closed")
    else:
        print("Port ",port," is opened")
portscanner(port)