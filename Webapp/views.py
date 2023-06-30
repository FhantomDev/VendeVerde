from django.shortcuts import render, redirect
from .models import cliente, tipoUsuario, comuna, empleado, pedido, detallePedido, suscripcion
from django.db import IntegrityError

# Create your views here.


def index(request):
    context = {
        
    }
    return render(request, "pages/index.html", context)


def productos(request):
    context = {

    }
    return render(request, "pages/productos.html", context)


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
        context = {

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


def plantas(request):
    context = {

    }
    return render(request, "pages/plantas.html", context)


def macetas(request):
    context = {

    }
    return render(request, "pages/macetas.html", context)


def flores(request):
    context = {

    }
    return render(request, "pages/flores.html", context)


def usuario(request):
    run = request.session.get('runCliente')
    cli = cliente.objects.get(runCliente=run)
    ped = pedido.objects.filter(cliente=cli)
    context = {
        "cliente": cli,
        "pedido": ped
    }
    return render(request, "pages/usuario.html", context)


def admin(request):
    run = request.session.get('runEmpleado')
    emp = empleado.objects.get(runEmpleado=run)
    cli = cliente.objects.all()
    context = {
        "empleado": emp,
        "cliente": cli
    }
    return render(request, "pages/admin.html", context)


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

    }
    return render(request, "pages/exito.html", context)