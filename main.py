import Ejercicio_JSON as PJ

lista_coches =[]

Nombre_archivo = input("Determina un nombre para el archivo: ")

while True:
    marca = input("Marca del coche: ")
    if marca == "fin":
            break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")

    linea = {}
    linea["Marca Coche"] = marca

    linea["Modelo"] = modelo

    linea["Combustible"] = combustible

    linea["Cilindrada"] = cilindrada
    lista_coches.append(linea)

PJ.store(lista_coches, Nombre_archivo)
lista_coches = []
print("Lista de coches: \n", lista_coches)

lista_coches = PJ.retrieve(Nombre_archivo)
print("Lista de coches: \n", lista_coches)
