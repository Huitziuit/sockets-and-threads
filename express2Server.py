#Author Huitziuit 
import random
import math
from sys import argv
import sys
from threading import Thread, Lock
import time
import socket

from rsc.uber import HOST

PORT = 7000
HOST = "127.0.0.1"

clientes=[]


def main():
    argv=sys.argv

    numAutos=10000000       #10000000            tarda 26seg
    anchoDelMapa=10000000000    #10,000,000,000

    #Coloca en lugares aleatorios los autos
    PosAutosX=[]
    PosAutosY=[]

    print("======== Colocando autos... ========")
    for i in range(numAutos):
        
        PosAutosX.append(random.randrange(0, anchoDelMapa, 1))
        PosAutosY.append(random.randrange(0, anchoDelMapa, 1))
    print("\n---> Autos colocados\n---> Creando socket...")

    try:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("---> Socket creado.\n")
        mySocket.bind((HOST, PORT))        
        mySocket.listen()    
        print("\n======== Esperando clientes ========")
        print("======= En el puerto ", PORT," =======")
        while True:
            coneccion, direccion_cliente = mySocket.accept()    
            print ("\n\nSe detecto una coneccion\n----> Asignando coneccion a un hilo" )
            t = Thread(target=calcula, args=(coneccion, numAutos, PosAutosX, PosAutosY))
            t.start()

    except socket.error as err:
        print(err)


def calcula(Coneccion,No_A,Xs,Ys):
    coneccion=Coneccion 
    solicitud = coneccion.recv(1024).decode()#recibe la solicitud del cliente
    print("--------> Calculando distancias de "+ solicitud.split(" ")[0]+" a cada Uber...")
    menor=math.inf
    mejorUber=0
    for i in range(No_A):
        aux=distancia(int(solicitud.split(" ")[1]), int(solicitud.split(" ")[2]),Xs[i],Ys[i])
        if(aux<menor):
            menor=aux
            mejorUber=i

    menor=round(menor,3)

    print("\nPara "+ solicitud.split(" ")[0]+ " la mejor distancia es ",menor, " al Uber No. ",mejorUber+1,"\n" )  
    
    datos_para_el_cliente = "Estas a "+str(menor)+ " del Uber No. "+str(mejorUber+1) 
    coneccion.send(datos_para_el_cliente.encode())  
    coneccion.close()

def distancia(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return distancia

if __name__ == "__main__":
    main()

