import tkinter as tk
from tkinter import messagebox, Label

class ControlAccesoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Acceso")
        
        Label(root, text="Bienvenido \n Merks and Spend", font=("Helvetica", 15)).pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_usuario = tk.Label(self.frame, text="Departamento:")
        self.label_usuario.grid(row=0, column=0, sticky="e")
        self.entry_usuario = tk.Entry(self.frame)
        self.entry_usuario.grid(row=0, column=1)

        self.label_password = tk.Label(self.frame, text="Contraseña:")
        self.label_password.grid(row=1, column=0, sticky="e")
        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=1)

        self.button_ingresar = tk.Button(self.frame, text="Ingresar", command=self.verificar_acceso)
        self.button_ingresar.grid(row=2, columnspan=2, pady=10)

    def verificar_acceso(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if usuario == "compras" and password == "admin":
            self.abrir_ventana_principal()
        else:
            messagebox.showerror("Acceso Denegado", "Usuario o contraseña incorrectos.")

    def abrir_ventana_principal(self):
        self.root.destroy()  # Cierra la ventana de control de acceso
        ventana_principal = tk.Tk()
        app_principal = VentanaPrincipalApp(ventana_principal)
        ventana_principal.mainloop()


class VentanaPrincipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MERKS AND SPEND")
        self.root.geometry("600x400")

        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(side="top", fill="x")

        self.button_admin_usuarios = tk.Button(self.toolbar, text="Admin Usuarios", command=self.admin_usuarios)
        self.button_admin_usuarios.pack(side="left", padx=5, pady=5)

        self.button_admin_articulos = tk.Button(self.toolbar, text="Admin Articulos", command=self.admin_articulos)
        self.button_admin_articulos.pack(side="left", padx=5, pady=5)

        self.button_inventario = tk.Button(self.toolbar, text="Inventario", command=self.inventario)
        self.button_inventario.pack(side="left", padx=5, pady=5)

        self.button_solicitudes = tk.Button(self.toolbar, text="Solicitudes", command=self.solicitudes)
        self.button_solicitudes.pack(side="left", padx=5, pady=5)

    def admin_usuarios(self):
        messagebox.showinfo("Admin Usuarios", "Funcionalidad de Administración de Usuarios")

    def admin_articulos(self):
        messagebox.showinfo("Admin Articulos", "Funcionalidad de Administración de Articulos")

    def inventario(self):
        messagebox.showinfo("Inventario", "Funcionalidad de Inventario")

    def solicitudes(self):
        messagebox.showinfo("Solicitudes", "Funcionalidad de Solicitudes")




if __name__ == "__main__":
    root = tk.Tk('600x400')
    app = ControlAccesoApp(root)
    root.mainloop()
