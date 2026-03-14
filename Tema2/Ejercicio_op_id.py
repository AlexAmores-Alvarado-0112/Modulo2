
print("\n Adivina la palabra\n")

palabra_adivinar = ("Tangamandapio")


def adivinar_palabra(letra_prueba, palabra_intento):
    letra_prueba1 = letra_prueba in palabra_adivinar
    print("\n¿La letra de prueba se encuentra en la palabra? ", letra_prueba1) 
    len1 = len(palabra_intento)
    len2 = len(palabra_adivinar)
    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len1 == len2)
    print("\nEl jugador gana:", resultado_adivinanza, "\n")
adivinar_palabra("a", "Tangamandapio")


    