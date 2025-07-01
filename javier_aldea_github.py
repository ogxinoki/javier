def sumar(a,b):
    return a+b

while True:
    try:   
        n1 = int(input("ingrese valor: "))
        n2 = int(input("ingrese valor: "))
        break
    except:
        print("ingrese valor entero")

print(sumar(n1,n2))