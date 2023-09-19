from graphviz import Graph as gr
from graphviz import Digraph as gr2
#Objeto de graphviz para hacer el grafo graficamente
grafico = gr('G', filename='grafo', engine='neato') 
#Objeto de graphviz para hacer el arbol graficamente
arbol = gr2('G', filename='arbol', engine='dot')

#Clase nodo
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre #atributo nombre para identificrlos
        self.vecinos = [] #lista de las conexiones que tienen
        self.distancias = [] #lista de distancias que tiene con cada conexion
        #La relacion de las distancias con las otras conexiones se deben realizar
        #mediante los indices, ejemplo, si este nodo se llama 
        #vecinos[0]= a, distancias[0]= 4, nos dice que tiene conexion con el nodo
        #a y su conexion tiene una distancia de 4
    

    #Metodo que muestra en pantalla las conexiones que tiene el nodo
    def Vecinos(self):
        rta = ''
        if(len(self.vecinos) != 0):
            for v in self.vecinos:
                rta += v + " "
        else:
            rta = "No tiene conexiones"
        print (rta)
    

    #Metodo para validar las conexiones, no puede hacer conexiones 
    #con el mismo nodo, y no pueden haber dos conexiones iguales
    def Validar(self,nombre):
        if (nombre in self.vecinos or nombre == self.nombre):
            return False
        return True
#FIN DEL OBJETO NODO


#Metodo para validar si el nombre del nodo que se va a usar
# ya se usó o está disponible, no pueden haber dos nodos
# con el mismo nombre
def Validar(nombre):
    busqueda = True
    for n in grafo:
        if(n.nombre == nombre):
            busqueda = False
    return busqueda


# Cuando se realiza una conexion, debemos validar si debemos realizar
# la misma conexion desde el otro nodo, esto se debe hacer siempre y cuando 
# no sea el nodo objetivo o el nodo inicial
def conexionReciproca(nombre1,nombre2,distancia):
    if(nombre1 == grafo[(len(grafo) - 1)]):
        return 0
    for n in grafo:
        if(n.nombre == nombre1 and nombre2 != grafo[0].nombre and nombre2 != grafo[len([grafo])-1].nombre): #and nombre1 != grafo[(len(grafo) - 1)]
            n.vecinos.append(nombre2)
            n.distancias.append(distancia)


def generarArbol():
    # Establecemos los atributos para el nodo en el grafico
    arbol.attr('node', shape='circle')

     # Matriz todos, ayudará a llevar control de los nodos creados para el arbol, ya que no podemos crear dos nodos con el mismo nombre esta matriz va a trabajar así:
     # las filas deben ser del mismo tamaño que el array grafo, y en las columnas dejamos un numero apreciativo que considero no va a sobrepasar de la creacion de nodos
     # así se veria :
     # [[0,0,0,0] posicion 0 corresponde al primer nodo
     #  [b0,b1,b2,0] posicion 1 corresponde al segundo nodo
     #  [0,0,0,0] posicion 2 corresponde al tercer nodo
     #  [0,0,0,0] posicion 3 corresponde al cuarto nodo
     #  [0,0,0,0] posicion 4 corresponde al quinto nodo
     #  [0,0,0,0]] posicion 5 corresponde al sexto nodo
     # Vector Grafo: 
     # [a, posicion 0
     #  b, posicion 1
     #  c, posicion 2
     #  d, posicion 3
     #  e, posicion 4
     #  f] posicion 5
     # 
     # 
     # 
     # *
    
    



    # Si o si el arbol debe iniciar por el nodo inicial, lo ponemos de una vez en el grafico
    todos[0].append(grafo[0].nombre)
    prueba(grafo[0], "")        
    arbol.view()

def buscarEspacio(pos):
    if(len(todos[pos]) == 0):
        return 0
    else:
        return len(todos[pos])

