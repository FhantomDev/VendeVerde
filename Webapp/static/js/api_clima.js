window.addEventListener('load', () => {
    let lon
    let lat

    let temperatura = document.getElementById('temperatura')
    let descripcion = document.getElementById('descripcion')
    let lugar = document.getElementById('lugar')
    let humedad = document.getElementById('humedad')

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(ubicacion => {

            lon = ubicacion.coords.longitude
            lat = ubicacion.coords.latitude
            const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=3ae80e82c01ac76584b76e5b7ed603ec&lang=es&units=metric`

            fetch(url)
                .then(response => { return response.json() })
                .then(datos => {

                    //console.log(datos)
                    console.log(datos.main.humidity)
                    temperatura.innerHTML = 'Temp. ' + datos.main.temp + ' °C'
                    descripcion.innerHTML = datos.weather[0].description
                    humedad.innerHTML = 'Humedad ' +datos.main.humidity+ '%'
                })
                .catch(error => {
                    console.log(error)


                })
        })
    }
})
