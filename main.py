import os
from core import CitasManager

def mostar_menu():
    print("----- Menu -----")
    print("1. Registrar cita: ")
    print("2. buscar citas: ")
    print("3. Modificar cita: ")
    print("4. Cancelar cita:")
    print("5. Salir del programa: ")

def agregar_cita(citas_manager):
    print("----Agregar cita----")
    nombre = input("Ingrese en nombre del paciente: ")
    fecha = input("Ingrese la fecha (aaaa-mm-dd) de la cita:")
    hora = input("Ingrese la hora de la cita: ")
    motivo = input("Ingrese el motivo de la consulta: ")

    cita = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo

    }
    citas_manager.agregar_cita(cita)
    print("La cita ha sigo agregada exitosamente....")

def buscar_cita(citas_manager):
    print("----Buscar cita----")
    criterio = input("Ingrese el criterio de la busqueda(nombre o fecha): ")

    citas_encontradas = citas_manager.buscar_citas(criterio)
    if citas_encontradas:
        print("citas Encontradas: ")
        for cita in citas_encontradas:
            print(f"Nombre:{cita['nombre']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}")
    else:
        print("Lo sentimos "+"No se encontraron citas....")

def modificar_citas(citas_manager):
    print("----Modificar citas----")
    fecha = input("Ingrese la fecha de la cita a modificar:")
    hora = input("Ingrese la hora de la cita a modificar:")

    for cita in citas_manager.citas:
        if cita['fecha'] == fecha and  cita['hora'] == hora:
            nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
            nuevo_motivo = input("Ingrese el nuevo motivo de la consulta: ")

            cita_moficada = {
                "nombre": nuevo_nombre,
                "fecha": cita['fecha'],
                "hora": cita['hora'],
                "motivo": nuevo_motivo,

            }
            if citas_manager.modificar_cita(cita_moficada):
                print("La cita ha sido modificada correctamente...")
            else:
                print("No pudo modificar la cita.")
            return        
    print("No se encontor la cita especificada...")

def cancelar_citas(citas_manager):
    print("----Cancelar cita----")
    fecha = input("Ingresar la fecha de la cita a cancelar :")
    hora = input("ingrese la hora  de la cita a cancelar :")

    for cita in citas_manager.citas:
            if cita['fecha'] == fecha and cita['hora'] == hora:
                if citas_manager.cancelar_cita(cita):
                    print("Cita cancelada exitosamente..")
                else:
                    print("No se pudo cancelar la cita")
                return
    print("No se encontro la cita especificada a cancelar")

def main():
    citas_manager = CitasManager('citas.json')

    while True:
        mostar_menu()
        opcion = 0
        opcion = int(input("Seleccione una opción: "))

        if (opcion == 1):
            os.system('clear')
            agregar_cita(citas_manager)
        elif (opcion == 2):
            os.system('clear')
            buscar_cita(citas_manager)
        elif (opcion == 3):
            os.system('clear')
            modificar_citas(citas_manager)
        elif (opcion == 4):
            os.system('clear')
            cancelar_citas(citas_manager)    
        elif (opcion == 5):
            print("¡Hasta luego!")
            break
        else:
            print("opcion invalida. por favor, selecione una opcion valida.")

if __name__ == "__main__":
    main()

