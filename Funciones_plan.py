def Dis_Plan(): #Definicion de la funcion para listar planetas y la distancia
    planetas = {
        'mercurio': 77,#Tupla(Clave y valor)
        'venus': 38,
        'marte': 56,
        'jupiter': 628,
        'saturno': 1275,
        'urano': 2724,
        'neptuno': 4351
    }
    print("\n\nDistancias de los planetas\n")# titulo

    for nombre, distancia in planetas.items():#Items es para la variable junto a el valor que tiene
        print(f"Nombre del planeta: {nombre}\nDistancia al planeta: {distancia} millones de Km \n\n")


Dis_Plan()