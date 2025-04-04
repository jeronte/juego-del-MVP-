import random

numero_secreto=random.randint(0,2)
cant_intentos = 0
cant_max_intentos = 5
adivinado=False
print("bienvenido, si queres ser como el MVP tenes que aprender a actuar como uno")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada=input("a cuantas mujeres le habla el MVP por trimestre?: ")
    numero=int(entrada)
    #este segundo renglon se utilizó para hacer el casteo ya que input lo ingresa como string y no como numero

    if numero == numero_secreto:
        print("felicidades pensas como el MVP")
        adivinado = True
    elif numero > numero_secreto:
        print("estas siendo muy optimista muchacho")
    cant_intentos+=1

if not cant_intentos < cant_max_intentos: 
    print("si haces juego de volumen el MVP pierde exclusividad")


