import tkinter as tk
from tkinter import messagebox, Label

class Articulo:
    def __init__(self, id_articulo, nombre, marca, precio, categoria):
        self.id_articulo = id_articulo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.categoria = categoria

class AdministradorArticulosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Artículos")
        
        Label(root, text="Administrador de Articulos", font=("Helvetica", 15)).pack()
        
        self.articulos = []  # Lista que simula una base de datos (solo ejemplo para demostrar posible funcionalidad)

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_nombre = tk.Label(self.frame, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, sticky="e")
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        self.label_marca = tk.Label(self.frame, text="Marca:")
        self.label_marca.grid(row=1, column=0, sticky="e")
        self.entry_marca = tk.Entry(self.frame)
        self.entry_marca.grid(row=1, column=1)

        self.label_precio = tk.Label(self.frame, text="Precio:")
        self.label_precio.grid(row=2, column=0, sticky="e")
        self.entry_precio = tk.Entry(self.frame)
        self.entry_precio.grid(row=2, column=1)

        self.label_categoria = tk.Label(self.frame, text="Categoría:")
        self.label_categoria.grid(row=3, column=0, sticky="e")
        self.entry_categoria = tk.Entry(self.frame)
        self.entry_categoria.grid(row=3, column=1)

        self.button_agregar = tk.Button(self.frame, text="Agregar Artículo", command=self.agregar_articulo)
        self.button_agregar.grid(row=4, columnspan=2, pady=10)

        self.button_editar = tk.Button(self.frame, text="Editar Artículo", command=self.editar_articulo)
        self.button_editar.grid(row=5, columnspan=2, pady=10)

        self.button_eliminar = tk.Button(self.frame, text="Salida articulo", command=self.eliminar_articulo)
        self.button_eliminar.grid(row=6, columnspan=2, pady=10)

        self.lista_articulos = tk.Listbox(self.root, width=50)
        self.lista_articulos.pack(pady=20)

        self.mostrar_articulos()

    def agregar_articulo(self):
        nombre = self.entry_nombre.get()
        marca = self.entry_marca.get()
        precio = self.entry_precio.get()
        categoria = self.entry_categoria.get()

        if nombre and marca and precio and categoria:
            nuevo_articulo = Articulo(len(self.articulos) + 1, nombre, marca, precio, categoria)
            self.articulos.append(nuevo_articulo)
            self.mostrar_articulos()
            self.limpiar_campos()
            messagebox.showinfo("Artículo Agregado", "Artículo agregado con éxito.")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def editar_articulo(self):
        seleccionado = self.lista_articulos.curselection()
        if seleccionado:
            index = seleccionado[0]
            articulo = self.articulos[index]

            nombre = self.entry_nombre.get()
            marca = self.entry_marca.get()
            precio = self.entry_precio.get()
            categoria = self.entry_categoria.get()

            if nombre and marca and precio and categoria:
                articulo.nombre = nombre
                articulo.marca = marca
                articulo.precio = precio
                articulo.categoria = categoria

                self.mostrar_articulos()
                self.limpiar_campos()
                messagebox.showinfo("Artículo Editado", "Artículo editado con éxito.")
            else:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
        else:
            messagebox.showerror("Error", "Por favor seleccione un artículo.")

    def eliminar_articulo(self):
        seleccionado = self.lista_articulos.curselection()
        if seleccionado:
            index = seleccionado[0]
            self.articulos.pop(index)
            self.mostrar_articulos()
            self.limpiar_campos()
            messagebox.showinfo("Artículo Eliminado", "Artículo eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Por favor seleccione un artículo.")

    def mostrar_articulos(self):
        self.lista_articulos.delete(0, tk.END)
        for articulo in self.articulos:
            self.lista_articulos.insert(tk.END, f"{articulo.nombre} - Marca: {articulo.marca} - Precio: {articulo.precio} - Categoría: {articulo.categoria}")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("500x500")
    app = AdministradorArticulosApp(ventana)
    ventana.mainloop()
