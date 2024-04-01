import tkinter as tk
from tkinter import ttk, messagebox, Label
from claseStatus import AppAdmin

class AppAdminGUI(tk.Tk):
    def __init__(self, solicitudes):
        super().__init__()

        self.title("Aplicación de Almacén - Perfil Admin")
        self.geometry("600x400")
        Label(text="Pedidos Solicitados", font=("Helvetica", 15)).pack()

        self.app_admin = AppAdmin(solicitudes)

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=20, pady=20)

        self.lista_solicitudes = ttk.Treeview(self.frame, columns=("Fecha", "Usuario", "Producto", "Cantidad", "Estado"), show="headings")
        self.lista_solicitudes.heading("Fecha", text="Fecha")
        self.lista_solicitudes.heading("Usuario", text="Usuario")
        self.lista_solicitudes.heading("Producto", text="Producto")
        self.lista_solicitudes.heading("Cantidad", text="Cantidad")
        self.lista_solicitudes.heading("Estado", text="Estado")
        self.lista_solicitudes.pack(padx=20, pady=20)

        self.button_notificar = ttk.Button(self.frame, text="Notificar Estado", command=self.app_admin.notificar_estado)
        self.button_notificar.pack(padx=5, pady=5)

        self.app_admin.actualizar_lista_solicitudes()

if __name__ == "__main__":
    solicitudes = []  # Replace [] with your actual list of solicitudes
    app_admin_gui = AppAdminGUI(solicitudes)
    app_admin_gui.mainloop()
