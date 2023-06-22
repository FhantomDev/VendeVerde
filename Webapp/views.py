from django.shortcuts import render

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
    context = {

    }
    return render(request, "pages/registro.html", context)


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
    context = {

    }
    return render(request, "pages/usuario.html", context)


def admin(request):
    context = {

    }
    return render(request, "pages/admin.html", context)
