import datetime

# Simulación de la base de datos
usuarios = {1: "Usuario 1", 2: "Usuario 2", 3: "Usuario 3"}
productos = {1: "Producto 1", 2: "Producto 2", 3: "Producto 3"}
estados = {1: "Pendiente", 2: "Aprobada", 3: "Rechazada"}

solicitudes = []

def enviar_solicitud(usuario, producto, cantidad):
    if not usuario or not producto or not cantidad:
        return False

    solicitud = {
        "Fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Usuario": usuario,
        "Producto": producto,
        "Cantidad": cantidad,
        "Estado": "Pendiente"
    }

    solicitudes.append(solicitud)
    return True
