from tkinter import Tk, Menu, messagebox, Toplevel, Label, Entry, Button, Listbox, END
from controllers.cliente_controller import ClienteController
from models.cliente import Cliente  # Asegúrate de importar la clase Cliente

class ClientesMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Clientes")
        self.cliente_controller = ClienteController()

        # Create the menu
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # Add menu items
        self.client_menu = Menu(self.menu)
        self.menu.add_cascade(label="Clientes", menu=self.client_menu)
        self.client_menu.add_command(label="Dar de alta", command=self.dar_alta)
        self.client_menu.add_command(label="Dar de baja", command=self.dar_baja)
        self.client_menu.add_command(label="Modificar", command=self.modificar)
        self.client_menu.add_command(label="Listar", command=self.listar)
        self.client_menu.add_command(label="Buscar", command=self.buscar)
        self.client_menu.add_separator()
        self.client_menu.add_command(label="Salir", command=self.master.quit)

    def dar_alta(self):
        alta_win = Toplevel(self.master)
        alta_win.title("Alta de Cliente")
        alta_win.configure(bg="#f0f4f7")

        label_font = ("Segoe UI", 11)
        entry_font = ("Segoe UI", 11)

        Label(alta_win, text="Nombre:", font=label_font, bg="#f0f4f7").grid(row=0, column=0, padx=10, pady=8, sticky="e")
        nombre_entry = Entry(alta_win, font=entry_font)
        nombre_entry.grid(row=0, column=1, padx=10, pady=8)

        Label(alta_win, text="Apellido:", font=label_font, bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=8, sticky="e")
        apellido_entry = Entry(alta_win, font=entry_font)
        apellido_entry.grid(row=1, column=1, padx=10, pady=8)

        Label(alta_win, text="Email:", font=label_font, bg="#f0f4f7").grid(row=2, column=0, padx=10, pady=8, sticky="e")
        email_entry = Entry(alta_win, font=entry_font)
        email_entry.grid(row=2, column=1, padx=10, pady=8)

        def guardar_cliente():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            email = email_entry.get()
            if nombre and apellido and email:
                try:
                    nuevo_cliente = Cliente(None, nombre, apellido, email)
                    self.cliente_controller.alta_cliente(nuevo_cliente)
                    messagebox.showinfo("Éxito", "Cliente dado de alta correctamente.")
                    alta_win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo dar de alta: {e}")
            else:
                messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")

        Button(alta_win, text="Guardar", command=guardar_cliente, bg="#1976d2", fg="white", font=label_font, width=15).grid(row=3, column=0, columnspan=2, pady=12)

    def dar_baja(self):
        baja_win = Toplevel(self.master)
        baja_win.title("Baja de Cliente")

        Label(baja_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(baja_win)
        codigo_entry.grid(row=0, column=1)

        def eliminar_cliente():
            codigo = codigo_entry.get()
            if codigo:
                try:
                    if self.cliente_controller.baja_cliente(int(codigo)):
                        messagebox.showinfo("Éxito", "Cliente dado de baja correctamente.")
                        baja_win.destroy()
                    else:
                        messagebox.showwarning("No encontrado", "No se encontró el cliente.")
                except ValueError:
                    messagebox.showwarning("Valor inválido", "El código debe ser un número entero.")
            else:
                messagebox.showwarning("Campo vacío", "Ingrese el código de cliente.")

        Button(baja_win, text="Eliminar", command=eliminar_cliente).grid(row=1, column=0, columnspan=2)

    def modificar(self):
        mod_win = Toplevel(self.master)
        mod_win.title("Modificar Cliente")

        Label(mod_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(mod_win)
        codigo_entry.grid(row=0, column=1)

        # Campos para mostrar y editar
        Label(mod_win, text="Nombre:").grid(row=1, column=0)
        nombre_entry = Entry(mod_win)
        nombre_entry.grid(row=1, column=1)

        Label(mod_win, text="Apellido:").grid(row=2, column=0)
        apellido_entry = Entry(mod_win)
        apellido_entry.grid(row=2, column=1)

        Label(mod_win, text="Email:").grid(row=3, column=0)
        email_entry = Entry(mod_win)
        email_entry.grid(row=3, column=1)

        def cargar_datos():
            codigo = codigo_entry.get()
            if codigo:
                try:
                    cliente = self.cliente_controller.buscar_cliente(int(codigo))
                    if cliente:
                        nombre_entry.delete(0, 'end')
                        nombre_entry.insert(0, cliente.nombre)
                        apellido_entry.delete(0, 'end')
                        apellido_entry.insert(0, cliente.apellido)
                        email_entry.delete(0, 'end')
                        email_entry.insert(0, cliente.email)
                    else:
                        messagebox.showwarning("No encontrado", "No se encontró el cliente.")
                except ValueError:
                    messagebox.showwarning("Valor inválido", "El código debe ser un número entero.")
            else:
                messagebox.showwarning("Campo vacío", "Ingrese el código de cliente.")

        def modificar_cliente():
            codigo = codigo_entry.get()
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            email = email_entry.get()
            if codigo and nombre and apellido and email:
                try:
                    cliente_mod = Cliente(int(codigo), nombre, apellido, email)
                    if self.cliente_controller.modificar_cliente(cliente_mod):
                        messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
                        mod_win.destroy()
                    else:
                        messagebox.showwarning("No encontrado", "No se encontró el cliente.")
                except ValueError:
                    messagebox.showwarning("Valor inválido", "El código debe ser un número entero.")
            else:
                messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")

        Button(mod_win, text="Cargar datos", command=cargar_datos).grid(row=0, column=2)
        Button(mod_win, text="Modificar", command=modificar_cliente).grid(row=4, column=0, columnspan=3)

    def listar(self):
        listar_win = Toplevel(self.master)
        listar_win.title("Lista de Clientes")
        listar_win.configure(bg="#f0f4f7")

        label_font = ("Segoe UI", 11)

        clientes = self.cliente_controller.listar_clientes()
        # Ahora clientes es una lista de objetos Cliente
        listbox = Listbox(listar_win, width=60, font=label_font, bg="#eaf1fb")
        listbox.pack(padx=10, pady=10)

        if clientes:
            for c in clientes:
                listbox.insert(END, f"Código: {c.codigo} | Nombre: {c.nombre} | Apellido: {c.apellido} | Email: {c.email}")
        else:
            listbox.insert(END, "No hay clientes registrados.")

        Button(listar_win, text="Cerrar", command=listar_win.destroy, bg="#1976d2", fg="white", font=label_font, width=15).pack(pady=10)

    def buscar(self):
        buscar_win = Toplevel(self.master)
        buscar_win.title("Buscar Cliente")

        Label(buscar_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(buscar_win)
        codigo_entry.grid(row=0, column=1)

        def buscar_cliente():
            codigo = codigo_entry.get()
            if codigo:
                try:
                    cliente = self.cliente_controller.buscar_cliente(int(codigo))
                    if cliente:
                        messagebox.showinfo("Cliente encontrado",
                            f"Código: {cliente.codigo}\nNombre: {cliente.nombre}\nApellido: {cliente.apellido}\nEmail: {cliente.email}")
                        buscar_win.destroy()
                    else:
                        messagebox.showwarning("No encontrado", "No se encontró el cliente.")
                except ValueError:
                    messagebox.showwarning("Valor inválido", "El código debe ser un número entero.")
            else:
                messagebox.showwarning("Campo vacío", "Ingrese el código de cliente.")

        Button(buscar_win, text="Buscar", command=buscar_cliente).grid(row=1, column=0, columnspan=2)

if __name__ == "__main__":
    root = Tk()
    app = ClientesMenu(root)
    root.mainloop()