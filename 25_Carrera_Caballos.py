#Importamos las librerias numpy para arreglos, random para los tiempos, 
#networkx y matplotlib para grafos y manejo de estructuras
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

#Se importa el objeto/clase arbol 
from Arbol import Arbol


#Matriz con mis 25 caballos (5x5)
General = np.zeros((5, 5))
dimension = General.shape
for x in range(dimension[0]):
    for y in range (dimension[1]):
        General[x, y] = random.randint(0,500)
print ('\n')
print ("Participan 25 caballos y solo pueden correr 5 por carrera:" )
print ('\n')
        

#Primeras 5 Carreras
print ("Primeras 5 carreras:" )
for x in range(5):
  print(" Carrera ", x + 1,"=", General[x])


#Resultados primeras 5 carreras
print("\nResultados de las primeras 5 carreras de menor a mayor: ")
for x in range(5):
  General[x].sort() 
  print(" Carrera ", x + 1,"=", General[x]) 
  

#Carrera 6 para obtener nuestro primer lugar
print("\nCarrera 6 entre los caballos mas rapidos de las primeras 5 carreras:")
R6= np.array([General[0,4],General[1,4],General[2,4],General[3,4],General[4,4]])
print(R6)

#Se hace el acomodo final con la función argsort que mueve las filas hasta la esquina inferior derecha
print("\nAcomodo despues de carrera 6:")
R6Final = General[np.argsort(General[:, 4])]
for x in range(5):
  print(R6Final[x]) 

#Carrera 7 para obtener nuestro segundo lugar
print("\nCarrera 7 por el segundo lugar:")
R7 = np.array([R6Final[2, 4],R6Final[3, 4],R6Final[3, 3],R6Final[4, 3],R6Final[4, 2]])
print(R7)
R7.sort()

#Posiciones finales de todos los caballos
print("\nPodio:")
print("1er lugar (mas rapido Carrera 6):", int(R6Final[4,4]), "pts")
print("2ndo lugar (mas rapido Carrera 7):", int(R7[4]), "pts")

print("\nLugares (Posicion 25 -- Posicion 1): ")
ListaGrafoFinal = np.concatenate(R6Final)
ListaGrafoFinal.sort()
print(ListaGrafoFinal)

arbol= Arbol(int(General[0, 0]), "Caballo  1")
arbol.agregar(int(General[0, 1]),"Caballo  2")
arbol.agregar(int(General[0, 2]),"Caballo  3")
arbol.agregar(int(General[0, 3]),"Caballo  4")
arbol.agregar(int(General[0, 4]),"Caballo  5")
arbol.agregar(int(General[1, 0]),"Caballo  6")
arbol.agregar(int(General[1, 1]),"Caballo  7")
arbol.agregar(int(General[1, 2]),"Caballo  8")
arbol.agregar(int(General[1, 3]),"Caballo  9")
arbol.agregar(int(General[1, 4]),"Caballo 10")
arbol.agregar(int(General[2, 0]),"Caballo 11")
arbol.agregar(int(General[2, 1]),"Caballo 12")
arbol.agregar(int(General[2, 2]),"Caballo 13")
arbol.agregar(int(General[2, 3]),"Caballo 14")
arbol.agregar(int(General[2, 4]),"Caballo 15")
arbol.agregar(int(General[3, 0]),"Caballo 16")
arbol.agregar(int(General[3, 1]),"Caballo 17")
arbol.agregar(int(General[3, 2]),"Caballo 18")
arbol.agregar(int(General[3, 3]),"Caballo 19")
arbol.agregar(int(General[3, 4]),"Caballo 20")
arbol.agregar(int(General[4, 0]),"Caballo 21")
arbol.agregar(int(General[4, 1]),"Caballo 22")
arbol.agregar(int(General[4, 2]),"Caballo 23")
arbol.agregar(int(General[4, 3]),"Caballo 24")
arbol.agregar(int(General[4, 4]),"Caballo 25")
arbol.lista()

#Se crea un arreglo tipo string vacio para guardar los nombres 
#de mis caballos y ponerlos en mi grafo
CaballoG = ["" for x in range(25)]

