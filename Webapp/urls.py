from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("contacto", views.contacto, name="contacto"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("registro", views.registro, name="registro"),
    path("usuario", views.usuario, name="usuario"),
    path("admin", views.admin, name="admin"),
    path("exito", views.exito, name="exito"),
    path("error", views.error, name="error"),
    path("loginCliente", views.loginCliente, name="loginCliente"),
    path("updateCliente", views.updateCliente, name="updateCliente"),
    path("salir", views.salir, name="salir"),
    path("eliminarCliente/<str:pk>", views.eliminarCliente, name="eliminarCliente"),
    path("suscripcionCliente", views.suscripcionCliente, name="suscripcionCliente"),
    path("eliminarSuscripcion/<str:pk>", views.eliminarSuscripcion, name="eliminarSuscripcion"),
    path("comprar", views.comprar, name="comprar"),
    path("cambiarEstado", views.cambiarEstado, name="cambiarEstado"),
    path("carro", views.carro, name="carro"),
    path("agregarProducto/<str:producto_id>", views.agregarProducto, name="agregarProducto"),
    path("restarProducto/<str:producto_id>", views.restarProducto, name="restarProducto"),
    path("limpiarCarrito", views.limpiarCarrito, name="limpiarCarrito"),
]