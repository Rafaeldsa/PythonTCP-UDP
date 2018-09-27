import socket

target_host = "0.0.0.0"
target_port = 9999
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host,target_port))
    
    entrada = raw_input()
    if entrada == "sair" or entrada == "exit":
        client.close()
        break
       
    client.send(entrada)
    
    resposta = client.recv(4096)

    print resposta
