import tkinter as tk
from tkinter import ttk, messagebox, Label

class AppAdmin(tk.Tk):
    def __init__(self, solicitudes):
        super().__init__()

        self.title("Aplicación de Almacén - Perfil Admin")
        self.geometry("600x400")
        Label(text="Pedidos Solicitados", font=("Helvetica", 15)).pack()

        self.solicitudes = solicitudes

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=20, pady=20)

        self.lista_solicitudes = ttk.Treeview(self.frame, columns=("Fecha", "Usuario", "Producto", "Cantidad", "Estado"), show="headings")
        self.lista_solicitudes.heading("Fecha", text="Fecha")
        self.lista_solicitudes.heading("Usuario", text="Usuario")
        self.lista_solicitudes.heading("Producto", text="Producto")
        self.lista_solicitudes.heading("Cantidad", text="Cantidad")
        self.lista_solicitudes.heading("Estado", text="Estado")
        self.lista_solicitudes.pack(padx=20, pady=20)

        self.button_notificar = ttk.Button(self.frame, text="Notificar Estado", command=self.notificar_estado)
        self.button_notificar.pack(padx=5, pady=5)

        self.actualizar_lista_solicitudes()

    def actualizar_lista_solicitudes(self):
        self.lista_solicitudes.delete(*self.lista_solicitudes.get_children())
        for solicitud in self.solicitudes:
            self.lista_solicitudes.insert("", "end", values=(solicitud["Fecha"], solicitud["Usuario"], solicitud["Producto"], solicitud["Cantidad"], solicitud["Estado"]))

    def notificar_estado(self):
        selected_item = self.lista_solicitudes.focus()
        if selected_item:
            index = int(selected_item.lstrip('I')) - 1
            solicitud = self.solicitudes[index]
            messagebox.showinfo("Notificación", f"Estado de la solicitud: {solicitud['Estado']}")
        else:
            messagebox.showerror("Error", "Por favor seleccione una solicitud.")

if __name__ == "__main__":
    solicitudes = []  # Replace [] with your actual list of solicitudes
    app_admin = AppAdmin(solicitudes)
    app_admin.mainloop()
    
    

