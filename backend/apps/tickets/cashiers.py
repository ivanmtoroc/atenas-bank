from datetime import datetime, date, time, timedelta
from collections import deque


class Turno:
    def __init__(self, numeroTurno, usuario, tipoUsuario, actividad, horaLlegada, fecha):
        # Contructor con datos bases
        self.numeroTurno = numeroTurno
        self.usuario =  usuario
        self.tipoUsuario = tipoUsuario
        self.actividad = actividad
        self.estado = 0 # 0 significa sin atender, 1 atendido, 2 aplazado
        self.horaLlegada = horaLlegada
        self.horaInicio = ""
        self.horaFinal = "" # Se pone despues de haber atendido el turno
        self.tiempoTotal = ""
        self.fecha = fecha

class Cajero:
    def __init__(self, tipoCajero):
         self.tipoCajero = tipoCajero
         self.cola = deque()
         self.numeroSecuencia = 0 # Numero para identificar los turnos al llegar
         self.numeroCola = 0 # Nuemro de clientes en cola
         self.actualTurno = None

    def siguienteTurno(self): # Se toma el siguiente turno de la cola del cajero
        self.actualTurno = self.cola.popleft()
        print ("Siguiente turno: ", self.actualTurno.numeroTurno)
        return self.actualTurno.numeroTurno

    def iniciarTurno(self): # Cuando el cliente llega al cajero
        # Se toma el tiempo actual para el inicio del turno
        self.actualTurno.horaInicio = datetime.now()

    def finalizarTurno(self):
        self.numeroCola -= 1
        self.actualTurno.horaFinal = datetime.now() # Se toma el tiempo actual para el final del turno
        self.actualTurno.estado = 1 # Turno atendido
        self.actualTurno.tiempoTotal = self.actualTurno.horaFinal - self.actualTurno.horaInicio # Tiempo total de atencion
        # Aqui se envian los datos del turno a la base de datos

    def posponerTurno(self):
        if self.actualTurno.estado == 2: # Ya ha sido aplazado una vez
            print ("Turno eliminado, siguiente turno")
            # Se puede mandar a la base de datos el turno que ha sido eliminado
        else:
            self.actualTurno.estado = 2
            if len(self.cola) > 0: # Si hay ya gente en la cola, entonces el turno aplazado lo ponemos de segundo en la cola
                self.cola.insert(1,self.actualTurno)
            else:
                self.cola.add(self.actualTurno) # Cola vacia, entonces se vuelve a agregar el turno

# Funcion para saber en que posicion se encuentra la cola con menor numero de clientes en esperando
def cajeroMenosCola(cajeros):
    indice = 0
    for i in range(0, 7): # De 0 a 7, en total solo se hacen 7 iteraciones
        if cajeros[i].numeroCola > cajeros[i+1].numeroCola:
            indice = i+1
    return indice

# Funcion que verifica si en una cola hay clientes vip, si hay entonces retorna la posicion, sino retorna -1
def hayVip(cajero):
    indice = -1
    if len(cajero.cola) == 0:
        return indice
    for i in range(0,len(cajero.cola)):
        if cajero.cola[i].tipoUsuario == "vip":
            indice = i
    return indice

# Toda la logica para la gestion del turno al llegar un cliente vip
def parteVip(usuario, tipoUsuario, actividad):
    # Verificamos si alguna cola vip esta vacia
    if cajeros[6].numeroCola == 0:
        numeroTurno = cajeros[6].numeroSecuencia
        cajeros[6].numeroSecuencia += 1 # Aumentamos el numero de secuencia para el siguiete turno
        nuevoTurno = Turno(numeroTurno,usuario,tipoUsuario,actividad,datetime.now(),date.today())
        cajeros[6].cola.append(nuevoTurno) # Se agrega el turno a la cola
        cajeros[6].numeroCola += 1
    elif cajeros[7].numeroCola == 0:
        numeroTurno = cajeros[7].numeroSecuencia
        cajeros[7].numeroSecuencia += 1 # Aumentamos el numero de secuencia para el siguiete turno
        nuevoTurno = Turno(numeroTurno,usuario,tipoUsuario,actividad,datetime.now(),date.today())
        cajeros[7].cola.append(nuevoTurno) # Se agrega el turno a la cola
        cajeros[7].numeroCola += 1
    else: # Si ninguna cola vip esta desocupada, entonces va a la cola con menos clientes en espera
        indice = cajeroMenosCola(cajeros)
        vip = hayVip(cajeros[indice])
        if vip == -1: # No hay cliente vip en la cola, entonces se pone en la primera posicion de la cola
            numeroTurno = cajeros[indice].numeroSecuencia
            cajeros[indice].numeroSecuencia += 1 # Aumentamos el numero de secuencia para el siguiete turno
            nuevoTurno = Turno(numeroTurno,usuario,tipoUsuario,actividad,datetime.now(),date.today())
            cajeros[indice].cola.insert(0,nuevoTurno) # Se agrega el turno al principio de la cola
            cajeros[indice].numeroCola += 1
        else: # Significa que si hay un vip en la cola
            numeroTurno = cajeros[indice].numeroSecuencia
            cajeros[indice].numeroSecuencia += 1 # Aumentamos el numero de secuencia para el siguiete turno
            nuevoTurno = Turno(numeroTurno,usuario,tipoUsuario,actividad,datetime.now(),date.today())
            cajeros[indice].cola.insert(vip + 1,nuevoTurno) # Se agrega el turno atras del ultimo vip encontrado
            cajeros[indice].numeroCola += 1


