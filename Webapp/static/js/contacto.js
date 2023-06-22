
var email = document.getElementById("email");
var asunto = document.getElementById("asunto");
var areaTexto = document.getElementById("areaTexto");

var formContacto = document.getElementById("form-contacto");
var alerta = document.getElementById("alerta");

formContacto.addEventListener("submit", function (evento) {
    var validarContacto = true;

    var validarEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var validarAsunto = /^[a-zA-Z0-9_ ]{4,15}$/;
    var validarTexto = /^[a-zA-Z0-9_ ,.?!¡¿-]{10,300}$/;

    if (!validarEmail.test(email.value)) {
        validarContacto = false;
    }
    if (!validarAsunto.test(asunto.value)) {
        validarContacto = false;
    }
    if (!validarTexto.test(areaTexto.value)) {
        validarContacto = false;
    }

    if (validarContacto == false) {
        evento.preventDefault();
        alerta.innerText = "¡Error! Complete correctamente el formulario";
        alerta.style.border = "2px solid red";
        alerta.style.backgroundColor = "lightcoral";
        alerta.style.fontSize = "20px";
        alerta.style.fontWeight = "bold";
        alerta.style.textAlign = "center";
        alerta.style.height = "50px"
        alerta.style.lineHeight = "50px";
    } else {
        evento.preventDefault();
        alerta.innerText = "Exito ";
        alerta.style.border = "2px solid green";
        alerta.style.backgroundColor = "palegreen";
        alerta.style.fontSize = "20px";
        alerta.style.fontWeight = "bold";
        alerta.style.textAlign = "center";
        alerta.style.height = "50px"
        alerta.style.lineHeight = "50px";
    }
})