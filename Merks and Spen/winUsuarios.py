import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Label

class Usuario:
    def __init__(self, id_usuario, username, password, nombre_completo, correo, id_rol, id_departamento):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.id_rol = id_rol
        self.id_departamento = id_departamento

class Rol:
    def __init__(self, id_rol, nombre, descripcion):
        self.id_rol = id_rol
        self.nombre = nombre
        self.descripcion = descripcion

class Departamento:
    def __init__(self, id_departamento, nombre, descripcion):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.descripcion = descripcion

class AdministradorUsuariosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Usuarios")
        Label(root, text="Registro de Usuarios", font=("Helvetica", 15)).pack()

        self.roles = [Rol(1, "Admin", "Administrador del sistema"), Rol(2, "Usuario", "Usuario normal")]
        self.departamentos = [Departamento(1, "Almacen", "Departamento de almacen"), 
                                Departamento(2, "Compras", "Departamento de compras"),
                                Departamento(3, "Produccion", "Departamento de produccion"),
                                Departamento(4, "Logistica", "Departamento de Logistica"),
                                Departamento(5, "Recursos Humanos", "Departamento de recursos humanos")]

        self.usuarios = [] 

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_username = tk.Label(self.frame, text="Nombre de usuario:")
        self.label_username.grid(row=0, column=0, sticky="e")
        self.entry_username = tk.Entry(self.frame)
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(self.frame, text="Contraseña:")
        self.label_password.grid(row=1, column=0, sticky="e")
        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=1)

        self.label_nombre = tk.Label(self.frame, text="Nombre completo:")
        self.label_nombre.grid(row=2, column=0, sticky="e")
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=2, column=1)

        self.label_correo = tk.Label(self.frame, text="Correo electrónico:")
        self.label_correo.grid(row=3, column=0, sticky="e")
        self.entry_correo = tk.Entry(self.frame)
        self.entry_correo.grid(row=3, column=1)

        self.label_rol = tk.Label(self.frame, text="Rol:")
        self.label_rol.grid(row=4, column=0, sticky="e")
        self.combobox_rol = ttk.Combobox(self.frame, values=[rol.nombre for rol in self.roles])
        self.combobox_rol.grid(row=4, column=1)

        self.label_departamento = tk.Label(self.frame, text="Departamento:")
        self.label_departamento.grid(row=5, column=0, sticky="e")
        self.combobox_departamento = ttk.Combobox(self.frame, values=[departamento.nombre for departamento in self.departamentos])
        self.combobox_departamento.grid(row=5, column=1)

        self.button_agregar = tk.Button(self.frame, text="Agregar Usuario", command=self.agregar_usuario)
        self.button_agregar.grid(row=6, columnspan=2, pady=10)

        self.button_editar = tk.Button(self.frame, text="Editar Usuario", command=self.editar_usuario)
        self.button_editar.grid(row=7, columnspan=2, pady=10)

        self.button_eliminar = tk.Button(self.frame, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.button_eliminar.grid(row=8, columnspan=2, pady=10)

        self.lista_usuarios = tk.Listbox(self.root, width=50)
        self.lista_usuarios.pack(pady=20)

        self.mostrar_usuarios()

    def agregar_usuario(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        rol_index = self.combobox_rol.current()
        departamento_index = self.combobox_departamento.current()

        if username and password and nombre and correo and rol_index != -1 and departamento_index != -1:
            rol_id = self.roles[rol_index].id_rol
            departamento_id = self.departamentos[departamento_index].id_departamento

            nuevo_usuario = Usuario(len(self.usuarios) + 1, username, password, nombre, correo, rol_id, departamento_id)
            self.usuarios.append(nuevo_usuario)
            self.mostrar_usuarios()
            self.limpiar_campos()
            messagebox.showinfo("Usuario Agregado", "Usuario agregado con éxito.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def editar_usuario(self):
        seleccionado = self.lista_usuarios.curselection()
        if seleccionado:
            index = seleccionado[0]
            usuario = self.usuarios[index]

            username = self.entry_username.get()
            password = self.entry_password.get()
            nombre = self.entry_nombre.get()
            correo = self.entry_correo.get()
            rol_index = self.combobox_rol.current()
            departamento_index = self.combobox_departamento.current()

            if username and password and nombre and correo and rol_index != -1 and departamento_index != -1:
                rol_id = self.roles[rol_index].id_rol
                departamento_id = self.departamentos[departamento_index].id_departamento

                usuario.username = username
                usuario.password = password
                usuario.nombre_completo = nombre
                usuario.correo = correo
                usuario.id_rol = rol_id
                usuario.id_departamento = departamento_id

                self.mostrar_usuarios()
                self.limpiar_campos()
                messagebox.showinfo("Usuario Editado", "Usuario editado con éxito.")
            else:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
        else:
            messagebox.showerror("Error", "Por favor seleccione un usuario.")

    def eliminar_usuario(self):
        seleccionado = self.lista_usuarios.curselection()
        if seleccionado:
            index = seleccionado[0]
            self.usuarios.pop(index)
            self.mostrar_usuarios()
            self.limpiar_campos()
            messagebox.showinfo("Usuario Eliminado", "Usuario eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Por favor seleccione un usuario.")

    def mostrar_usuarios(self):
        self.lista_usuarios.delete(0, tk.END)
        for usuario in self.usuarios:
            rol_nombre = next((rol.nombre for rol in self.roles if rol.id_rol == usuario.id_rol), "Desconocido")
            departamento_nombre = next((departamento.nombre for departamento in self.departamentos if departamento.id_departamento == usuario.id_departamento), "Desconocido")
            self.lista_usuarios.insert(tk.END, f"{usuario.nombre_completo} - {usuario.username} - Rol: {rol_nombre} - Departamento: {departamento_nombre}")

    def limpiar_campos(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.combobox_rol.set('')
        self.combobox_departamento.set('')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = AdministradorUsuariosApp(root)
    root.mainloop()