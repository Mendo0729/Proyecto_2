import json
from datetime import datetime

task = {}
#TASK_FILE = 'task.json'

"""
ESTRUCTURA DEL DICCIONARIO DE DATOS

task = id{
            tarea: ("nombre de la tarea"),
            fecha: ("fecha que se agrego la tarea")
            estado: ['en_proceso', 'pausada', 'completada']}
"""


def mostrar_tareas(Tareas):
    if not Tareas:
        print(f"{'ID':<5} {'TAREA':<40} {'FECHA':<20} {'ESTADO':<15}")
        print("-" * 80)
        print("\nNo hay Tareas Registradas\n")
        return

    # Encabezado
    print(f"{'ID':<5} {'TAREA':<40} {'FECHA':<20} {'ESTADO':<15}")
    print("-" * 80)

    # Mostrar tareas
    for id, tarea_datos in Tareas.items():
        print(f"{id:<5} {tarea_datos['tarea']:<40} {tarea_datos['fecha']:<20} {tarea_datos['estado']:<15}")

    print()  # Espacio adicional después de la lista

def anadir_tareas(Tareas, TASK_FILE):
    if Tareas is None:
        Tareas = {}

    while True:
        tarea = input("Ingresa el nombre de la tarea: ")
        if not tarea:
            print("El campo no puede estar vacío")
            continue

        fecha_formateada = datetime.now()
        fecha = fecha_formateada.strftime("%d-%m-%Y %H:%M:%S")

        estado = 'en_proceso'

        # Obtener el último ID, si existen tareas, si no, comenzamos con el ID 1
        ultimo_id = max([int(id) for id in Tareas.keys()], default=0)
        nuevo_id = ultimo_id + 1

        # Agregar la tarea al diccionario Tareas
        Tareas[nuevo_id] = {
            "tarea": tarea,
            "fecha": fecha,
            "estado": estado
        }

        # Guardar las tareas en el archivo
        guardar_datos(Tareas, TASK_FILE)
        print("Tarea guardada exitosamente")
        break

def eliminar_tareas(Tareas, TASK_FILE):
    lista_id = []

    mostrar_tareas(Tareas)

    # Mostrar tareas en proceso y guardar los IDs
    for id, tarea_datos in Tareas.items():
        lista_id.append(id)  # Guardamos todos los IDs
        print(f"{id:<5} {tarea_datos['tarea']:<40} {tarea_datos['fecha']:<20} {tarea_datos['estado']:<15}")

    if not lista_id:
        print("No hay tareas en proceso para eliminar.")
        return

    # Bucle para seleccionar tarea a eliminar
    while True:
        try:
            op = input(f"\n¿Cual tarea quieres eliminar? ({lista_id}) o 'salir' para salir de la funcion: ").strip().lower()

            if op == 'salir':  # Si el usuario quiere salir de la función
                print("Saliendo de la función...")
                break

            if op not in lista_id:
                print("La opción elegida está fuera de rango.")
                continue

            # Confirmación para eliminar la tarea seleccionada
            for id, tarea_datos in Tareas.items():
                if str(id) == op:
                    confirmacion = input(f"¿Estás seguro de que deseas eliminar la tarea '{tarea_datos['tarea']}'? (si/no): ").strip().lower()
                    if confirmacion == 'si':
                        del Tareas[op]  # Eliminar tarea
                        guardar_datos(Tareas, TASK_FILE)  # Guardar los cambios
                        print(f"Tarea '{tarea_datos['tarea']}' eliminada con éxito.")
                    break  # Salir del bucle después de eliminar la tarea

            break  # Salir del bucle después de completar la eliminación

        except ValueError:
            print("Error: Debes ingresar una opción válida.\n")
            continue
        except KeyboardInterrupt:
            print("\nProceso interrumpido. Saliendo del programa...")
            exit()

def completar_tarea(Tareas, TASK_FILE):
    lista_id = []
    mostrar_tareas(Tareas)
    # Mostrar tareas
    for id, tarea_datos in Tareas.items():
        if tarea_datos['estado'] == "en_proceso":
            lista_id.append(id)

        print(f"{id:<5} {tarea_datos['tarea']:<40} {tarea_datos['fecha']:<20} {tarea_datos['estado']:<15}")

    #print(lista_id)

    while True:
        try:
            op = input(f"\nCual tarea quieres completar({lista_id}) o 'salir' para salir del la funcion: ").strip().lower()
            if op == 'salir':
                print("Saliendo de la función...")
                break

            if not op in lista_id:
                print("La opcion elegida esta fuera de rango")
                continue

            for id, tarea_datos in Tareas.items():
                if str(id) == op:
                    tarea_datos['estado'] = "completada"
                    guardar_datos(Tareas, TASK_FILE)
                    print(f"Tarea con ID {id} completada.")
                    break

        except ValueError:
            print("Error: Debes ingresar una opcion valida.\n")
            continue
        except KeyboardInterrupt:
            print("\nProceso interrumpido. Saliendo del programa...")
            exit()

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read().strip()
            return json.loads(contenido) if contenido else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def guardar_datos(data, archivo):
    with open(archivo, 'w') as file:
        json.dump(data, file, indent=4)
    print()