#Funcion para buscar el nombre de mis caballos en base a mi arreglo de 
#posiciones finales y meterlo a mi matriz llamada Caballo
for x in range(25):
  Dato = arbol.buscar(ListaGrafoFinal[x])
  CaballoG[x] = Dato.nombre

#Se agregan los nodos en base a nuestra matriz sorteada
Grafo = nx.Graph()
vertices_G = [CaballoG[24], CaballoG[23], CaballoG[22], CaballoG[21], CaballoG[20],CaballoG[19], CaballoG[18], 
              CaballoG[17], CaballoG[16], CaballoG[15], CaballoG[14], CaballoG[13], CaballoG[12], CaballoG[11], 
              CaballoG[10], CaballoG[9], CaballoG[8], CaballoG[7], CaballoG[6], CaballoG[5],CaballoG[4],
              CaballoG[3], CaballoG[2], CaballoG[1], CaballoG[0]]
Grafo.add_nodes_from(vertices_G)

#Se agregan los vértices a nuestro grafo
aristas_G = [(CaballoG[24], CaballoG[23]), (CaballoG[23], CaballoG[22]), (CaballoG[22], CaballoG[21]), (CaballoG[21], CaballoG[20]),
             (CaballoG[20], CaballoG[19]), (CaballoG[19], CaballoG[18]), (CaballoG[18], CaballoG[17]), (CaballoG[17], CaballoG[16]),
             (CaballoG[16], CaballoG[15]), (CaballoG[15], CaballoG[14]), (CaballoG[14], CaballoG[13]), (CaballoG[13], CaballoG[12]),
             (CaballoG[12], CaballoG[11]), (CaballoG[11], CaballoG[10]), (CaballoG[10], CaballoG[9]), (CaballoG[9], CaballoG[8]), 
             (CaballoG[8], CaballoG[7]), (CaballoG[7], CaballoG[6]), (CaballoG[6], CaballoG[5]), (CaballoG[5], CaballoG[4]),
             (CaballoG[4], CaballoG[3]), (CaballoG[3], CaballoG[2]), (CaballoG[2], CaballoG[1]), (CaballoG[1], CaballoG[0])]
Grafo.add_edges_from(aristas_G)

#Coordenadas de los nodos
ubica = {CaballoG[24]: (1, 21), CaballoG[23]: (1, 18), CaballoG[22]: (1, 15), CaballoG[21]: (1, 12), CaballoG[20]: (1, 9),
         CaballoG[19]: (1, 6), CaballoG[18]: (1, 3), CaballoG[17]: (5, 21), CaballoG[16]: (5, 18), CaballoG[15]: (5, 15), 
         CaballoG[14]: (5, 12), CaballoG[13]: (5, 9), CaballoG[12]: (5, 6), CaballoG[11]: (5, 3), CaballoG[10]: (9, 21),
         CaballoG[9]: (9, 18), CaballoG[8]: (9, 15), CaballoG[7]: (9, 12), CaballoG[6]: (9, 9), CaballoG[5]: (9, 6),
         CaballoG[4]: (9, 3), CaballoG[3]: (13, 21), CaballoG[2]: (13, 18), CaballoG[1]: (13, 15), CaballoG[0]: (13, 12)}


#Se crea el objeto tipo tupla para el grafo
class Tupla:
    def _init_(self, x, y):
       self.x = x
       self.y = y

