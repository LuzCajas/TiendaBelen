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
from django.contrib.auth.decorators import login_required

app_name = 'administradores'

urlpatterns = [
    path('productos/', login_required(views.ListarCategorias), name='productosapp'),
    path('crear_categoria/', login_required(views.CrearCategoria.as_view()), name='crearcategoriaapp'),
    path('editar_categoria/<int:pk>', login_required(views.EditarCategoria.as_view()), name='editarcategoriaapp'),
    path('toggle_categoria/<int:pk>', login_required(views.ToggleCategoriaActivo), name='togglecategoriainactivoapp'),

    path('categoria/<int:cid>/productos/', login_required(views.ListarProductosCategoria), name='productoscat'),
    path('categoria/<int:cid>/crear_producto/', login_required(views.CrearProducto.as_view()), name='crearproductoapp'),
    path('editar_producto/<int:pk>', login_required(views.EditarProducto.as_view()), name='editarproductoapp'),
    path('ver_producto/<int:pk>', login_required(views.VerProducto.as_view()), name='verproductoapp'),
    path('toggle_producto/<int:pk>', login_required(views.ToggleProductoActivo), name='toggleproductoinactivoapp'),

    path('compras/', login_required(views.ListarCompras), name='comprasapp'),
    path('crear_compra/', login_required(views.CrearCompra), name='crearcompraapp'),
    path('editar_compra/<int:pk>', login_required(views.EditarCompra.as_view()), name='editarcompraapp'),
    path('ver_compra/<int:pk>', login_required(views.VerCompra.as_view()), name='vercompraapp'),
    path('toggle_compra/<int:pk>', login_required(views.ToggleCompraActivo), name='togglecomprainactivoapp'),

    path('ver_carrito/', login_required(views.VerCarrito), name='vercarritoapp'),
    path('agregar_producto_carrito/', login_required(views.AgregarProductoCarrito), name='agregarproductocarritoapp'),
    path('quitar_producto_carrito/<int:pk>', login_required(views.QuitarProductoCarrito), name='quitarproductocarritoapp'),

    path('proveedores/', login_required(views.ListarProveedores), name='proveedoresapp'),
    path('crear_proveedor/', login_required(views.CrearProveedor.as_view()), name='crearproveedorapp'),
    path('editar_proveedor/<int:pk>', login_required(views.EditarProveedor.as_view()), name='editarproveedorapp'),
    path('toggle_proveedor/<int:pk>', login_required(views.ToggleProveedorActivo), name='toggleproveedorinactivoapp'),

    path('clientes/', login_required(views.ListarClientes), name='clientesapp'),
    path('crear_cliente/', login_required(views.CrearCliente.as_view()), name='crearclienteapp'),
    path('editar_cliente/<int:pk>', login_required(views.EditarCliente.as_view()), name='editarclienteapp'),

    path('ventas/', login_required(views.ListarVentas), name='ventasapp'),
    path('crear_venta/', login_required(views.CrearVenta), name='crearventaapp'),
    path('editar_venta/<int:pk>', login_required(views.EditarVenta.as_view()), name='editarventaapp'),
    path('ver_venta/<int:pk>', login_required(views.VerVenta.as_view()), name='verventaapp'),
    path('toggle_venta/<int:pk>', login_required(views.ToggleVentaActivo), name='toggleventainactivoapp'),

    path('ver_carrito_venta/', login_required(views.VerCarritoVenta), name='vercarritoventaapp'),
    path('agregar_producto_carrito_venta/', login_required(views.AgregarProductoVenta), name='agregarproductocarritoventaapp'),
    path('quitar_producto_carrito_venta/<int:pk>', login_required(views.QuitarProductoVenta), name='quitarproductocarritoventaapp'),

    path('reportes/', login_required(views.Reportes), name='reportesapp'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.LoginView.as_view(), name='loginapp'),
]
