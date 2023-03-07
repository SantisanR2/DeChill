
def main():
    #Número máximo
    max = 100
    suma1 = 0
    
    for i in range(max+1):
        suma1 += i
    print("Por el primer for da: " + str(suma1))
    
    cont = 0
    suma2 = 0
    
    while(cont <= max):
        suma2 += cont
        cont += 1
    print("Usando el while da: " + str(suma2))
    
    natu = list(range(0,max+1))
    suma3 = 0
    
    for i in natu:
        suma3 += i
    print("Usando for each da: " + str(suma3))
    
main()