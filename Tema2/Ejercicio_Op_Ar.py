def calcular_calorias():

    C = int(input("ingresa los gramos de los carbohidratos: "))
    P = int(input("ingresa los gramos de las proteinas: "))
    G = int(input("ingresa los gramos de las grasas: "))
    Cal = 4
    Calg = 9

    Carbohidratos = C * Cal
    Proteinas = P * Cal
    Grasas = G * Calg
    Total = Carbohidratos + Proteinas + Grasas
 
    print("Calorias Totales", Total)
calcular_calorias()
    