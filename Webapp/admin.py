from django.contrib import admin
from .models import cliente, tipoUsuario, comuna, provincia, region, empleado, pedido, despacho, producto, detallePedido, promocion, suscripcion
# Register your models here.

admin.site.register(cliente) 
admin.site.register(tipoUsuario)
admin.site.register(comuna) 
admin.site.register(provincia) 
admin.site.register(region)
admin.site.register(empleado)
admin.site.register(pedido)
admin.site.register(despacho)
admin.site.register(producto)
admin.site.register(detallePedido)
admin.site.register(promocion)
admin.site.register(suscripcion)