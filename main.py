import json

DATA_FILE = "productos.json"

def cargar_datos():
    try:
        with open(DATA_FILE, 'r') as file:
            contenido = file.read()
            if not contenido:  # Si el archivo está vacío
                return {}
            return json.loads(contenido)
    except FileNotFoundError:
        return {}  # Si el archivo no existe, devolvemos un diccionario vacío
    except json.JSONDecodeError:
        return {}  # Si el JSON es inválido, devolvemos un diccionario vacío


def guardar_datos(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def crear_producto(producto):
    data = cargar_datos()
    if producto['id'] in data:
        return "Producto con ID ya existe."
    data[producto['id']] = producto
    guardar_datos(data)
    return "Producto creado exitosamente."

def leer_producto(id_producto):
    data = cargar_datos()
    return data.get(id_producto, "Producto no encontrado.")

def actualizar_producto(id_producto, campos):
    data = cargar_datos()
    if id_producto not in data:
        return "Producto no encontrado."
    data[id_producto].update(campos)
    guardar_datos(data)
    return "Producto actualizado."

def eliminar_producto(id_producto):
    data = cargar_datos()
    if id_producto not in data:
        return "Producto no encontrado."
    del data[id_producto]
    guardar_datos(data)
    return "Producto eliminado."
