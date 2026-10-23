"""
URL configuration for Tarea4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'administradores'

urlpatterns = [
    path('productos/', views.ListarCategorias, name='productosapp'),
    path('crear_categoria/', views.CrearCategoria.as_view(), name='crearcategoriaapp'),
    path('editar_categoria/<int:pk>', views.EditarCategoria.as_view(), name='editarcategoriaapp'),
    path('toggle_categoria/<int:pk>', views.ToggleCategoriaActivo, name='togglecategoriainactivoapp'),

    path('categoria/<int:cid>/productos/', views.ListarProductosCategoria, name='productoscat'),
    path('categoria/<int:cid>/crear_producto/', views.CrearProducto.as_view(), name='crearproductoapp'),
    path('editar_producto/<int:pk>', views.EditarProducto.as_view(), name='editarproductoapp'),
    path('ver_producto/<int:pk>', views.VerProducto.as_view(), name='verproductoapp'),
    path('toggle_producto/<int:pk>', views.ToggleProductoActivo, name='toggleproductoinactivoapp'),

    path('compras/', views.ListarCompras, name='comprasapp'),
    path('crear_compra/', views.CrearCompra, name='crearcompraapp'),
    path('editar_compra/<int:pk>', views.EditarCompra.as_view(), name='editarcompraapp'),
    path('ver_compra/<int:pk>', views.VerCompra.as_view(), name='vercompraapp'),
    path('toggle_compra/<int:pk>', views.ToggleCompraActivo, name='togglecomprainactivoapp'),

    path('ver_carrito/', views.VerCarrito, name='vercarritoapp'),
    path('agregar_producto_carrito/', views.AgregarProductoCarrito, name='agregarproductocarritoapp'),
    path('quitar_producto_carrito/<int:pk>', views.QuitarProductoCarrito, name='quitarproductocarritoapp'),

    path('proveedores/', views.ListarProveedores, name='proveedoresapp'),
    path('crear_proveedor/', views.CrearProveedor.as_view(), name='crearproveedorapp'),
    path('editar_proveedor/<int:pk>', views.EditarProveedor.as_view(), name='editarproveedorapp'),
    path('toggle_proveedor/<int:pk>', views.ToggleProveedorActivo, name='toggleproveedorinactivoapp'),

    path('clientes/', views.ListarClientes, name='clientesapp'),
    path('crear_cliente/', views.CrearCliente.as_view(), name='crearclienteapp'),
    path('editar_cliente/<int:pk>', views.EditarCliente.as_view(), name='editarclienteapp'),

    path('ventas/', views.ListarVentas, name='ventasapp'),
    path('crear_venta/', views.CrearVenta, name='crearventaapp'),
    path('editar_venta/<int:pk>', views.EditarVenta.as_view(), name='editarventaapp'),
    path('ver_venta/<int:pk>', views.VerVenta.as_view(), name='verventaapp'),
    path('toggle_venta/<int:pk>', views.ToggleVentaActivo, name='toggleventainactivoapp'),

    path('ver_carrito_venta/', views.VerCarritoVenta, name='vercarritoventaapp'),
    path('agregar_producto_carrito_venta/', views.AgregarProductoVenta, name='agregarproductocarritoventaapp'),
    path('quitar_producto_carrito_venta/<int:pk>', views.QuitarProductoVenta, name='quitarproductocarritoventaapp'),

    path('reportes/', views.Reportes, name='reportesapp'),
    path('login/', views.LoginView.as_view(), name='loginapp'),
]
