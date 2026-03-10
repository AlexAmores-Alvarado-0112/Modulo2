def cabecera():
    """Cabecera de la aplicacion"""
    Head = """R
 _____                         _____                 
|  __ \                       |_   _|                
| |  \/ __ _ _ __ ___   ___ _ __| | __ _  __ _  __ _ 
| | __ / _` | '_ ` _ \ / _ \ '__| |/ _` |/ _` |/ _` |
| |_\ \ (_| | | | | | |  __/ |  | | (_| | (_| | (_| |
 \____/\__,_|_| |_| |_|\___|_|  \_/\__,_|\__, |\__, |
                                          __/ | __/ |
                                         |___/ |___/ 

                                         """
    
    print(Head)

#parte de la app principal

def Crea_taggbase(Nombre):
    """vrearun parametro basico usando las primeras 4 letras de su nombre
    
    parametro 
    Nombres: retorna el nombre del usuario
    
    parametro
    tag: crear tagg basico"""

    tagg= Nombre[0:4]
    print(tagg)


def tagg_inver(Nombre):
    """Crea un tagg invirtiendo el nombre comleto
    
    parametro
    String: el nombre del ususario 
    
    retorna
    String: el gametagg invertido"""

    tagg = Nombre[::-1]
    print(tagg)

def crar_tagg_inter(Nombre, Apellido):
    """Crear un tagg intercalado con el nombre y apellido del usuario
    
    parametro
    String: el nombre del usuario y apellidos intercalado 
    
    retorna
    String: el gametagg intercalado"""

    tagg = Nombre[0]
    tagg1 = Apellido[0]
    tagg2 = Nombre[1:]
    tagg3 = Apellido[1:]

    print(tagg, tagg1,tagg2, tagg3, sep="")


def crear_tag_elite(Nombre):
    """Crear un tagg con las ultimas letras del nombre del usuario
    
    parametro
    String: el nombre del usuario priemras letras y ultimas
    
    retorna
    String: el gametagg elite"""

    tagg = Nombre[:2]
    tagg1 = Nombre[-2:]
    print(tagg, tagg1, sep="")


def crear_tag_con_numero(Nombre,N):
    """Muestra el nombre y numero proporcionado
    Parametro
    Str: Nombre a analizar
    
    paramtero
    int: numero a unir"""
    
    
    tagg = Nombre[:4]
    print(tagg, N, sep="")

    
def mostrar_estadisticas(Nombre):
    """Muestra estadisitcas del nombre proporcionado
    Parametro
    Str: Nombre a analizar"""
    #Nombre = input("ingresa tu nombre: ")

    tagg = Nombre[0]
    tagg1= Nombre[-1]

    print("\n \tESTADÍSTICAS DE TU NOMBRE:") 

    print(f"Nombre completo: {Nombre} ")

    print("Longitud del nombre:", len(Nombre), "Caracteres") 

    print(f"Primera letra: {tagg}") 

    print(f"Última letra: {tagg1}")






cabecera()

print("================================")
print("TUS OPCIONES DE GAMME TAGG")
print("================================")




Nombre = input("ingresa tu nombre: ")
Apellido = input("Ingresa tru apellido: ")
N = int(input("Numero: "))




mostrar_estadisticas(Nombre)
crear_tag_con_numero(Nombre, N)
crear_tag_elite(Nombre)
crar_tagg_inter(Nombre, Apellido)
tagg_inver(Nombre)
Crea_taggbase(Nombre)


print("Elige tu favorito y conquista el mundo gammer")