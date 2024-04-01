from tkinter import messagebox

class ControlAccesoApp:
    def __init__(self):
        pass

    def verificar_acceso(self, usuario, password):
        if usuario == "compras" and password == "admin":
            return True
        else:
            return False

    def abrir_ventana_principal(self):
        # Aquí iría el código para abrir la ventana principal
        pass

    def admin_usuarios(self):
        messagebox.showinfo("Admin Usuarios", "Funcionalidad de Administración de Usuarios")

    def admin_articulos(self):
        messagebox.showinfo("Admin Articulos", "Funcionalidad de Administración de Articulos")

    def inventario(self):
        messagebox.showinfo("Inventario", "Funcionalidad de Inventario")

    def solicitudes(self):
        messagebox.showinfo("Solicitudes", "Funcionalidad de Solicitudes")
