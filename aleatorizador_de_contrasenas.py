import random
ids = []
cuentas = []
usuarios = []
contrasenas = []
niveles = []
fechas = []
observaciones = []
#-------------------------------------------------#
#--|menu_principal_aleatorizador_de_contraseñas|--#
#-------------------------------------------------#
while True:
    print("menu principal aleatorizador de contraseñas")
    print("1) crear contraseña")
    print("2) editar contraseña")
    print("3) eliminar contraseña")
    print("4) buscar contraseña")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------------#
    #--|crear_contrasena|--#
    #----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_contrasena = 1
        else:
            id_contrasena = ids[-1] + 1
        cuenta = input("nombre de la cuenta: ")
        usuario = input("usuario: ")
        contrasena = input("contraseña: ")
        nivel = input("nivel de seguridad: ")
        fecha = input("fecha: ")
        observacion = input("observación: ")
        ids.append(id_contrasena)
        cuentas.append(cuenta)
        usuarios.append(usuario)
        contrasenas.append(contrasena)
        niveles.append(nivel)
        fechas.append(fecha)
        observaciones.append(observacion)
        print("contraseña registrada correctamente.")
        print("id:", id_contrasena)
    #-----------------------#
    #--|editar_contrasena|--#
    #-----------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar contraseña")
            for i in range(len(ids)):
                print(f"{ids[i]} | {cuentas[i]} | {usuarios[i]} | {contrasenas[i]} | {niveles[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {cuentas[posicion]} | {usuarios[posicion]} | {contrasenas[posicion]} | {niveles[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                cuentas[posicion] = input("nuevo nombre de la cuenta: ")
                usuarios[posicion] = input("nuevo usuario: ")
                contrasenas[posicion] = input("nueva contraseña: ")
                niveles[posicion] = input("nuevo nivel de seguridad: ")
                fechas[posicion] = input("nueva fecha: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------------#
    #--|eliminar_contrasena|--#
    #-------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar contraseña")
            for i in range(len(ids)):
                print(f"{ids[i]} | {cuentas[i]} | {usuarios[i]} | {contrasenas[i]} | {niveles[i]} | {fechas[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {cuentas[posicion]} | {usuarios[posicion]} | {contrasenas[posicion]} | {niveles[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    cuentas.pop(posicion)
                    usuarios.pop(posicion)
                    contrasenas.pop(posicion)
                    niveles.pop(posicion)
                    fechas.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|buscar_contrasena|--#
    #-----------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar contraseña")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {cuentas[posicion]} | {usuarios[posicion]} | {contrasenas[posicion]} | {niveles[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {cuentas[i]} | {usuarios[i]} | {contrasenas[i]} | {niveles[i]} | {fechas[i]} | {observaciones[i]}")
            print("estadísticas aleatorizador de contraseñas")
            print("cantidad de contraseñas:", len(ids))
            print("cuentas registradas:", len(cuentas))
            print("primera cuenta registrada:", cuentas[0])
            print("última cuenta registrada:", cuentas[-1])
            posicion = random.randint(0, len(ids) - 1)
            print()
            print("contraseña seleccionada aleatoriamente")
            print(f"{ids[posicion]} | {cuentas[posicion]} | {usuarios[posicion]} | {contrasenas[posicion]} | {niveles[posicion]} | {fechas[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de contraseñas.")
        break
    else:
        print("opción no válida.")