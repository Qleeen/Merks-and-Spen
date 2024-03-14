import tkinter as tk
from tkinter import ttk, messagebox, Label

class ReportesPDFApp:
    def __init__(self, root, inventario):
        self.root = root
        self.root.title("Generar Reportes PDF")
        Label(root, text="Generar Reportes PDF", font=("Helvetica", 15)).pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.inventario = inventario

        self.label_articulos = tk.Label(self.frame, text="Artículos del inventario:")
        self.label_articulos.grid(row=0, column=0, sticky="e")
        self.texto_articulos = tk.Text(self.frame, width=50, height=10)
        self.texto_articulos.grid(row=0, column=1, padx=5, pady=5)

        self.label_pedidos_departamento = tk.Label(self.frame, text="Pedidos por departamento:")
        self.label_pedidos_departamento.grid(row=1, column=0, sticky="e")
        self.texto_pedidos_departamento = tk.Text(self.frame, width=50, height=10)
        self.texto_pedidos_departamento.grid(row=1, column=1, padx=5, pady=5)

        self.label_pedidos_fechas = tk.Label(self.frame, text="Pedidos por fechas:")
        self.label_pedidos_fechas.grid(row=2, column=0, sticky="e")
        self.texto_pedidos_fechas = tk.Text(self.frame, width=50, height=10)
        self.texto_pedidos_fechas.grid(row=2, column=1, padx=5, pady=5)

        self.button_descargar_pdf = tk.Button(self.frame, text="Descargar PDF", command=self.descargar_pdf)
        self.button_descargar_pdf.grid(row=3, columnspan=2, pady=10)

        self.cargar_datos()

    def cargar_datos(self):
        articulos = self.inventario.obtener_articulos()
        self.texto_articulos.insert(tk.END, "Nombre\tCategoría\tPrecio\tStock\n")
        for articulo in articulos:
            self.texto_articulos.insert(tk.END, f"{articulo['nombre']}\t{articulo['categoria']}\t{articulo['precio']}\t{articulo['stock']}\n")


        self.texto_pedidos_departamento.insert(tk.END, "No hay pedidos por departamento disponibles.")
        self.texto_pedidos_fechas.insert(tk.END, "No hay pedidos por fechas disponibles.")

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Módulo de Inventario")
        Label(root, text="Administrador Inventario", font=("Helvetica", 15)).pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_categoria = tk.Label(self.frame, text="Categoría:")
        self.label_categoria.grid(row=0, column=0, sticky="e")
        self.combobox_categoria = ttk.Combobox(self.frame, values=["Muebles de Oficina", "Suministros", "Equipos Electrónicos", "Material de Oficina", "Organizadores", "Electrodomésticos", "Materiales de Presentación", "Suministros de Limpieza", "Ergonómicos", "Artículos de Decoración"])
        self.combobox_categoria.grid(row=0, column=1, padx=5, pady=5)

        self.button_inicio = tk.Button(self.frame, text="Inicio", command=self.ir_a_inicio)
        self.button_inicio.grid(row=0, column=2, padx=5, pady=5)

        self.label_ordenar_por = tk.Label(self.frame, text="Ordenar por:")
        self.label_ordenar_por.grid(row=0, column=3, sticky="e")
        self.combobox_ordenar_por = ttk.Combobox(self.frame, values=["Nombre", "Precio", "Stock"])
        self.combobox_ordenar_por.grid(row=0, column=4, padx=5, pady=5)

        self.lista_articulos = tk.Listbox(self.frame, width=50, height=10)
        self.lista_articulos.grid(row=1, columnspan=5, pady=10)

        self.imagenes = {}

        self.cargar_articulos() 

        self.button_consultar = tk.Button(self.frame, text="Consultar", command=self.consultar)
        self.button_consultar.grid(row=2, column=0, padx=5, pady=5)

        self.button_graficas = tk.Button(self.frame, text="Gráficas", command=self.graficas)
        self.button_graficas.grid(row=2, column=1, padx=5, pady=5)

        self.button_reportes_pdf = tk.Button(self.frame, text="Reportes PDF", command=self.abrir_reportes_pdf)
        self.button_reportes_pdf.grid(row=2, column=2, padx=5, pady=5)

    def cargar_articulos(self):
        articulos = [
            {"nombre": "Silla de Oficina", "categoria": "Muebles de Oficina", "precio": "$100", "stock": 10, "imagen": "silla_oficina.jpg"},
            {"nombre": "Impresora Multifunción", "categoria": "Equipos Electrónicos", "precio": "$200", "stock": 5, "imagen": "impresora.jpg"},
            {"nombre": "Libreta", "categoria": "Material de Oficina", "precio": "$5", "stock": 50, "imagen": "libreta.jpg"},
            {"nombre": "Organizador de Escritorio", "categoria": "Organizadores", "precio": "$15", "stock": 20, "imagen": "organizador.jpg"},
        ]

        for articulo in articulos:
            self.lista_articulos.insert(tk.END, articulo["nombre"])
            fileImagen = articulo["imagen"]
            self.imagenes[articulo["nombre"]] = fileImagen 

        self.lista_articulos.bind("<Double-Button-1>", self.mostrar_detalle)

    def mostrar_detalle(self, event):
        seleccionado = self.lista_articulos.curselection()
        if seleccionado:
            index = seleccionado[0]
            nombre_articulo = self.lista_articulos.get(index)
            

            imagen = self.imagenes.get(nombre_articulo)
            if imagen:
                ventana_detalle = tk.Toplevel(self.root)
                ventana_detalle.title("Detalle del Artículo")
                label_nombre = tk.Label(ventana_detalle, text=nombre_articulo)
                label_nombre.pack()

            else:
                messagebox.showerror("Error", "No se encontró la imagen del artículo.")

    def ir_a_inicio(self):
        self.lista_articulos.selection_clear(0, tk.END)

    def consultar(self):
        messagebox.showinfo("Consultar", "Falta funcionalidad")

    def graficas(self):
        messagebox.showinfo("Gráficas", "Falta funcionalidad")

    def abrir_reportes_pdf(self):

        reportes_pdf_window = tk.Toplevel(self.root)
        reportes_pdf_app = ReportesPDFApp(reportes_pdf_window, self)

    def obtener_articulos(self):

        articulos = [
            {"nombre": "Silla de Oficina", "categoria": "Muebles de Oficina", "precio": "$100", "stock": 10},
            {"nombre": "Impresora Multifunción", "categoria": "Equipos Electrónicos", "precio": "$200", "stock": 5},
            {"nombre": "Libreta", "categoria": "Material de Oficina", "precio": "$5", "stock": 50},
            {"nombre": "Organizador de Escritorio", "categoria": "Organizadores", "precio": "$15", "stock": 20},
        ]
        return articulos

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()