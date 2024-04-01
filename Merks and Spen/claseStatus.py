class AppAdmin:
    def __init__(self, solicitudes):
        self.solicitudes = solicitudes

    def actualizar_lista_solicitudes(self):
        for solicitud in self.solicitudes:
            print(solicitud)  # Aquí solo un ejemplo de lo que podrías hacer

    def notificar_estado(self):
        selected_item = self.lista_solicitudes.focus()
        if selected_item:
            index = int(selected_item.lstrip('I')) - 1
            solicitud = self.solicitudes[index]
            print(f"Estado de la solicitud: {solicitud['Estado']}")  # Aquí solo un ejemplo de lo que podrías hacer
        else:
            print("Por favor seleccione una solicitud.")  # Aquí solo un ejemplo de lo que podrías hacer
