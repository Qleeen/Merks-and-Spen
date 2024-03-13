import tkinter as tk
from tkinter import Label

class InventarioApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de inventario")
        Label(root, text="Registro de nuevos articulos", font=("Helvetica", 15)).pack()

        self.inventario = {}

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

        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

        self.mostrar_resultado(f"Entrada registrada: {cantidad} unidades de {producto}")

    def registrar_salida(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())

        if producto in self.inventario and self.inventario[producto] >= cantidad:
            self.inventario[producto] -= cantidad
            self.mostrar_resultado(f"Salida registrada: {cantidad} unidades de {producto}")
        else:
            self.mostrar_resultado("Error: Cantidad insuficiente en inventario")

    def mostrar_inventario(self):
        inventario_str = "\n".join([f"{producto}: {cantidad}" for producto, cantidad in self.inventario.items()])
        self.mostrar_resultado(f"Inventario Actual:\n{inventario_str}")

    def mostrar_resultado(self, mensaje):
        self.resultado.config(text=mensaje)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    app = InventarioApp(root)
    root.mainloop()
