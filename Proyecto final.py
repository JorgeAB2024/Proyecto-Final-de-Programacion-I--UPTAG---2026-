def menu_auth():
    gestor = GestorUsuarios()
    while True:
        print(f"\n{'='*15} SISTEMA DE AUTENTICACIÓN {'='*15}")
        print("1. Iniciar Sesión | 2. Registrarse | 3. Salir")
        opc = input("Seleccione: ").strip()

        if opc == "1":
            print("\n--- INICIAR SESIÓN ---")
            usuario = input("Usuario: ").strip()
            contrasena = getpass.getpass("Contraseña: ").strip()
            if gestor.autenticar(usuario, contrasena):
                print(f"\n¡Bienvenido/a, {usuario}!")
                menu(usuario)
        elif opc == "2":
            print("\n--- REGISTRO DE USUARIO ---")
            nuevo_usuario = input("Nuevo usuario: ").strip()
            nueva_contrasena = getpass.getpass("Nueva contraseña: ").strip()
            contrasena_confirmacion = getpass.getpass("Confirmar contraseña: ").strip()
            if nueva_contrasena == contrasena_confirmacion:
                gestor.registrar(nuevo_usuario, nueva_contrasena)
            else:
                print("Las contraseñas no coinciden.")
        elif opc == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

def menu(usuario_actual):
    inv = Inventario()
    while True:
        print(f"\n{'='*15} GESTIÓN NUMÉRICA - Usuario: {usuario_actual} {'='*15}")
        print("1. Agregar | 2. Ver Todo | 3. Buscar | 4. Borrar | 5. Salir")
        opc = input("Seleccione: ")

        if opc == "1":
            codigo = solicitar_solo_numeros("Código (solo números): ")
            nombre = input("Nombre del producto: ")
            precio = solicitar_solo_numeros("Precio: ", permitir_decimal=True)
            cantidad = solicitar_solo_numeros("Cantidad (Stock): ")
            inv.agregar(codigo, nombre, precio, cantidad)
        elif opc == "2":
            print("\n" + "="*50)
            if not inv.productos: 
                print("Inventario vacío.")
            else:
                for producto in inv.productos.values(): print(producto)
            print("="*50)
        elif opc == "3":
            busqueda = input("Ingrese el código o nombre a buscar: ")
            resultados = inv.buscar(busqueda)
            print("\n" + "-"*20 + " RESULTADOS " + "-"*20)
            if resultados:
                for resultado in resultados: print(resultado)
            else:
                print("No se encontraron coincidencias.")
            print("-"*52)
        elif opc == "4":
            codigo_borrar = solicitar_solo_numeros("Ingrese el código numérico a borrar: ")
            inv.borrar(codigo_borrar)
        elif opc == "5":
            inv.guardar()
            print("Cambios guardados. Saliendo...")
            break

if __name__ == "__main__":
    menu_auth()