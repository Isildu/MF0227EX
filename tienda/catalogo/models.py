from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # max_digits=10, decimal_places=2 permite hasta 99,999,999.99
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)] # El precio no puede ser negativo
    )
    descuento = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100)
        ] # El descuento debe estar entre 0 y 100
    )

    def __str__(self):
        return self.nombre