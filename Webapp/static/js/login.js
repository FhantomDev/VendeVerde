var rutLogin = document.getElementById("rut");
var passLogin = document.getElementById("password");

var formLogin = document.getElementById("login");
var alertaLogin = document.getElementById("alerta-login");

formLogin.addEventListener("submit", function (evento) {
    var validarLogin = true; // Cambiado a true

    var validarRut = /^.{10}$/;
    var validarPass = /^.{6,15}$/;

    if (!validarRut.test(rutLogin.value)) {
        validarLogin = false;
        rutLogin.style.border = "2px solid red";
    } else {
        rutLogin.style.border = "2px solid green";
    }
    if (!validarPass.test(passLogin.value)) {
        validarLogin = false;
        passLogin.style.border = "2px solid red";
    } else {
        passLogin.style.border = "2px solid green";
    }

    if (validarLogin == false) {
        evento.preventDefault();
        alertaLogin.innerText = "¡Error!";
        alertaLogin.style.border = "2px solid red";
        alertaLogin.style.backgroundColor = "lightcoral";
        alertaLogin.style.fontSize = "20px";
        alertaLogin.style.fontWeight = "bold";
        alertaLogin.style.textAlign = "center";
        alertaLogin.style.height = "50px";
        alertaLogin.style.lineHeight = "50px";
    } 
});