def prueba(nodo, nombreAnterior):
    print(nodo.nombre[:1])
    print ("Entramos al ciclo")
    posicion = 0
    indice = 0
    if(verificarCaminoArbol(nodo.nombre[:1])  or nodo.nombre == grafo[0].nombre):
        # Guardamos la posicion del nodo a trabajar
        for n in range(tam):
            if(grafo[n].nombre == nodo.nombre):
                posicion = n
        # Tenemos que validar cuantos nodos iguales hemos agregado o recorrido
        indice = buscarEspacio(posicion)
        indice = indice-1
        # Despues de validar en que posicion vamos de agregar los nodos, pasamos a hacer la respectiva asignacion
        todos[posicion][indice] += str(indice)
        print(todos[posicion][indice])
        # Ahora tenemos que agregar el nodo al grafico, el valor real del nodo será ocultado por la etiqueta del nombre propio del nodo, ejemplo 
        # a1,a esos dos son los parametros, en el grafico debe aparecer a, pero su verdadero valor es a1
        arbol.node(todos[posicion][indice],grafo[posicion].nombre)
        # Registramos el camino que estamos tomando
        if(nombreAnterior != ""):
            arbol.edge(nombreAnterior,todos[posicion][indice])
        for vecino in nodo.vecinos:
            p = 0
            for n in range(tam):
                if(grafo[n].nombre == vecino):
                    p = n
            print(grafo[p].nombre)
            buscarEspacio(p)
            print(todos)
            print("longitud: "+str(len(todos[p])))
            todos[p].append(grafo[p].nombre)
            print(todos)
            print("longitud: "+str(len(todos[p])))
            print(str(caminoArbol))
            print("nodo nuevo: "+grafo[p].nombre)
            prueba(grafo[p],todos[posicion][indice])
        if (caminoArbol[-1] == grafo[-1].nombre):
            if(len(caminos)==0):
                caminos.append([])
                for n in range(len(caminoArbol)):
                    if(n==0):
                        caminos[-1].append(caminoArbol[n])
                    else:
                        caminos[-1].append(caminoArbol[n])
            else:
                caminos.append([])
                for n in range(len(caminoArbol)):
                    caminos[-1].append(caminoArbol[n])
                    
                
            #caminos.append(caminoArbol)
            sum = 0
            for i in range(len(caminoArbol)):
                for a in range(tam):
                    if(grafo[a].nombre == caminoArbol[i]):
                        ppp = a
                        if(i < (len(caminoArbol)-1)):
                            print("nodo en el que vamos: "+grafo[ppp].nombre )
                            print("nodo con el que conecta: "+grafo[ppp].vecinos[grafo[ppp].vecinos.index(caminoArbol[i+1])] )
                            print("posicion nodo conexion: : "+ str(grafo[ppp].vecinos.index(caminoArbol[i+1])) )
                            print("")
                            siguiente = grafo[ppp].vecinos.index(caminoArbol[i+1]) 
                            print(grafo[ppp].distancias[siguiente])
                            sum += grafo[ppp].distancias[siguiente]
            caminos[-1].append(sum)
            print("----------------------------------------------------")
            print("la trayectoria : " + str(caminoArbol))
            print("la trayectoria : " + str(caminos))
            print("tiene un peso de : " + str(caminos[-1][-1]))
        caminoArbol.pop()
        print(todos)
        print(caminoArbol)
        
        







# Debemos verificar cuando creamos arbol el camino que vamos llevando 
# si ya pasamos por ese nodo, no debemos volver a crear conexion con él
# caso contrario enviamos la respuesta para que si lo agrege y de paso
# agregamos el nuevo nodo en el recorrido de la
def verificarCaminoArbol(nodo):
    print("Este es el nodo que estamos buscando: *"+nodo+"*")
    print("Este es nuestro recorrido actual: *"+str(caminoArbol)+"*")
    if(len(caminoArbol) == 0):
        caminoArbol.append(nodo)
        print("Se inserta primer nodo al recorrido")
        return True
        
    for n in range(len(caminoArbol)):
        if(nodo == caminoArbol[n]):
            print("Si se encontro el nodo en el recorrido")
            print(caminoArbol)
            for m in range(len(todos)):
                if(nodo in todos[m]):
                    todos[m].pop()
            return False
    print("No se ha recorrido, lo agregamos")
    caminoArbol.append(nodo)
    return True


# PROGRAMA PRINCIPAL
# solicitamos la cantidad de nodos, se guardan en la variable tam
global caminos
caminos = []
global caminoArbol
caminoArbol = []
global grafo
grafo = []
global todos
todos = []
global tam
tam = int(input("Ingrese cantidad de nodos a trabajar en el grafo: "))
for n in range(tam):
    todos.append([])

# Luego de saber la cantidad de nodos a trabar procedemos a solicitarlos
for nodo in range(tam):
    estado = False # variable usada para validar si el nombre 
    # a usar en el nodo a crear está disponible o no
    while(estado == False): # Ciclo que garantiza que se ingresará un nombre valido
        # solicitamos el nombre del nuevo nodo
        nodot = input("Ingrese nombre del nodo "+str(nodo+1)+" ")

        # hacemos uso del metodo para validar si el nombre está disponible
        if (Validar(nodot)): 

            # damos atributos al nodo en la parte grafica
            grafico.attr('node', shape='circle', rank='same')
            # agregamos el nodo al grafico
            grafico.node(nodot)
            # Creamos un objeto nodo
            objNodo = Nodo(nodot)
            # Insertamos el objeto nodo al array que contiene el grafo
            grafo.append(objNodo)
            # cambiamos el estado para salir del ciclo y proceder con el siguiente nodo
            estado = True
        else:
            print("Nombre ya usado, ingrese otro")


