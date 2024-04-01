class Inventario:
    def __init__(self):
        self.inventario = {}

    def registrar_entrada(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

        return f"Entrada registrada: {cantidad} unidades de {producto}"

    def registrar_salida(self, producto, cantidad):
        if producto in self.inventario and self.inventario[producto] >= cantidad:
            self.inventario[producto] -= cantidad
            return f"Salida registrada: {cantidad} unidades de {producto}"
        else:
            return "Error: Cantidad insuficiente en inventario"

    def mostrar_inventario(self):
        inventario_str = "\n".join([f"{producto}: {cantidad}" for producto, cantidad in self.inventario.items()])
        return f"Inventario Actual:\n{inventario_str}"
