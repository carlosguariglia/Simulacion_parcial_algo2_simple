# SandTech Clientes App

## Descripción del Proyecto
La aplicación "SandTech Clientes" es una herramienta diseñada para gestionar los pedidos de artículos de los clientes de la empresa SandTech. Este módulo permite registrar, modificar y eliminar información sobre los clientes, así como listar y buscar clientes específicos.

## Estructura del Proyecto
El proyecto está organizado en varias carpetas y archivos, cada uno con una función específica:

- **src/**: Contiene el código fuente de la aplicación.
  - **main.py**: Punto de entrada de la aplicación, inicializa la interfaz gráfica y comienza el bucle de eventos.
  - **db/**: Maneja la conexión y operaciones de la base de datos SQLite.
    - **database.py**: Contiene funciones para crear la base de datos y gestionar los registros de clientes.
  - **gui/**: Contiene los componentes de la interfaz gráfica.
    - **clientes_menu.py**: Funciones para mostrar menús y manejar interacciones del usuario.
  - **models/**: Define las estructuras de datos.
    - **cliente.py**: Clase que representa a un cliente con atributos como id, nombre e información de contacto.
  - **controllers/**: Contiene la lógica de negocio.
    - **cliente_controller.py**: Funciones para añadir, eliminar, modificar y recuperar clientes de la base de datos.
  - **utils/**: Funciones utilitarias.
    - **logger.py**: Proporciona funcionalidad de registro para rastrear eventos y transacciones de la aplicación. por ahora muestra los logs por consola


TODO:
- **diagrams/**: Contiene diagramas que representan la arquitectura del sistema y otros aspectos del diseño.
  - **sistema_general.png**: Diagrama de la arquitectura general del sistema.
  - **paquetes.png**: Ilustra la estructura de paquetes y capas arquitectónicas.
  - **clases.png**: Diagrama de clases que detalla las relaciones entre las diferentes clases.
  - **secuencia_alta_cliente.png**: Diagrama de secuencia para el proceso de registro de clientes.

- **README.md**: Documentación del proyecto, incluyendo instrucciones de configuración y pautas de uso.

- **requirements.txt**: Lista de dependencias necesarias para el proyecto, incluyendo bibliotecas de Tkinter y SQLite.

## Instrucciones de Configuración
1. Clona el repositorio en tu máquina local.
2. Navega a la carpeta del proyecto.
3. Instala las dependencias utilizando el archivo `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```
   python src/main.py
   ```

## Uso
La aplicación permite gestionar los clientes a través de un menú interactivo. Los usuarios pueden:
- Dar de alta nuevos clientes.
- Dar de baja clientes existentes.
- Modificar la información de los clientes.
- Listar todos los clientes o buscar uno específico por código.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.