# Despues de agregar los nodos al array, que nos ayuda en la parte logica 
# y en el grafico procedemos a crear las conexiones, recorremos el vector de nodos, el grafo
for nodo in grafo:
    estado = False # variable usada para validar si la conexion 
    # ya se hizo o se puede o no

    # Ciclo que permite garantizar que podemos agregar las conexiones necesarias en cada nodo
    while(estado == False):
        # Mostramos las conexiones que tiene el nodo en ese momento
        print ("El nodo *",nodo.nombre,"* tiene conexion con estos nodos actualmente: ")
        nodo.Vecinos()

        # Preguntamos si quieren agregar una conexion
        new = input("Desea agregar una conexion? s/n: ")

        # Validamos si debemos crear una conexion

        
        if (new == 'n'): # cuando el usuario dijite la n salimos del ciclo con el nodo actual y pasamos a preguntar por el siguiente
            estado = True
        else:
            if(new == 's'): # cuando el usuario dijite s solicitamos los datos de la conexion
                nuevoNodo = input("Ingrese el nombre del nodo con el que conecta: ")
                distancia = int(input("Ingrese la distancia de la conexión: "))

                # Validamos si la conexion solicitada ya existe
                if(nodo.Validar(nuevoNodo)):
                    # Generamos la conexion en la parte grafica
                    grafico.edge(nodo.nombre, nuevoNodo,str(distancia))
                    # Agregamos la conexion en los datos del nodo
                    nodo.vecinos.append(nuevoNodo)
                    # Agregamos la distancia de la conexion en el nodo
                    nodo.distancias.append(distancia)
                    # Se llama a conexion Reciproca
                    """print(nodo.nombre)
                    print(grafo[-1].nombre)
                    input("seguir")"""
                    if(nuevoNodo != grafo[-1].nombre):
                        conexionReciproca(nuevoNodo,nodo.nombre,distancia)
                else:
                    print("Ya existe esa conexión")
            else: # dado el caso que ingresen algo difernte no hacemos mas que mostrar el mensaje
                print ("\n Solo se aceptan estas opciones: s (si) n (no) \n")



"""objNodo = Nodo('a')
grafo.append(objNodo)
objNodo = Nodo('b')
grafo.append(objNodo)
objNodo = Nodo('c')
grafo.append(objNodo)
objNodo = Nodo('d')
grafo.append(objNodo)
objNodo = Nodo('e')
grafo.append(objNodo)
objNodo = Nodo('f')
grafo.append(objNodo)

grafo[0].vecinos.append('b') #a
grafo[0].distancias.append(4)
grafo[0].vecinos.append('c')
grafo[0].distancias.append(3)

grafo[1].vecinos.append('e') #b
grafo[1].distancias.append(2)

grafo[2].vecinos.append('d') #c
grafo[2].distancias.append(2)
grafo[2].vecinos.append('e')
grafo[2].distancias.append(5)

grafo[3].vecinos.append('c') #d
grafo[3].distancias.append(2)
grafo[3].vecinos.append('e')
grafo[3].distancias.append(4)
grafo[3].vecinos.append('f')
grafo[3].distancias.append(3)

grafo[4].vecinos.append('b') #e
grafo[4].distancias.append(2)
grafo[4].vecinos.append('c')
grafo[4].distancias.append(5)
grafo[4].vecinos.append('d')
grafo[4].distancias.append(4)
grafo[4].vecinos.append('f')
grafo[4].distancias.append(4)"""





grafico.view() # Esto permite ver el grafico
print(grafico.source) # Esto permite generar el codigo .dot con el que trabaja el archivo de la imagen
generarArbol() #Pasamos a crear el arbol
menor = 9999
posMenor = 0
for n in range(len(caminos)):
    print(str(caminos[n][-1]) + " -------- " + str(menor))
    if(caminos[n][-1] < menor):
        menor = caminos[n][-1]
        posMenor = n
print("----------------------------")
print("Se encontraron estos caminos: ")
for n in range(len(caminos)):
    print(caminos[n])
print("//////////////////////////////////")
print("El resultado de la buqueda es: "+ str(caminos[posMenor]))




