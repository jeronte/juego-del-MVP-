
nombre1= input("como es le nombre de jugador1?:")
nombre2= input("como es le nombre de jugador2?:")

jugador1= input(nombre1 + " hola que elegís?:").lower()
jugador2= input(nombre2 + " hola que elegís?:").lower()

condicion1= jugador1=="piedra" and jugador2 =="tijera"
condicion2= jugador1=="papel" and jugador2=="piedra"
condicion3= jugador1== "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("empate")
elif condicion1 or condicion2  or condicion3:
    print("ganaste!",nombre1)
else:
    print("ganaste!",nombre2)
