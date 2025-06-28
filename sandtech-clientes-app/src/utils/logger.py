# Este módulo define funciones para registrar 
# mensajes de log que saldran por consola 
# 
# Mas adelante se puede implementar un logger mas avanzado
# Incluso con persistencia en archivos o bases de datos

def log_info(message):
    print(f"[INFO] {message}")

def log_warning(message):
    print(f"[WARNING] {message}")

def log_error(message):
    print(f"[ERROR] {message}")

def log_debug(message):
    print(f"[DEBUG] {message}")