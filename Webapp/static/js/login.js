var emailLogin = document.getElementById("email-login");
var passLogin = document.getElementById("password-login");

var formLogin = document.getElementById("login");
var alertaLogin = document.getElementById("alerta-login");

formLogin.addEventListener("submit", function (evento) {
    var validarForm = false;

    emailLogin.style.border = "2px solid red";
    passLogin.style.border = "2px solid red";
    
    if (validarForm == false) {
        evento.preventDefault();
        alertaLogin.innerText = "¡Error!";
        alertaLogin.style.border = "2px solid red";
        alertaLogin.style.backgroundColor = "lightcoral";
        alertaLogin.style.fontSize = "20px";
        alertaLogin.style.fontWeight = "bold";
        alertaLogin.style.textAlign = "center";
        alertaLogin.style.height = "50px"
        alertaLogin.style.lineHeight = "50px";


    } else {
        evento.preventDefault();
    }
})