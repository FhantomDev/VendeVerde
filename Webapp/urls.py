from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("contacto", views.contacto, name="contacto"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("registro", views.registro, name="registro"),
    path("plantas", views.plantas, name="plantas"),
    path("macetas", views.macetas, name="macetas"),
    path("flores", views.flores, name="flores"),
    path("usuario", views.usuario, name="usuario"),
    path("admin", views.admin, name="admin"),

]
