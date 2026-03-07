print("\n Práctica tipos de argumentos en una función \n")

def organizar_fiesta(invitados,Tema = "Python",Lugar = "Aula de informatica"):
    #invitados = 45
    #Tema = "Python"
    #Lugar = "Aula de informatica"
    print(f"Preparando un fiesta para {invitados}")
    print(f"Tema de la fiesta {Tema}")
    print(f"Lugar de la celebracion{Lugar}\n")
organizar_fiesta(15)
print("\n")
organizar_fiesta(35, "Diplomado")
print("\n")
organizar_fiesta(45, "Cumpleaños", " Salon B")




