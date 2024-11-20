import unittest
import json
from main import crear_producto, leer_producto, actualizar_producto, eliminar_producto

class TestCRUD(unittest.TestCase):
    def setUp(self):
        """Reinicia el archivo JSON antes de cada prueba."""
        with open("productos.json", "w") as file:
            json.dump({}, file)

    # Test para Crear Producto
    def test_crear_producto_exitoso(self):
        resultado = crear_producto({"id": "1", "nombre": "Producto A", "descripcion": "Desc A", "precio": 100, "cantidad": 10})
        self.assertEqual(resultado, "Producto creado exitosamente.")
    
    def test_crear_producto_id_existente(self):
        crear_producto({"id": "1", "nombre": "Producto A", "descripcion": "Desc A", "precio": 100, "cantidad": 10})
        resultado = crear_producto({"id": "1", "nombre": "Producto B", "descripcion": "Desc B", "precio": 200, "cantidad": 5})
        self.assertEqual(resultado, "Producto con ID ya existe.")

    # Test para Leer Producto
    def test_leer_producto_exitoso(self):
        crear_producto({"id": "1", "nombre": "Producto A", "descripcion": "Desc A", "precio": 100, "cantidad": 10})
        producto = leer_producto("1")
        self.assertEqual(producto['nombre'], "Producto A")
    
    def test_leer_producto_no_existente(self):
        producto = leer_producto("99")
        self.assertEqual(producto, "Producto no encontrado.")

    # Test para Actualizar Producto
    def test_actualizar_producto_exitoso(self):
        crear_producto({"id": "1", "nombre": "Producto A", "descripcion": "Desc A", "precio": 100, "cantidad": 10})
        resultado = actualizar_producto("1", {"precio": 120})
        self.assertEqual(resultado, "Producto actualizado.")
    
    def test_actualizar_producto_no_existente(self):
        resultado = actualizar_producto("99", {"precio": 120})
        self.assertEqual(resultado, "Producto no encontrado.")

    # Test para Eliminar Producto
    def test_eliminar_producto_exitoso(self):
        crear_producto({"id": "1", "nombre": "Producto A", "descripcion": "Desc A", "precio": 100, "cantidad": 10})
        resultado = eliminar_producto("1")
        self.assertEqual(resultado, "Producto eliminado.")
    
    def test_eliminar_producto_no_existente(self):
        resultado = eliminar_producto("99")
        self.assertEqual(resultado, "Producto no encontrado.")

if __name__ == "__main__":
    unittest.main()
