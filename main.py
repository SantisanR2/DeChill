# Inicio del programa

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a/b

def sumar(a, b):
    return a + b

def restar(a, b):
    return a-b

def main():
    print("Bienvenidos a La Calculadora Nashe")
    print("¿Que Quieres hacer?")
    print("Si quieres multiplicar oprime 1")
    print("Si quieres dividir oprime 2")
    print("Si quieres sumar oprime 3")
    print("Si quieres restar oprime 4")
    print("Si quieres salir oprime 5")
    respuesta=input("Dame tu numero puta: ")
    if respuesta=="1":
        num1=input("Dame el primer numero a multiplicar: ")
        num2=input("Dame el segundo numero a multiplicar: ")
        num1=int(num1)
        num2=int(num2)
        resp=multiplicar(num1, num2)
        print("El resultado de tu multiplicacion es: "+ str(resp)+ "\n\n")
        main()
    elif respuesta=="2":
        num1=input("Dame el numerador: ")
        num2=input("Dame el denominador: ")
        num1=int(num1)
        num2=int(num2)
        resp=dividir(num1, num2)
        print("El resultado de tu division es: "+ str(resp)+ "\n\n")
        main()
    elif respuesta=="3":
        num1=input("Dame el primer numero a sumar: ")
        num2=input("Dame el segundo numero a sumar: ")
        num1=int(num1)
        num2=int(num2)
        resp=sumar(num1, num2)
        print("El resultado de tu suma es: "+ str(resp)+ "\n\n")
        main()
    elif respuesta=="4":
        num1=input("Dame el numero al que le quieres restar: ")
        num2=input("Dame el numero que quieres restar: ")
        num1=int(num1)
        num2=int(num2)
        resp=restar(num1, num2)
        print("El resultado de tu resta es: "+ str(resp)+ "\n\n")
        main()
    elif respuesta=="5":
        pass
    else:
        print("Tocó cursito de español \n\n\n")
        main()
        
        
main()