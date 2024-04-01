import tkinter as tk
from tkinter import Label
from claseRegistroInv import Inventario

class InventarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de inventario")
        Label(root, text="Registro de nuevos articulos", font=("Helvetica", 15)).pack()

        self.inventario = Inventario()

        self.etiqueta_producto = tk.Label(master, text="Producto:")
        self.etiqueta_producto.pack(pady=5)

        self.entry_producto = tk.Entry(master)
        self.entry_producto.pack(pady=5)

        self.etiqueta_cantidad = tk.Label(master, text="Cantidad:")
        self.etiqueta_cantidad.pack(pady=5)

        self.entry_cantidad = tk.Entry(master)
        self.entry_cantidad.pack(pady=5)

        self.boton_entrada = tk.Button(master, text="Registrar Entrada", command=self.registrar_entrada)
        self.boton_entrada.pack(pady=5)

        self.boton_salida = tk.Button(master, text="Registrar Salida", command=self.registrar_salida)
        self.boton_salida.pack(pady=5)

        self.boton_mostrar = tk.Button(master, text="Mostrar Inventario", command=self.mostrar_inventario)
        self.boton_mostrar.pack(pady=10)

        self.resultado = tk.Label(master, text="")
        self.resultado.pack(pady=5)

    def registrar_entrada(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())
        mensaje = self.inventario.registrar_entrada(producto, cantidad)
        self.mostrar_resultado(mensaje)

    def registrar_salida(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())
        mensaje = self.inventario.registrar_salida(producto, cantidad)
        self.mostrar_resultado(mensaje)

    def mostrar_inventario(self):
        mensaje = self.inventario.mostrar_inventario()
        self.mostrar_resultado(mensaje)

    def mostrar_resultado(self, mensaje):
        self.resultado.config(text=mensaje)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    app = InventarioApp(root)
    root.mainloop()
