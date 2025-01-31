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

def eliminar_tareas():
    print()

def completar_tarea():
    print()

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