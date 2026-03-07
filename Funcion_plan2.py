def Dis_Plan(): #Definicion de la funcion para listar planetas y la distancia
    planetas = [
        'mercurio',#Tupla(Clave y valor)
        'venus',
        'marte',
        'jupiter',
        'saturno',
        'urano',
        'neptuno'
    ]
    dista = [
        77,
        38,
        56,
        628,
        1275,
        2724,
        4351
    ]
    print("\n\nDistancias de los planetas\n")# titulo

    for nombre, distancia in zip(planetas, dista):#Zip es para la variable junto a el valor que tiene
        print(f"Nombre del planeta: {nombre}\nDistancia al planeta: {distancia} millones de Km \n\n")


Dis_Plan()

#for nombre, distancia in planetas.items():#Items es para la variable junto a el valor que tiene
#        print(f"Nombre del planeta: {nombre}\nDistancia al planeta: {distancia} millones de Km \n\n")