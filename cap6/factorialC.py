import facto
x=1
n=5
while(x!=0):
    print("\t\t\t------------------------------------")
    print("\t\t\t|     BIENVENIDO AH FACTORIZANDO   |")
    print("\t\t\t|1.factorizar iterando             |")
    print("\t\t\t|2.factorizar recursiva            |")
    print("\t\t\t------------------------------------")
    p=int(input("fac: "))
    if(p==1):
        print("aqui usamos iteracion-->",facto.factorialiterando(n))
    if(p==2):
        print("usamos recursividad -->",facto.factorial(n))
    x=int(input("Desea salir: "))



