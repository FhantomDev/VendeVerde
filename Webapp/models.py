from django.db import models

# Create your models here.

# REGION  
class region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_region)
    

# PROVINCIA
class provincia(models.Model):
    idProvincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=50, blank=False, null=False)
    region = models.ForeignKey("region", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_provincia)
    

# COMUNA
class comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30, blank=False, null=False)
    provincia = models.ForeignKey("provincia", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_comuna)


# TIPO USUARIO
class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True)
    nombreTipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombreTipoUsuario)
    

# CLIENTE
class cliente(models.Model):
    runCliente = models.CharField(max_length=10, primary_key=True)
    nombreCliente = models.CharField(max_length=30, blank=False, null=False)
    apPaternoCliente = models.CharField(max_length=30, blank=False, null=False)
    apMaternoCliente = models.CharField(max_length=30, blank=False, null=False)
    direccionCliente = models.CharField(max_length=30, blank=False, null=False)
    telefonoCliente = models.IntegerField()
    correoCliente = models.EmailField(blank=False, null=False, max_length=30)
    contraseñaCliente = models.CharField(max_length=30, blank=False, null=False)
    comuna = models.ForeignKey("comuna", on_delete=models.CASCADE)
    tipoUsuario = models.ForeignKey("tipoUsuario", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreCliente)+" "+str(self.apPaternoCliente)+" "+str(self.apMaternoCliente)
    

class empleado(models.Model):
    runEmpleado = models.CharField(max_length=10, primary_key=True)
    nombreEmpleado = models.CharField(max_length=30, blank=False, null=False)
    apPaternoEmpleado = models.CharField(max_length=30, blank=False, null=False)
    apMaternoEmpleado = models.CharField(max_length=30, blank=False, null=False)
    contraseñaEmpleado = models.CharField(max_length=30, blank=False, null=False)
    tipoUsuario = models.ForeignKey("tipoUsuario", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreEmpleado)+" "+str(self.apPaternoEmpleado)+" "+str(self.apMaternoEmpleado)
    

class pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fechaPedido = models.DateField(blank=False, null=False)
    descuentoPedido = models.IntegerField()
    totalPedido = models.IntegerField()
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPedido)+" "+str(self.cliente)


class estado_despacho(models.Model):
    idEstado = models.AutoField(primary_key=True)
    nombreEstado = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.nombreEstado)


class despacho(models.Model):
    idDespacho = models.AutoField(primary_key=True)
    fechaDespacho = models.DateField(blank=False, null=False)
    fechaEntrega = models.DateField(blank=False, null=False)
    pedido = models.ForeignKey("pedido", on_delete=models.CASCADE)
    estado = models.ForeignKey("estado_despacho", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idDespacho)+" "+str(self.fechaDespacho)
    

class producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=20, blank=False, null=False)
    precioProducto = models.IntegerField()
    stockProducto = models.IntegerField()

    def __str__(self):
        return str(self.nombreProducto)
    

class detallePedido(models.Model):
    pedido = models.ForeignKey("pedido", on_delete=models.CASCADE)
    producto = models.ForeignKey("producto", on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()
    subtotalPedido = models.IntegerField()

    def __str__(self):
        return str(self.pedido)+" "+str(self.producto)
    

class promocion(models.Model):
    idPromocion = models.AutoField(primary_key=True)
    fechaPromocion = models.DateField(blank=False, null=False)
    descuentoPromocion = models.IntegerField()

    def __str__(self):
        return str(self.fechaPromocion)
    

class suscripcion(models.Model):
    runSuscriptor = models.CharField(primary_key=True, max_length=10, blank=False, null=False)
    montoSuscripcion = models.IntegerField()

    def __str__(self):
        return str(self.runSuscriptor)