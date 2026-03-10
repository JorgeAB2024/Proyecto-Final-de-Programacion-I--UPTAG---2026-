import os
import hashlib
import getpass 

class Usuario:
    def __init__(self, nombre_usuario, contrasena_encriptada):
        self.nombre_usuario = nombre_usuario
        self.contrasena_encriptada = contrasena_encriptada

    def a_csv(self):
        return f"{self.nombre_usuario},{self.contrasena_encriptada}\n"

class GestorUsuarios:
    def __init__(self, archivo="usuarios_pro.txt"):
        self.archivo = archivo
        self.usuarios = {}
        self._cargar_datos()

    def _encriptar_contrasena(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def _cargar_datos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    for linea in f:
                        parts = linea.strip().split(",")
                        if len(parts) == 2:
                            usuario, contrasena = parts
                            self.usuarios[usuario] = Usuario(usuario, contrasena)
            except: pass

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            f.writelines(usuario.a_csv() for usuario in self.usuarios.values())

    def registrar(self, nombre_usuario, contrasena):
        if nombre_usuario in self.usuarios:
            print(f"El usuario '{nombre_usuario}' ya existe.")
            return False
        if not nombre_usuario.strip() or not contrasena.strip():
            print("Usuario y contraseña no pueden estar vacíos.")
            return False
            
        contrasena_encriptada = self._encriptar_contrasena(contrasena)
        self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena_encriptada)
        self.guardar()
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")
        return True

    def autenticar(self, nombre_usuario, contrasena):
        if nombre_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return False
            
        usuario = self.usuarios[nombre_usuario]
        if usuario.contrasena_encriptada == self._encriptar_contrasena(contrasena):
            return True
        else:
            print("Contraseña incorrecta.")
            return False

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