# Funcion principal que se encarga de asignar los turnos a los cajeros:
# la idea es tener los 8 cajeros en un arreglo, asi cuando llegue un nuevo turno
# podemos identificar cual cajero tiene menos clientes en su cola, entonces asignamos el nuevo turno
# al cajero que tenga menos clientes esperando. Por defecto si la cola del cajero con la actividad que
# el cliente necesita esta vacia entonces es asignado a la cola de ese cajero, si no esta vacia, entonces
# simpre se asigna a el cajero con la menor cola. Se sigue el mismo proceso entre usuarios normal y vip
# la unica diferencia es que el usuario vip va al principio de cualquier cola a la que vaya, sin embargo si ya hay
# otro usuario vip en esta cola, entonces se pone detras de este usuario.

# Creacion de cajeros
cajero1 = Cajero("CR")
cajero2 = Cajero("CR")
cajero3 = Cajero("CR")
cajero4 = Cajero("IE")
cajero5 = Cajero("S")
cajero6 = Cajero("D")
cajero7 = Cajero("VP")
cajero8 = Cajero("VP")
cajeros = [cajero1, cajero2, cajero3, cajero4, cajero5, cajero6, cajero7, cajero8]
print("Cajeros:  ", cajeros)
cajeros[0].actualTurno = 123

def adminTurnos(usuario, tipoUsuario, actividad):
    if tipoUsuario == "vip":
        parteVip(usuario, tipoUsuario, actividad)
    else: # Es un cliente normal, se busca el cajero con menor cola y se pone e la ultima posicion
        indice = cajeroMenosCola(cajeros)
        numeroTurno = cajeros[indice].numeroSecuencia
        cajeros[indice].numeroSecuencia += 1 # Aumentamos el numero de secuencia para el siguiete turno
        nuevoTurno = Turno(numeroTurno,usuario,tipoUsuario,actividad,datetime.now(),date.today())
        cajeros[indice].cola.append(nuevoTurno) # Se agrega el turno a la cola
        cajeros[indice].numeroCola += 1

adminTurnos("jose", "normal", "S")
print("nombre cajero 0", cajeros[0].cola[0].usuario)
adminTurnos("juan", "normal", "S")
print("nombre cajero 1", cajeros[1].cola[0].usuario)
adminTurnos("pedro", "normal", "S")
print("nombre cajero 2", cajeros[2].cola[0].usuario)
adminTurnos("simon", "normal", "S")
print("nombre cajero 3", cajeros[3].cola[0].usuario)
adminTurnos("sebastian", "normal", "S")
print("nombre cajero 4", cajeros[4].cola[0].usuario)
adminTurnos("javier", "normal", "S")
print("nombre cajero 5", cajeros[5].cola[0].usuario)
adminTurnos("fabian", "normal", "S")
print("nombre cajero 6", cajeros[6].cola[0].usuario)
adminTurnos("ivan", "normal", "S")
print("nombre cajero 7", cajeros[7].cola[0].usuario)
adminTurnos("señor vip", "vip", "S")
print("nombre cajero 0", cajeros[0].cola[0].usuario)
print("nombre cajero 0 segundo cliente", cajeros[0].cola[1].usuario)
