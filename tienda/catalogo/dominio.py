class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        # Validación: el precio no puede ser negativo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def precio_final(self):
        # Devuelve el precio original
        return self.precio

    
class ProductoOferta(ProductoBase):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        # Validación del descuento (entre 0 y 100)
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.descuento = descuento

    def precio_final(self):
        # Devuelve el precio con el descuento aplicado
        return self.precio - (self.precio * self.descuento / 100)

   
