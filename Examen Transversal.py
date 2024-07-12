import random
import csv
import statistics
import math

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos = {}

def sueldos_aleatorios():
    global sueldos
    sueldos = trabajadores == random.randint(300000, 2500000)
    for trabajador in trabajadores:
        print("Sueldos asignados aleatoriamente")
        
def clasificar_sueldos():
    if not sueldos:
        print("Primero debe asignar sueldos aleatorios")
        return

    menores_800k = {k: v for k, v in sueldos.item() if v < 800000}
    entre_800_2m = {k: v for k, v in sueldos.item() if 800000 <= v <= 2000000}
    mayores_2m = {k: v for k, v in sueldos.item() if v > 2000000}
    print("Sueldos menores a $800.000 TOTAL: ", len(menores_800k))

    for k, v in menores_800k.items():
        print(f"Nombre empleado {k} Sueldo ${s}")

    print("\nSueldos entre $800.000 y $2.000.000 TOTAL: ", len(entre_800k_2m))

    for k, v in entre_800k_2m.items():
        print(f"Nombre empleado {k} Sueldo ${v}")

    print("\nSueldos superiores a $2.000.000 TOTAL: ", len(mayores_2m))

    for k, v in mayores_2m.items():
        print(f"Nombre empleado {k} Sueldo ${v}")
        
def mostrar_estadisticas():
    sueldos_valores = list(sueldos.values())
    sueldo_mas_alto = max(sueldos.values)
    sueldo_mas_bajo = min(sueldos.values)
    promedio_sueldos = statistics.mean(sueldos.valores)

    print(f"Sueldo mas alto: ${sueldo_mas_alto}")
    print(f"Sueldo mas bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")

def reporte_sueldos():
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for empleado, sueldo_base in sueldos.item():
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.012
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([empleado, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{empleado} - Sueldo base: ${sueldo_base}, Descuento Salud: ${descuento_salud:.2f}, Descuento AFP: ${descuento_afp:.2f}, Sueldo Liquido: ${sueldo_liquido:.2f}")            
            
def salir_del_programa():
     print("\nFinalizando programa...")
     print("\nDesarrollado por Benjamin Yantzen")
     print("RUT 21980530-6")

def main():
    while True:
        print("\nMenu:")
        print("\n1. Asignar sueldos aleatorios")
        print("\n2. Clasificar sueldos")
        print("\n3. Ver estadísticas")
        print("\n4. Reporte de sueldos")
        print("\n5. Salir del programa")

        opcion = input("Seleccione una opcion (1-5): ")
        if opcion == '1':
            sueldos_aleatorios()
        if opcion == '2':
            clasificar_sueldos()
        if opcion == '3':
            mostrar_estadisticas()
        if opcion == '4':
            reporte_sueldos()
        if opcion == '5':
            salir_del_programa()
            break
        else:
            print("Opcion invalida, intente nuevamente")

if __name__ == "__main__":
    main()
