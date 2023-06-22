$(document).ready(function () {
  $.ajax({
    url: "https://apis.digital.gob.cl/dpa/regiones",
    type: "GET",
    crossDomain: true,
    dataType: "jsonp",
    success: function (data) {
      $.each(data, function (i, item) {
        $("#regiones").append(
          "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
        );
      });
    },
    error: function (xhr, status, error) {
      console.log("Error al obtener las regiones: " + error);
    },
  });
})

$("#regiones").change(function () {
  var idRegion = $("#regiones").val();
  $("#provincias").attr("disabled", false);
  $("#provincias").empty();
  $("#provincias").append("<option hidden disable>Seleccione una opción</option>");
  $("#comunas").empty();
  $("#comunas").append("<option hidden disable>Seleccione una opción</option>");

  $.ajax({
    url: "https://apis.digital.gob.cl/dpa/regiones/" + idRegion + "/provincias",
    type: "GET",
    crossDomain: true,
    dataType: "jsonp",
    success: function (data) {
      $.each(data, function (i, item) {
        $("#provincias").append(
          "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
        );
      });
    },
    error: function (xhr, status, error) {
      console.log("Error al obtener las regiones: " + error);
    },
  });

  $("#provincias").change(function () {
    var idRegion = $("#regiones").val();
    var idProvincia = $("#provincias").val();
    $("#comunas").attr("disabled", false);
    $("#comunas").empty();
    $("#comunas").append("<option hidden disable>Seleccione una opción</option>");
    $.ajax({
      url: "https://apis.digital.gob.cl/dpa/regiones/" + idRegion + "/provincias/" + idProvincia + "/comunas",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#comunas").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      },
    });
  });
});

