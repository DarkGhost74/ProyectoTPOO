# ProyectoTPOO
Este es el proyecto final del equipo 1 del grupo 004 de Taller de programación orientada a objetos.

El objetivo de este proyecto es simplificar la gestión y manejo de las pólizas de seguro. Los usuarios del proyecto podrán ver y editar las pólizas y usuarios del sistema, así como también ver una lista completa de los agentes y aseguradoras que se encuentran en el sistema. Además, podrán tener acceso a reportes detallados de las pólizas de seguro y las relaciones de los agentes con las aseguradoras, así como de las aseguradoras con los tipos de póliza que maneja cada una. Los usuarios podrán también crear una póliza desde cero pudiendo escoger o crear un usuario para esta y manejar fácilmente los campos requeridos para la creación de esta.

## Instalación y ejecución del servidor de prueba
Si se desea descargar el proyecto para ejecutarlo localmente en un servidor de pruebas es necesario seguir los siguientes pasos:
### 1. Instalar Python.
Es necesario tener instalada la versión 3.13 de Python, si no se tienen instalado Python puede descargarlo [aquí.](https://www.python.org/downloads/) Es importante que verifique que Python y pip estén agregados al path y puedan ejecutarse desde consola.
### 2. Instalar el proyecto.
Para instalar el proyecto puede descargarse directamente en un archivo `.zip` o ejecutando en cualquier carpeta desde git Bash:
``` 
git clone https://github.com/DarkGhost74/ProyectoTPOO.git
```

### 3. Crear un entorno virtual.
Para crear el entorno virtual puede utilizar cualquier herramienta de Python, como venv. Para crear el entorno, se debe de ejecutar en la carpeta del proyecto el siguiente comando:
``` 
python -m venv venv
```

### 4. Activar el entorno virtual
Si se está usando PowerShell se debe de ejecutar en la misma carpeta el siguiente comando:
```
 .\venv\Scripts\Activate.ps1
```
O bien, si es desde el CMD, el comando:
```
venv\Scripts\activate
```

### 5. Instalar requerimientos.
Para instalar los requerimientos basta con ir a la carpeta del proyecto recién instalado y ejecutar:
```
pipenv install -r requirements.txt
```

### 6. Ejecutar el servidor de pruebas.
Para correr el servidor local se debe de ejecutar en la carpeta del proyecto el comando:
```
python manage.py runserver
```

### 7. Editar el código del proyecto.
Si se desea modificar el código se debe se asegurar que sea con el intérprete de Python del entorno virtual. En VS Code por ejemplo, puede hacerse presionando F1, seleccionar interprete de Python, y seleccionar el interprete local. Si se va a trabajar en VS Code se debe de asegurar tener instaladas las extensiones de Python de Microsoft, Django y Djaneiro. Así como tambien ir a la ruta `File > Preferences > Settings`, en el filtro poner `pylint` y en los Args agregar:
```
"pylint.args": ["--load-plugins", "pylint_django"]
```

## Base de datos
El proyecto se conecta a una base de datos remota de pruebas alojada en Clever Cloud. Las credenciales de acceso se encuentran en la linea 83 de `ProyectoTPOO/settings.py`.
Si se desea conectar a la BD mediante terminal puede ejecutar el comando
```
mysql -h blbobicm5ybh67kjinxc-mysql.services.clever-cloud.com -P 3306 -u uxxuzbyn4sknuup3 -p blbobicm5ybh67kjinxc
```
y escribir la contraseña
```
HWnbIzeSH3zcsx97Bu3M
```
Teniendo acceso desde terminal se puede verificar más a detalle las tablas de esta. Unicamente las siguientes tablas cuentas con `managed = False` en sus respectivos modelos:
| Tablas |
|--------------|
| agente |
| aseguradora |
| cliente |
| detalleAgAs |
| detalleAsTP |
| formaPago |
| generoCliente |
| metodoPago |
| poliza |
| tipoPoliza  |

El que los modelos de dichas tablas tengan `managed = False` significa que fueron agregadas manualmente a la BD y unicamente el desarrollador tiene el poder de cambiarlas. Django no tiene el poder de modificarlas o crearlas al ejecutar `python manage.py makemigrations`, para eso se tendría que cambiar el valor a `managed = True`.

### Crear copia de la BD
Si se desea crear una copia local de la BD o alojada en otro lado se debe de cambiar el valor `managed = False` a `managed = True` en todos los modelos de las respectivas tablas. Luego se debe de ir a la linea 83 de `ProyectoTPOO/settings.py` y cambiar las credenciales a las de la nueva BD. Despues se debe ejecutar:
```
python manage.py makemigrations
```
y luego:
```
python manage.py migrate
```
Esto hace que Django pueda tener control sobre todas las tablas y crearlas desde cero.

### Crear copia sin `managed = True`
Si no se desea que Django tenga control sobre estas tablas solamente se deben de seguir todos los pasos excepto cambiar `managed`, y crear las tablas correspondientes desde cero. Para esto se puede apoyar ejecutando `describe tabla;` con cada una de las tablas conectado mediante terminal a la BD remota.
