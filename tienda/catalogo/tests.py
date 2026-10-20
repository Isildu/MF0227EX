from django.test import TestCase
from django.urls import reverse
from .dominio import ProductoOferta

class ProductoOfertaTestCase(TestCase):
    def test_precio_final_con_descuento(self):
        # 1. Verificar que un producto de 100 € con 20% de descuento devuelve 80 €
        producto = ProductoOferta("Producto Test", 100, 20)
        self.assertEqual(producto.precio_final(), 80.0)


class VistaListadoTestCase(TestCase):
    def test_pagina_productos_responde_200(self):
        # 2. Verificar que la página /productos/ responde con el código HTTP 200
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)

