import Task as t

print("Bienvenido Usuario")

TASK_FILE = 'task.json'
tareas = t.cargar_datos(TASK_FILE)

while True:
    try:
        print("\nMenu")
        print("1.Mostrar Tareas")
        print("2.Agregar Tarea")
        print("3.Eliminar Tarea")
        print("4.Completar Tarea")
        print("5. salir\n")

        op = int(input("Elija una opcion: "))
        if not op in [1,2,3,4,5,]:
            print("La opcion elegida esta fuera de rango")
            continue

    except ValueError:
        print("Error: Debes ingresar un número.\n")
        continue
    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo del programa...")
        exit()

    if op == 1:
        t.mostrar_tareas(tareas)
        print()
    elif op == 2:
        t.anadir_tareas(tareas, TASK_FILE)
        print()
    elif op == 3:
        t.eliminar_tareas()
        print()
    elif op == 4:
        print()
    elif op == 5:
        t.guardar_datos(tareas, TASK_FILE)
        print("Saliendo del programa...")
        break