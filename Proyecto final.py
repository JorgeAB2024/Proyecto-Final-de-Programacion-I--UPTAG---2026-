import getpass



class GestorUsuarios:
    def __init__(self):
        self.usuarios = {"admin": "1234"} 
    def registrar(self, usuario, contrasena):
        if usuario in self.usuarios:
            print(f"El usuario '{usuario}' ya existe.")
        else:
            self.usuarios[usuario] = contrasena
            print("Usuario registrado con éxito.")

    def autenticar(self, usuario, contrasena):
        if usuario in self.usuarios and self.usuarios[usuario] == contrasena:
            return True
        print("Usuario o contraseña incorrectos.")
        return False

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, codigo, nombre, precio, cantidad):
        self.productos[codigo] = f"ID: {codigo} | Nombre: {nombre} | Precio: ${precio} | Stock: {cantidad}"
        print("Producto agregado con éxito.")

    def buscar(self, criterio):
        return [v for k, v in self.productos.items() if criterio in str(k) or criterio in v]

    def borrar(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            print("Producto eliminado.")
        else:
            print("Código no encontrado.")

    def guardar(self):
        print("Datos guardados en la base de datos local.")



def solicitar_solo_numeros(mensaje, permitir_decimal=False):
   
    while True:
        try:
            entrada = input(mensaje).strip()
            valor = float(entrada) if permitir_decimal else int(entrada)
            if valor >= 0:
                return entrada if not permitir_decimal else valor
            print("Error: No se permiten números negativos.")
        except ValueError:
            print("Error: Ingrese un número válido.")



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
