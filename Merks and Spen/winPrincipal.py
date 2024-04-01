import tkinter as tk
from tkinter import Label, Frame, Entry, Button
from tkinter import messagebox
from clasePrin import ControlAccesoApp

class InterfazAcceso:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Acceso")
        
        Label(root, text="Bienvenido \n Merks and Spend", font=("Helvetica", 15)).pack()

        self.frame = Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_usuario = Label(self.frame, text="Departamento:")
        self.label_usuario.grid(row=0, column=0, sticky="e")
        self.entry_usuario = Entry(self.frame)
        self.entry_usuario.grid(row=0, column=1)

        self.label_password = Label(self.frame, text="Contraseña:")
        self.label_password.grid(row=1, column=0, sticky="e")
        self.entry_password = Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=1)

        self.control_acceso = ControlAccesoApp()

        self.button_ingresar = Button(self.frame, text="Ingresar", command=self.verificar_acceso)
        self.button_ingresar.grid(row=2, columnspan=2, pady=10)

    def verificar_acceso(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if self.control_acceso.verificar_acceso(usuario, password):
            self.control_acceso.abrir_ventana_principal()
        else:
            messagebox.showerror("Acceso Denegado", "Usuario o contraseña incorrectos.")

def main():
    root = tk.Tk()
    app = InterfazAcceso(root)
    root.mainloop()

if __name__ == "__main__":
    main()
