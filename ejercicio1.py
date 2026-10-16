#definicion de funciones
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

#ciclo principal
while True:
    #eleccion de proceso
    print("#################")
    print("Calculadora Basica\n\n")
    print("1.SUMA")
    print("2.RESTA")
    print("3.MULTIPLICAR")
    print("4.DIVIDIR")
    print("5.SALIR\n\n")
    entrada= int(input("Digite la accion a realizar:"))
    print("#################")

    #logica segun proceso elegido
    match entrada:
        case 1:
            numA = float(input("Digite el primer numero: "))
            numB = float(input("Digite el segundo numero: "))

            result = suma(numA,numB)

            print(f"el resultado de la suma entre {numA} y {numB} es = {result}")
        case 2:
            numA = float(input("Digite el primer numero: "))
            numB = float(input("Digite el segundo numero: "))

            result = resta(numA,numB)

            print(f"el resultado de la resta entre {numA} y {numB} es = {result}")
        case 3:
            numA = float(input("Digite el primer numero: "))
            numB = float(input("Digite el segundo numero: "))

            result = multiplicar(numA,numB)

            print(f"el resultado de la multiplicación entre {numA} y {numB} es = {result}")
        case 4:
            numA = float(input("Digite el primer numero: "))
            numB = float(input("Digite el segundo numero: "))

            #solucion por si el usuario intenta dividir por 0
            while numB == 0:
                print("no se puede dividir entre 0, vuelva a digitar")
                numB = float(input("Digite el segundo numero: "))

                if numB != 0:
                    break
                

            result = dividir(numA,numB)

            print(f"el resultado de la division entre {numA} y {numB} es = {result}")
        case 5:
            print("gracias por usar el programa!!")
            break
        #default por si el usuario elige un numero no dicho en la lista de ociones
        case _:
            print("elegiste una opcion no listada")
            while entrada > 5 or entrada < 1:
                print("#################")
                print("Calculadora Basica\n\n")
                print("1.SUMA")
                print("2.RESTA")
                print("3.MULTIPLICAR")
                print("4.DIVIDIR")
                print("5.SALIR\n\n")
                entrada= input("Digite la accion a realizar:")
                print("#################")