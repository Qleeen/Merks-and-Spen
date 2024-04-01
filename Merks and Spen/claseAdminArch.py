class Articulo:
    def __init__(self, id_articulo, nombre, marca, precio, categoria):
        self.id_articulo = id_articulo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.categoria = categoria

class AdministradorArticulosApp:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, nombre, marca, precio, categoria):
        if nombre and marca and precio and categoria:
            nuevo_articulo = Articulo(len(self.articulos) + 1, nombre, marca, precio, categoria)
            self.articulos.append(nuevo_articulo)
            return True, "Artículo agregado con éxito."
        else:
            return False, "Por favor complete todos los campos."

    def editar_articulo(self, index, nombre, marca, precio, categoria):
        if nombre and marca and precio and categoria:
            articulo = self.articulos[index]
            articulo.nombre = nombre
            articulo.marca = marca
            articulo.precio = precio
            articulo.categoria = categoria
            return True, "Artículo editado con éxito."
        else:
            return False, "Por favor complete todos los campos."

    def eliminar_articulo(self, index):
        self.articulos.pop(index)
        return "Artículo eliminado con éxito."
