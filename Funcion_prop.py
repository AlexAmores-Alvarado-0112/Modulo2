def contar_caracteres():
    """Funcion para contar caracteres 3 de marzo de 2026"""
    print("\nla frase 'Aprender Python es divertido' tiene",len("Aprender Python es divertido"),"caracteres\n")

contar_caracteres()

def convertir_numero():
    """Convertir un numero de entero a cadena de texto y a flotante"""
    n = 35
    n1 = str(n)
    n2 = float(n)
    print("Entero:   ",n,"   Tipo:",type(n))
    print("Cadena:   ",n1,"   Tipo:",type(n1))
    print("Flotante: ",n2," Tipo:",type(n2))

convertir_numero()