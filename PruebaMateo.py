#def main():
#    listaLeche=["Colanta", "Alpina", "Hacendado", "Latti", 1]
#   cont=0
#    largoLista=len(listaLeche)
 #   while(cont<largoLista):
 #       item=listaLeche[cont]
 #       print(str(item))
 #       cont=cont+1
 #   for i in range(largoLista):
 #       print(listaLeche[i])
 #   for i in listaLeche:
    #    print(i)
def main():
    listanum=[]
    num=0
    resp=0
    while(len(listanum)<100):
        num=num+1
        listanum.append(num)
    for i in listanum:
        resp=resp+i
        if i==100:
            print(resp)
main()