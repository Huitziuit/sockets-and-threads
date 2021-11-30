#Author Huitziuit 
import random
import math
from sys import argv
import sys
from threading import Thread, Lock
import time
import socket
PORT = 7000
HOST = "127.0.0.1"

clientes=[]


def main():
    lock=Lock()         #candado para acceder a clientes[]    

    numAutos=       10000000       #10000000            tarda 10seg en relaizar los calculos
    anchoDelMapa=10000000000    #10,000,000,000

    #Coloca en lugares aleatorios los autos
    PosAutosX=[]
    PosAutosY=[]

    print("======== Colocando autos... ========")
    for i in range(numAutos):
        
        PosAutosX.append(random.randrange(0, anchoDelMapa, 1))
        PosAutosY.append(random.randrange(0, anchoDelMapa, 1))
    print("\n---> Autos colocados\n---> Creando socket...")

    #Crea el socket
    try:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("---> Socket creado.\n")
        mySocket.bind((HOST, PORT))        
        mySocket.listen()    
        print("\n======== Esperando clientes ========")
        print("======= En el puerto ", PORT," =======")
        while True:
            #si se detecta una coneccion se asigna el nuevo socket a un nuevo hilo
            coneccion, addrClient = mySocket.accept()    
            print ("\n\nSe detecto una coneccion\n----> Asignando coneccion a un hilo" )
            t = Thread(target=calcula, args=(coneccion, numAutos, PosAutosX, PosAutosY,lock)) 
            t.start()   #corriendo hilo

    except socket.error as err:
        print(err)


def calcula(Coneccion,No_A,Xs,Ys,lock):
    global clientes
    coneccion=Coneccion 
    coordenadas = coneccion.recv(1024).decode()# recibe lo que el cliente envio
    print("--------> Calculando distancias de "+ coordenadas.split(" ")[0]+" a cada Uber...")
    menor=math.inf
    mejorUber=0
    #calcula las distancias de cada uber al cliente 
    for i in range(No_A):
        aux=distancia(int(coordenadas.split(" ")[1]), int(coordenadas.split(" ")[2]),Xs[i],Ys[i])
        if(aux<menor):
            menor=aux
            mejorUber=i

    menor=round(menor,3)

    print("\nPara "+ coordenadas.split(" ")[0]+ " la mejor distancia es ",menor, " al Uber No. ",mejorUber+1,"\n" )  
    
    #Respuesta de la operacion para el cliente
    resCliente = "Estas a "+str(menor)+ " del Uber No. "+str(mejorUber+1) 
    coneccion.send(resCliente.encode()) 

    #comienzo de la seccion critica
    lock.acquire()
    clientes.append(coordenadas.split(" ")[0]) 
    lock.release()
    #fin de la seccion critica

    print("***** Clientes atendidos ",clientes)
    coneccion.close()

def distancia(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return distancia

if __name__ == "__main__":
    main()

