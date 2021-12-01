#Autor Huitziuit

#Formato de entrada 
#$ express2Cliente [nombre(sin espacios)] [x] [y]
import socket
import sys

PORT = 7000
HOST = "127.0.0.1"

def main():
    argv = sys.argv
    mySocket=socket.socket()
    mySocket.connect((HOST,PORT))
    mensaje=argv[1]+" "+argv[2]+" "+argv[3] #nombre y coordenadas
    mySocket.sendall(mensaje.encode())

    #Espero el calculo del lado del servidor
    print("Esperando respuesta del servidor...")
    respuesta = mySocket.recv(1024).decode()
    print("\n-> Respuesta: ",respuesta)
    mySocket.close()

if __name__ == "__main__":
    main()
