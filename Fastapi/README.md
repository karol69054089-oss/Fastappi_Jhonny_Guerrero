# Proyecto Clientes - API con FastAPI

## Descripción

Este proyecto consiste en una API desarrollada con FastAPI para la gestión de clientes, facturas y transacciones.

La aplicación permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) utilizando FastAPI, SQLModel y SQLite como base de datos.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- SQLModel
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

## Estructura del proyecto

```
FASAPI/
│
├── app/
│   ├── enrutadores/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── modelos/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── conexion_bd.py
│   ├── listas.py
│   └── main.py
│
├── bd_clientes.sqlite3
├── requirements.txt
└── README.md
```

## Instalación

### 1. Crear el entorno virtual

```
python -m venv .mi_env
```

### 2. Activar el entorno virtual

En Windows:

```
.\.mi_env\Scripts\Activate
```

### 3. Instalar las dependencias

```
pip install -r requirements.txt
```

## Ejecutar el proyecto

```
fastapi dev app/main.py
```

También puede ejecutarse con:

```
uvicorn app.main:app --reload
```

## Documentación de la API

Una vez iniciado el servidor, ingresar al siguiente enlace desde el navegador:

```
http://127.0.0.1:8000/docs
```

Allí se encuentran disponibles todos los endpoints de la API para realizar las pruebas.

## Funcionalidades

### Clientes

- Crear cliente.
- Consultar todos los clientes.
- Consultar un cliente por ID.
- Actualizar un cliente.
- Eliminar un cliente.

### Facturas

- Crear factura.
- Consultar todas las facturas.
- Consultar una factura por ID.
- Actualizar una factura.
- Eliminar una factura.

### Transacciones

- Crear transacción.
- Consultar todas las transacciones.
- Consultar una transacción por ID.
- Actualizar una transacción.
- Eliminar una transacción.

## Base de datos

El proyecto utiliza SQLite como sistema gestor de base de datos.

Archivo utilizado:

```
bd_clientes.sqlite3
```

## Autor

**Juan Sebastián Acosta Garcia**
