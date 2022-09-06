def potencia(y,z):
    if z==0:
        return 1
    else:
        return y*potencia(y,z-1)
y = int(input("Informe o número de base : "))
z = int(input("Informe o número seu expoente : "))
print (potencia(y,z))

def aurea(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return  aurea(n-1) + aurea(n-2)
n = int(input("Informe o termo que deseja calcular: "))
print (aurea(n))