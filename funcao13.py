def verificar_palindromo(texto):
    texto = texto.lower().peplace(" ", "")
    return texto == texto[::-1]
    
    texto = "Socorrame-me, subi no ônibus em Marrocos"
    if verificar_palindromo(texto):
        print(texto, "é um palidomo. ")

    else:
        print(texto, "não é um palindromo")