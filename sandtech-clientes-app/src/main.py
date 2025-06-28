# sandtech-clientes-app/src/main.py

import tkinter as tk
from gui.clientes_menu import ClientesMenu

def main():

    """
    Inicializa la aplicación de escritorio para 
    la gestión de clientes.

    Configura la ventana principal con título, tamaño y 
    color de fondo, y la coloca en el centro de la pantalla.
    Luego, crea una instancia de la clase ClientesMenu y
    comienza el bucle de eventos principal.
    """

    root = tk.Tk()
    root.title("SandTech - Gestión de Clientes")
    root.geometry("500x350")
    root.configure(bg="#e3eaf2")
    root.eval('tk::PlaceWindow . center')

    app = ClientesMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()