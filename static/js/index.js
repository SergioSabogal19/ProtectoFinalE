document.getElementById("opciones").addEventListener("change", function() {
    var opcionSeleccionada = document.getElementById("opciones").value;
    var textoMostrado = "";

    switch(opcionSeleccionada) {
        case "opcion1":
            textoMostrado = "Kernel de Detección de Bordes (Kernel Sobel)<br>" +
            "[ 1  0 -1 ]<br>" +
            "[ 2  0 -2 ]<br>" +
            "[ 1  0 -1 ]<br><br>" +
            "Este kernel se utiliza para detectar bordes en imágenes.<br>" +
            "Produce dos imágenes filtradas, una que resalta los bordes horizontales y otra los bordes verticales.";
            break;
        case "opcion2":
            textoMostrado = "Kernel de Suavizado (Kernel de Media)<br>" +
            "[ 1/9  1/9  1/9 ]<br>" +
            "[ 1/9  1/9  1/9 ]<br>" +
            "[ 1/9  1/9  1/9 ]<br><br>" +
            "Este kernel se utiliza para suavizar la imagen, reduciendo el ruido y las imperfecciones..<br>" +
            "Calcula el valor de cada píxel promediando los valores de los píxeles vecinos.";
            break;
        case "opcion3":
            textoMostrado = "Kernel de Realce de Bordes (Kernel Laplaciano)<br>" +
            "[ 0  1  0 ]<br>" +
            "[ 1 -4  1 ]<br>" +
            "[ 0  1  0 ]<br><br>" +
            "Este kernel resalta los bordes en una imagen al detectar cambios bruscos en la intensidad de los píxeles.";
            break;
        default:
            textoMostrado = "Seleccione una opción";
    }

    document.getElementById("texto-opcion").innerHTML = textoMostrado;
});


