
//Obtener los campos
var rut = document.getElementById("rut");
var email = document.getElementById("email");
var pass = document.getElementById("password");
var nombre = document.getElementById("nombre");
var apellidos = document.getElementById("apellidos");
var direccion = document.getElementById("direccion");
var telefono = document.getElementById("telefono");
var comuna = document.getElementById("comunas");
var provincia = document.getElementById("provincias");
var region = document.getElementById("regiones");

var formRegistro = document.getElementById("form-registro");
var alerta = document.getElementById("alerta");

var Fn = {
  // Valida el rut con su cadena completa "XXXXXXXX-X"
  validaRut: function (rutCompleto) {
    rutCompleto = rutCompleto.replace("‐", "-");
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
      return false;
    var tmp = rutCompleto.split('-');
    var digv = tmp[1];
    var rut = tmp[0];
    if (digv == 'K') digv = 'k';

    return (Fn.dv(rut) == digv);
  },
  dv: function (T) {
    var M = 0, S = 1;
    for (; T; T = Math.floor(T / 10))
      S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
  }
};

formRegistro.addEventListener("submit", function (evento) {
  var validarForm = true;
  var validarEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var validarPass = /^[a-zA-Z0-9]{6,15}$/;
  var validarNombre = /^([a-zA-Z]{2,}\s[a-zA-Z]{2,}|[a-zA-Z]{2,})$/;
  var validarApellidos = /^([a-zA-Z]{2,}\s[a-zA-Z]{2,}|[a-zA-Z]{2,})$/;
  var validarDireccion = /^(?=.*\d)(?=.*\s)[\w\s,.#-]{5,}$/;
  var validarTelefono = /^[1-9]\d{8}$/;

  if (!Fn.validaRut(rut.value)) {
    validarForm = false;
    rut.style.border = "2px solid red";
  } else {
    rut.style.border = "2px solid green";
  }
  if (!validarEmail.test(email.value)) {
    validarForm = false;
    email.style.border = "2px solid red";
  } else {
    email.style.border = "2px solid green";
  }
  if (!validarPass.test(pass.value)) {
    validarForm = false;
    pass.style.border = "2px solid red";
  } else {
    pass.style.border = "2px solid green";
  }
  if (!validarNombre.test(nombre.value)) {
    validarForm = false;
    nombre.style.border = "2px solid red";
  } else {
    nombre.style.border = "2px solid green";
  }
  if (!validarApellidos.test(apellidos.value)) {
    validarForm = false;
    apellidos.style.border = "2px solid red";
  } else {
    apellidos.style.border = "2px solid green";
  }
  if (!validarDireccion.test(direccion.value)) {
    validarForm = false;
    direccion.style.border = "2px solid red";
  } else {
    direccion.style.border = "2px solid green";
  }
  if (!validarTelefono.test(telefono.value)) {
    validarForm = false;
    telefono.style.border = "2px solid red";
  } else {
    telefono.style.border = "2px solid green";
  }
  if (comuna.options[comuna.selectedIndex].text === "Seleccione una opción") {
    validarForm = false;
    comuna.style.border = "2px solid red";
  } else {
    comuna.style.border = "2px solid green";
  }
  if (provincia.options[provincia.selectedIndex].text === "Seleccione una opción") {
    validarForm = false;
    provincia.style.border = "2px solid red";
  } else {
    provincia.style.border = "2px solid green";
  }
  if (region.options[region.selectedIndex].text === "Seleccione una opción") {
    validarForm = false;
    region.style.border = "2px solid red";
  } else {
    region.style.border = "2px solid green";
  }

  if (validarForm == false) {
    evento.preventDefault();
    alerta.innerText = "¡Error! Complete correctamente el formulario";
    alerta.style.border = "2px solid red";
    alerta.style.backgroundColor = "lightcoral";
    alerta.style.fontSize = "20px";
    alerta.style.fontWeight = "bold";
    alerta.style.textAlign = "center";
    alerta.style.height = "80px";
    console.log(Fn.validaRut(rut.value));

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
