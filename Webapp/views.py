from django.shortcuts import render, redirect
from .models import cliente, tipoUsuario, comuna, empleado, pedido, detallePedido, suscripcion, producto, despacho, estado_despacho
from .carro import Carrito
from datetime import datetime, timedelta
from django.db import IntegrityError
from django.db.models import F

# Create your views here.


def index(request):
    carrito = Carrito(request)
    total = carrito.obtener_total()

    run = request.session.get('runCliente')
    
    try:
        sus = suscripcion.objects.get(runSuscriptor=run)
    except suscripcion.DoesNotExist:
        sus = None

    context = {
        "total": total,
        "suscripcion": sus,
    }
    return render(request, "pages/index.html", context)



def contacto(request):
    context = {

    }
    return render(request, "pages/contacto.html", context)


def nosotros(request):
    context = {

    }
    return render(request, "pages/nosotros.html", context)


def registro(request):
    if request.method != "POST":
        com = comuna.objects.all()
        context = {
            "comuna": com,
        }
        return render(request, "pages/registro.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        contraseña = request.POST["password"]
        apPaterno = request.POST["apPaterno"]
        apMaterno = request.POST["apMaterno"]
        direccion = request.POST["direccion"]
        correo = request.POST["email"]
        telefono = request.POST["telefono"]
        comunaCli = request.POST["comunas"]
        tipo = 2

        objComuna = comuna.objects.get(idComuna=comunaCli)
        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        try:
            objCliente = cliente.objects.create(
                runCliente=rut,
                nombreCliente=nombre,
                contraseñaCliente=contraseña,
                apPaternoCliente=apPaterno,
                apMaternoCliente=apMaterno,
                direccionCliente=direccion,
                correoCliente=correo,
                telefonoCliente=telefono,
                tipoUsuario=objTipo,
                comuna=objComuna,
            )
            objCliente.save()
            context = {
                "mensaje": "Registrado correctamente"
            }
            return render(request, "pages/exito.html", context)
        except IntegrityError:
            context = {
                "mensaje": "El rut ya está registrado"
            }
            return render(request, "pages/error.html", context)



def loginCliente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            cli = cliente.objects.get(runCliente=username, contraseñaCliente=password)
        except cliente.DoesNotExist:
            cli = None

        try:
            emp = empleado.objects.get(runEmpleado=username, contraseñaEmpleado=password)
        except empleado.DoesNotExist:
            emp = None

        if cli is not None:
            request.session["runCliente"] = username
            usuarios = request.session["runCliente"]
            cli = cliente.objects.filter(runCliente=usuarios)
            context = {
                "mensaje": "Inicio de sesión exitoso"
                }
            return render(request, "pages/exito.html", context)
        elif emp is not None:
            request.session["runEmpleado"] = username
            usuarios = request.session["runEmpleado"]
            context = {
                "mensaje": "Inicio de sesión exitoso"
                }
            return render(request, "pages/exito.html", context)
        else:
            context = {"mensaje": "Usuario y/o Contraseña erronea"}
            return render(request, "pages/error.html", context)

    return render(request, "pages/login.html")


def updateCliente(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        contraseña = request.POST["password"]
        apPaterno = request.POST["apPaterno"]
        apMaterno = request.POST["apMaterno"]
        direccion = request.POST["direccion"]
        correo = request.POST["email"]
        telefono = request.POST["telefono"]
        comunaCli = request.POST["comunas"]
        tipo = 2

        objComuna = comuna.objects.get(idComuna=comunaCli)
        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        cli = cliente()
        cli.runCliente = rut
        cli.nombreCliente = nombre
        cli.contraseñaCliente = contraseña
        cli.apPaternoCliente = apPaterno
        cli.apMaternoCliente = apMaterno
        cli.direccionCliente = direccion
        cli.correoCliente = correo
        cli.telefonoCliente = telefono
        cli.tipoUsuario = objTipo
        cli.comuna = objComuna
        cli.save()

        context = {
            "mensaje": "Actualizado Correctamente"
        }
        return render(request, "pages/exito.html", context)


def productos(request):
    pro = producto.objects.all()
    carrito = Carrito(request)
    total = carrito.obtener_total()
    context = {
        "producto": pro,
        "total": total,
    }
    return render(request, "pages/productos.html", context)


def usuario(request):
    run = request.session.get('runCliente')
    cli = cliente.objects.get(runCliente=run)
    ped = pedido.objects.filter(cliente=cli)
    des = despacho.objects.filter(pedido__in=ped)
    com = comuna.objects.all()
    context = {
        "cliente": cli,
        "pedido": ped,
        "despacho": des,
        "comuna": com,
    }
    return render(request, "pages/usuario.html", context)


def admin(request):
    run = request.session.get('runEmpleado')
    emp = empleado.objects.get(runEmpleado=run)
    cli = cliente.objects.all()
    ped = pedido.objects.all()
    des = despacho.objects.all()

    context = {
        "empleado": emp,
        "cliente": cli,
        "pedido": ped,
        "despacho": des,
    }
    return render(request, "pages/admin.html", context)


def cambiarEstado(request):
    if request.method == "POST":
        idDes = request.POST["idDespacho"]
        estado = request.POST["estadoDespacho"]

        objDespacho = despacho.objects.get(idDespacho=idDes)
        objEstado = estado_despacho.objects.get(idEstado=estado)

        objDespacho.estado = objEstado
        objDespacho.save()

        return redirect("admin")


def exito(request):
    context = {

    }
    return render(request, "pages/exito.html", context)


def error(request):
    context = {

    }
    return render(request, "pages/error.html", context)


def salir(request):
    if "runCliente" in request.session:
        del request.session["runCliente"]
    elif "runEmpleado" in request.session:
        del request.session["runEmpleado"]
    return redirect("index")


def eliminarCliente(request, pk):
    context = {}
    try:
        cli = cliente.objects.get(runCliente=pk)

        cli.delete()
        cli = cliente.objects.all()
        emp = empleado.objects.all()
        context = {
            "mensaje": "Cliente eliminado",
            "cliente": cli,
            "empleado": emp
        }
        return render(request, "pages/exito.html", context)
    except:
        cli = cliente.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...",
                   "clientes": cli}
        return render(request, "pages/error.html", context)
    

def eliminarSuscripcion(request, pk):
    context = {}
    try:
        sus = suscripcion.objects.get(runSuscriptor=pk)
        sus.delete()
        context = {
            "mensaje": "Suscripción eliminada",
        }
        return render(request, "pages/exito.html", context)
    except:
        context = {"mensaje": "Error",}
        return render(request, "pages/error.html", context)
    

def suscripcionCliente(request):
    if request.method == "POST":
        run = request.session.get('runCliente')
        monto = request.POST["suscripcion"]
        objSus = suscripcion.objects.create(
            runSuscriptor = run,
            montoSuscripcion = monto
        )
        objSus.save()
    context = {
        "mensaje": "Susripción exitosa"
    }
    return render(request, "pages/exito.html", context)


def comprar(request):
    if request.method == "POST":
        run = request.session.get('runCliente')
        cli = cliente.objects.get(runCliente=run)

        totalPed = request.POST["totalPedido"]
        fechaPed = datetime.now()

        if suscripcion.objects.filter(runSuscriptor=run).exists():
            descuentoPed = float(totalPed) * 0.05
            totalPed = float(totalPed) - descuentoPed
        else:
            descuentoPed = 0

        objPedido = pedido.objects.create(
            fechaPedido=fechaPed,
            descuentoPedido=descuentoPed,
            totalPedido=totalPed,
            cliente=cli,
        )
        objPedido.save()

        fechaDespacho = fechaPed + timedelta(days=1)
        fechaEntrega = fechaPed + timedelta(days=2)
        est=1
        objEstado = estado_despacho.objects.get(idEstado=est)
 
        objDespacho = despacho.objects.create(
            fechaDespacho=fechaDespacho,
            fechaEntrega=fechaEntrega,
            pedido=objPedido,
            estado=objEstado,
        )
        objDespacho.save()

        carrito = request.session.get('carrito', {})
        for producto_id, value in carrito.items():
            pro = producto.objects.get(idProducto=producto_id)
            cantidad = value['cantidad']
            subTotal = value['acumulado']

            objDetallePedido = detallePedido.objects.create(
                pedido=objPedido,
                producto=pro,
                cantidadProducto=cantidad,
                subtotalPedido=subTotal,
            )
            objDetallePedido.save()
            producto.objects.filter(idProducto=producto_id).update(stockProducto=F('stockProducto') - cantidad)


        limpiarCarrito(request)

    context = {
            "mensaje": "Compra exitosa"
    }
    return render(request, "pages/exito.html", context)


def agregarProducto(request, producto_id):
    carrito = Carrito(request)
    pro = producto.objects.get(idProducto=producto_id)
    carrito.agregar(pro)
    return redirect("productos")

def eliminarProducto(request, producto_id):
    carrito = Carrito(request)
    pro = producto.objects.get(idProducto=producto_id)
    carrito.eliminar(pro)
    return redirect("productos")

def restarProducto(request, producto_id):
    carrito = Carrito(request)
    pro = producto.objects.get(idProducto=producto_id)
    carrito.restar(pro)
    return redirect("productos")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")


def carro(request):
    return render(request, "pages/carro.html")