def funcao_detecta(n):
    if(n % 2 == 0):
        return "É Par"
    else:
        return "É impar"


print (funcao_detecta(int(input("Entre com um número: "))))