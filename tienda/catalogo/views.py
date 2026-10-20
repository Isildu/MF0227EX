from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from .dominio import ProductoOferta # Importamos la clase de la Fase 1

# Create your views here.
def lista_productos(request):
    productos_db = Producto.objects.all()
    productos_procesados = []

    # Iteramos sobre los productos de la base de datos
    for p in productos_db:
        # Creamos un objeto de nuestra clase ProductoOferta
        # Convertimos el precio Decimal a float para que la clase lo acepte sin problemas
        producto_oferta = ProductoOferta(p.nombre, float(p.precio), p.descuento)
        
        # Añadimos el precio final calculado al diccionario que enviaremos al HTML
        productos_procesados.append({
            'nombre': p.nombre,
            'precio_original': p.precio,
            'descuento': p.descuento,
            'precio_final': producto_oferta.precio_final()
        })

    return render(request, 'catalogo/lista.html', {'productos': productos_procesados})


def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al listado tras guardar con éxito
            return redirect('lista_productos') 
    else:
        form = ProductoForm()

    return render(request, 'catalogo/formularios.html', {'form': form})