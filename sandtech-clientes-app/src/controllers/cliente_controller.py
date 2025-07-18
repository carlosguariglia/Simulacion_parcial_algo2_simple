from db.database import Database
from utils.logger import log_info, log_warning, log_error
from models.cliente import Cliente  # Importa la clase Cliente

class ClienteController:
    """
    Controlador para gestionar operaciones CRUD de clientes en la base de datos SQLite.
    """
    def __init__(self):
        """
        Constructor del controlador.
        
        Crea una instancia de la base de datos en 'clientes.db' y verifica si la tabla 'clientes' existe, de lo contrario la crea.
        """
        self.db = Database("clientes.db")
        self._crear_tabla()

    def __del__(self):  
        """  
        Destructor que cierra la conexión a la base de datos cuando se destruye el controlador.  
        No es una forma efectiva y el garbage collector de Python no garantiza que se llame inmediatamente.
        """  
        if hasattr(self, 'db') and self.db:  
            self.db.close_connection()  
            log_info("Conexión de base de datos cerrada.")


    def _crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
        self.db.execute(query)
        # Establecer el valor inicial del AUTOINCREMENT en 100 si es la primera vez
        self._set_autoincrement_start(100)
        log_info("Tabla 'clientes' verificada o creada.")

    def _set_autoincrement_start(self, start_value):
        # Verifica si la secuencia ya existe
        seq = self.db.fetchone("SELECT seq FROM sqlite_sequence WHERE name='clientes'")
        if not seq:
            # Inserta el valor inicial (start_value - 1) porque SQLite suma 1 al siguiente insert
            self.db.execute("INSERT INTO sqlite_sequence (name, seq) VALUES (?, ?)", ("clientes", start_value - 1))

    def alta_cliente(self, cliente):
        query = "INSERT INTO clientes (nombre, apellido, email) VALUES (?, ?, ?)"
        self.db.execute(query, (cliente.nombre, cliente.apellido, cliente.email))
        log_info(f"Alta de cliente: {cliente.nombre} {cliente.apellido} ({cliente.email})")

    def baja_cliente(self, codigo):
        query = "DELETE FROM clientes WHERE codigo = ?"
        result = self.db.execute(query, (codigo,))
        if result and result.rowcount > 0:
            log_info(f"Baja de cliente código: {codigo}")
            return True
        else:
            log_warning(f"Intento de baja fallido para código: {codigo}")
            return False

    def modificar_cliente(self, cliente):
        query = "UPDATE clientes SET nombre=?, apellido=?, email=? WHERE codigo=?"
        result = self.db.execute(query, (cliente.nombre, cliente.apellido, cliente.email, cliente.codigo))
        if result and result.rowcount > 0:
            log_info(f"Modificación de cliente código: {cliente.codigo}")
            return True
        else:
            log_warning(f"Intento de modificación fallido para código: {cliente.codigo}")
            return False

    def listar_clientes(self):
        query = "SELECT codigo, nombre, apellido, email FROM clientes"
        clientes_tuplas = self.db.fetchall(query)
        clientes = [Cliente(*tupla) for tupla in clientes_tuplas]
        log_info(f"Listado de clientes: {len(clientes)} encontrados.")
        return clientes

    def buscar_cliente(self, codigo):
        query = "SELECT codigo, nombre, apellido, email FROM clientes WHERE codigo=?"
        tupla = self.db.fetchone(query, (codigo,))
        if tupla:
            log_info(f"Búsqueda exitosa de cliente código: {codigo}")
            return Cliente(*tupla)
        else:
            log_warning(f"Búsqueda fallida de cliente código: {codigo}")
            return None