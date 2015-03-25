__author__ = "Jose Diaz"
__date__ = "25/03/2015 09:49:20 AM"
__email__ = "jozz.18x@gmail.com"

import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class GUI(Frame):

    BACKGROUND = None

    LABEL = dict(fg="black", font=("Adobe Fan Heiti Std B",11))
    ENTRY = dict(width=30, font=("Franklin Gothic Book",11))
    BUTTON = dict(cursor="hand2", width=13, relief=FLAT, bd=0, 
                  font=("Franklin Gothic Book",10), bg="#00887A", 
                  fg="#FFFFFF", activebackground="#333333", activeforeground="#FFFFFF")
    PADDING_ENTRY = dict(side=RIGHT, anchor=E, padx=10)

    @classmethod
    def main(cls):
        """Metodo principal"""
        root = Tk()
        root.title("Login - Prueba de validacion")
        root.geometry("400x160+480+250")
        root.focus_set()
        root.resizable(width=False, height=False)
        vista = cls(root)
        vista.pack(fill=BOTH, expand=True)
        root.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
        root.mainloop()

    def __init__(self, master):
        super().__init__(master)
        """Metodo que inicializa la clase"""
        #Declaracion de variables.
        self.USUARIO = "root"
        self.PASSWORD = "root"
        self.var_usuario = StringVar()
        self.var_password = StringVar()
        #Creamos la interfaz
        self.interfaz = self.crear_interfaz()
        self.interfaz.pack(fill=BOTH, expand=True)
        
    def crear_interfaz(self):
        """Crea e implementa la interfaz y los widgets, retotna el frame."""
        frame = Frame(self)
        frame["background"] = self.BACKGROUND

        frame1 = Frame(frame, bg=frame['bg'])
        frame1.pack(fill=X, pady=10)
        frame2 = Frame(frame, bg=frame['bg'])
        frame2.pack(fill=X, pady=10)

        Label(frame1, text="Usuario: ", bg=frame1['bg'], **self.LABEL).pack(side=LEFT, anchor=W, padx=10)
        self.entryUsuario = ttk.Entry(frame1, textvariable=self.var_usuario, **self.ENTRY)
        self.entryUsuario.focus()
        self.entryUsuario.pack(**self.PADDING_ENTRY)
        Label(frame2, text="Password: ", bg=frame2['bg'], **self.LABEL).pack(side=LEFT, anchor=W, padx=10)
        self.entryPassword = ttk.Entry(frame2, show='*', textvariable=self.var_password, **self.ENTRY)
        self.entryPassword.pack(**self.PADDING_ENTRY)

        self.entryPassword.bind('<Key-Return>', lambda e: self.validacion(self.USUARIO, self.PASSWORD)) #Evento KeyPress para la tecla enter
        
        btn_ingresar = Button(frame, command=lambda: self.validacion(self.USUARIO, self.PASSWORD), text="Ingresar", **self.BUTTON)
        btn_ingresar.pack(side=BOTTOM, anchor='e', padx=10, pady=10)

        return frame

    def validacion(self, usuario, clave):
            """Hace la validacion del usuario ingresado por teclado con el usuario establecido(Base de datos o en este caso asignado).
            REGLA DE NEGOCIO:
            El usuario y el password no deben de tener mas de 10 caracteres.
            Las mayusculas y minusculas deben ser precisos y deben coincidir."""
            user = self.var_usuario.get()
            password = self.var_password.get()
            if user == "":
                messagebox.showinfo(title="Atencion", message="Ingrese Usuario")
            elif password == "":
                messagebox.showinfo(title="Atencion", message="Ingrese password")
            else:
                if len(user) > 10:
                    messagebox.showinfo(title="MENSAJE", message="El Usuario que introdujo tiene mas de 10 caracteres.")
                elif len(password) > 10:
                    messagebox.showinfo(title="MENSAJE", message="El Password que introdujo tiene mas de 10 caracteres.")
                else:
                    if user==usuario and password==clave:
                        messagebox.showinfo(title="MENSAJE", message="Logeo satisfactorio.")
                        # Aqui se implementacion el codigo.
                    else:
                        messagebox.showerror(title="MENSAJE", message="Usuario o password introducido no son validos. \nIngrese otra vez por favor.")
                        # Limpiamos las entradas de texto y colocamos el foco el el usuario.
                        self.var_usuario.set("")
                        self.var_password.set("")
                        self.entryUsuario.focus()

if __name__ == "__main__":
        GUI.main()
