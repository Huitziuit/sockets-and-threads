import random
import math
from sys import argv
import sys
from threading import Thread, Lock
import time


clientes=[]


def main():
    argv=sys.argv

    numAutos=10000000       #10000000            tarda 26seg
    anchoDelMapa=10000000000    #10,000,000,000

    #Coloca en lugares aleatorios los autos
    PosAutosX=[]
    PosAutosY=[]

    print("Colocando autos...")
    for i in range(numAutos):
        
        PosAutosX.append(random.randrange(0, anchoDelMapa, 1))
        PosAutosY.append(random.randrange(0, anchoDelMapa, 1))
    print("Autos colocados")
    print("\n\n========== Esperando clientes ==========\n")

    for i in range(10):
        t = Thread(target=calcula, args=(PosAutosX,PosAutosY,numAutos,int(argv[1]),int(argv[2])))
        t.start()
    
    time.sleep(60)
    #Encuentra la distancia mas corta del cliente a los autos
    #calcula(PosAutosX,PosAutosY,numAutos,int(argv[1]),int(argv[2]))



def calcula(Xs,Ys,No_A,XUsuario,YUsuario): 
    print("Calculando distancias a cada Uber...")
    menor=math.inf
    mejorUber=0
    for i in range(No_A):
        aux=distancia(XUsuario, YUsuario,Xs[i],Ys[i])
        if(aux<menor):
            menor=aux
            mejorUber=i

    print("mejor distancia ",menor, "Uber No. ",mejorUber+1 )  
    

def distancia(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    #print("distancia ", distancia)
    return distancia

if __name__ == "__main__":
    main()

