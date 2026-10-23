from django.contrib import admin
from .models import Categoria, Cliente, Proveedor, Usuario, Producto, Compra, DetalleCompra, Venta, DetalleVenta
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio_compra', 'precio_venta', 'cantidad', 'fecha_vencimiento', 'id_categoria', 'activo']
    list_filter = ['activo', 'id_categoria']
    list_editable = ['activo']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'activo']
    list_filter = ['activo']
    list_editable = ['activo']

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'total', 'id_proveedor', 'id_usuario', 'activo']
    list_filter = ['activo']
    list_editable = ['activo']

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'total', 'id_cliente', 'id_usuario', 'activo']
    list_filter = ['activo']
    list_editable = ['activo']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'telefono', 'direccion', 'activo']
    list_filter = ['activo']
    list_editable = ['activo']

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(DetalleCompra)
admin.site.register(DetalleVenta)
