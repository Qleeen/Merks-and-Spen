import tkinter as tk
from tkinter import ttk, messagebox, Label
from claseSoli import usuarios, productos, estados, enviar_solicitud

class AppAlmacen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Almacén")
        self.geometry("600x400")
        Label(text="Solicitud de Articulos", font=("Helvetica", 15)).pack()

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=20, pady=20)

        self.label_usuario = ttk.Label(self.frame, text="Usuario:")
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combobox_usuario = ttk.Combobox(self.frame, values=list(usuarios.values()))
        self.combobox_usuario.grid(row=0, column=1, padx=5, pady=5)

        self.label_producto = ttk.Label(self.frame, text="Producto:")
        self.label_producto.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combobox_producto = ttk.Combobox(self.frame, values=list(productos.values()))
        self.combobox_producto.grid(row=1, column=1, padx=5, pady=5)

        self.label_cantidad = ttk.Label(self.frame, text="Cantidad:")
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = ttk.Entry(self.frame)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        self.button_agregar = ttk.Button(self.frame, text="Agregar", command=self.enviar_solicitud)
        self.button_agregar.grid(row=3, column=0, padx=5, pady=5)

        self.button_enviar = ttk.Button(self.frame, text="Enviar Solicitud", command=self.enviar_solicitud)
        self.button_enviar.grid(row=3, column=1, padx=5, pady=5)

        self.lista_solicitudes = ttk.Treeview(self, columns=("Fecha", "Usuario", "Producto", "Cantidad", "Estado"), show="headings")
        self.lista_solicitudes.heading("Fecha", text="Fecha")
        self.lista_solicitudes.heading("Usuario", text="Usuario")
        self.lista_solicitudes.heading("Producto", text="Producto")
        self.lista_solicitudes.heading("Cantidad", text="Cantidad")
        self.lista_solicitudes.heading("Estado", text="Estado")
        self.lista_solicitudes.pack(padx=20, pady=20)

    def enviar_solicitud(self):
        usuario = self.combobox_usuario.get()
        producto = self.combobox_producto.get()
        cantidad = self.entry_cantidad.get()

        if enviar_solicitud(usuario, producto, cantidad):
            self.actualizar_lista_solicitudes()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def actualizar_lista_solicitudes(self):
        self.lista_solicitudes.delete(*self.lista_solicitudes.get_children())
        for solicitud in solicitudes:
            self.lista_solicitudes.insert("", "end", values=(solicitud["Fecha"], solicitud["Usuario"], solicitud["Producto"], solicitud["Cantidad"], solicitud["Estado"]))

if __name__ == "__main__":
    app = AppAlmacen()
    app.mainloop()