puntoA = Tupla()
puntoA.x = ubica[CaballoG[24]][0]
puntoA.y = ubica[CaballoG[24]][1]
puntoB = Tupla()
puntoB.x = ubica[CaballoG[23]][0]
puntoB.y = ubica[CaballoG[23]][1]
puntoC = Tupla()
puntoC.x = ubica[CaballoG[22]][0]
puntoC.y = ubica[CaballoG[22]][1]
puntoD = Tupla()
puntoD.x = ubica[CaballoG[21]][0]
puntoD.y = ubica[CaballoG[21]][1]
puntoE = Tupla()
puntoE.x = ubica[CaballoG[20]][0]
puntoE.y = ubica[CaballoG[20]][1]
puntoF = Tupla()
puntoF.x = ubica[CaballoG[19]][0]
puntoF.y = ubica[CaballoG[19]][1]
puntoG = Tupla()
puntoG.x = ubica[CaballoG[18]][0]
puntoG.y = ubica[CaballoG[18]][1]
puntoH = Tupla()
puntoH.x = ubica[CaballoG[17]][0]
puntoH.y = ubica[CaballoG[17]][1]
puntoI = Tupla()
puntoI.x = ubica[CaballoG[16]][0]
puntoI.y = ubica[CaballoG[16]][1]
puntoJ = Tupla()
puntoJ.x = ubica[CaballoG[15]][0]
puntoJ.y = ubica[CaballoG[15]][1]
puntoK = Tupla()
puntoK.x = ubica[CaballoG[14]][0]
puntoK.y = ubica[CaballoG[14]][1]
puntoL = Tupla()
puntoL.x = ubica[CaballoG[13]][0]
puntoL.y = ubica[CaballoG[13]][1]
puntoM = Tupla()
puntoM.x = ubica[CaballoG[12]][0]
puntoM.y = ubica[CaballoG[12]][1]
puntoN = Tupla()
puntoN.x = ubica[CaballoG[11]][0]
puntoN.y = ubica[CaballoG[11]][1]
puntoO = Tupla()
puntoO.x = ubica[CaballoG[10]][0]
puntoO.y = ubica[CaballoG[10]][1]
puntoP = Tupla()
puntoP.x = ubica[CaballoG[9]][0]
puntoP.y = ubica[CaballoG[9]][1]
puntoQ = Tupla()
puntoQ.x = ubica[CaballoG[8]][0]
puntoQ.y = ubica[CaballoG[8]][1]
puntoR = Tupla()
puntoR.x = ubica[CaballoG[7]][0]
puntoR.y = ubica[CaballoG[7]][1]
puntoS = Tupla()
puntoS.x = ubica[CaballoG[6]][0]
puntoS.y = ubica[CaballoG[6]][1]
puntoT = Tupla()
puntoT.x = ubica[CaballoG[5]][0]
puntoT.y = ubica[CaballoG[5]][1]
puntoU = Tupla()
puntoU.x = ubica[CaballoG[4]][0]
puntoU.y = ubica[CaballoG[4]][1]
puntoV = Tupla()
puntoV.x = ubica[CaballoG[3]][0]
puntoV.y = ubica[CaballoG[3]][1]
puntoY = Tupla()
puntoY.x = ubica[CaballoG[2]][0]
puntoY.y = ubica[CaballoG[2]][1]
puntoX = Tupla()
puntoX.x = ubica[CaballoG[1]][0]
puntoX.y = ubica[CaballoG[1]][1]
puntoZ = Tupla()
puntoZ.x = ubica[CaballoG[0]][0]
puntoZ.y = ubica[CaballoG[0]][1]

#Diccionario
Puntos = {CaballoG[24]: puntoA, CaballoG[23]: puntoB, CaballoG[22]: puntoC, CaballoG[21]: puntoD, CaballoG[20]: puntoE, 
          CaballoG[19]: puntoF, CaballoG[18]: puntoG, CaballoG[17]: puntoH, CaballoG[16]: puntoI, CaballoG[15]: puntoJ, 
          CaballoG[14]: puntoK, CaballoG[13]: puntoL, CaballoG[12]: puntoM, CaballoG[11]: puntoN, CaballoG[10]: puntoO, 
          CaballoG[9]: puntoP, CaballoG[8]: puntoQ, CaballoG[7]: puntoR, CaballoG[6]: puntoS, CaballoG[5]: puntoT, 
          CaballoG[4]: puntoU, CaballoG[3]: puntoV, CaballoG[2]: puntoY, CaballoG[1]: puntoX, CaballoG[0]: puntoZ}
cont: int = 0
    
    #Diseño del grafo y características
nx.draw(Grafo, pos=ubica, node_color='orange', with_labels=True)
plt.show()
