import random
import math
from sys import argv
import sys

def main():
    argv=sys.argv

    numAutos=200000
    anchoDelMapa=1000000000

    mejorUber=0

    #Coloca en lugares aleatorios los autos
    PosAutosX=[]
    PosAutosY=[]

    for i in range(numAutos):
        
        PosAutosX.append(random.randrange(0, anchoDelMapa, 1))
        PosAutosY.append(random.randrange(0, anchoDelMapa, 1))

    #Encuentra la distancia mas corta el clienta a los autos
    menor=math.inf
    for i in range(numAutos):
        aux=distancia(int(argv[1]), int(argv[2]),PosAutosX[i],PosAutosY[i])
        if(aux<menor):
            menor=aux
            mejorUber=i

    print("menor distancia ",menor, "Uber No. ",mejorUber+1 )  

def distancia(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    print("distancia ", distancia)
    return distancia

if __name__ == "__main__":
    main()

