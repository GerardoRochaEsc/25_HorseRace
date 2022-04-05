#Se importa nuestro objeto caballo para nuestra funciones
from Caballo import caballo

class Arbol:

    #Método para inicializar
    def __init__(self, tiempo, nombre):
        self.raiz = caballo(tiempo, nombre)

    #Método para agregar a la lista
    def _agregarpriv(self, nodo, tiempo, nombre):
        if tiempo < nodo.tiempo:
            if nodo.izquierda is None:
                nodo.izquierda = caballo(tiempo, nombre)
            else:
                self._agregarpriv(nodo.izquierda, tiempo, nombre)
        else:
            if nodo.derecha is None:
                nodo.derecha = caballo(tiempo, nombre)
            else:
                self._agregarpriv(nodo.derecha, tiempo, nombre)

    #Método para agregar a los tiempos
    def _listapriv(self, nodo):
        if nodo is not None:
            self._listapriv(nodo.derecha)
            print(nodo.nombre, "-", nodo.tiempo,"segundos")
            self._listapriv(nodo.izquierda)
            
    #Método para buscar nodos
    def __buscar(self, nodo, tiempo):
       if nodo is None:
           return None
       if nodo.tiempo == tiempo:
           return nodo
       if tiempo < nodo.tiempo:
           return self.__buscar(nodo.izquierda, tiempo)
       else:
           return self.__buscar(nodo.derecha, tiempo)

        #Metodo para desplegar listado
    def lista(self):
        print("\nLista de caballos en orden: ")
        self._listapriv(self.raiz)
        print("")
        
    #Metodo para acceder a la funcion privada buscar
    def buscar(self, tiempo):
        return self.__buscar(self.raiz, tiempo)

    #Metodo para agregar Caballos
    def agregar(self, tiempo, nombre):
        self._agregarpriv(self.raiz, tiempo, nombre)
