class Cliente:
    def __init__(self, codigo, nombre, apellido, email):
        """
        Constructor de la clase Cliente.

        Parametros:
        codigo (int): numero de identificacion del cliente.
        nombre (str): nombre del cliente.
        apellido (str): apellido del cliente.
        email (str): direccion correo electronica del cliente.

        """
        if nombre is None or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if apellido is None or apellido.strip() == "":
            raise ValueError("El apellido no puede estar vacío.")
        if email is None or email.strip() == "":
            raise ValueError("El email no puede estar vacío.")

        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        """
        Representacion de objeto como cadena.

        Retorna una cadena que describe al objeto en forma de "Cliente(codigo=XX, nombre=XXX, apellido=XXX, email=XXX@XXX.XXX)".
        
        Returns:
        str: representacion del objeto como cadena.
        """
        return f"Cliente(codigo={self.codigo}, nombre={self.nombre}, apellido={self.apellido}, email={self.email})"
