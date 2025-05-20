document.addEventListener("DOMContentLoaded", function () {
    const riveCanvas = document.getElementById("rive-canvas");

    new rive.Rive({
        src: "/static/animations/factura.riv",
        canvas: riveCanvas,
        autoplay: true,
        onLoad: () => {
            console.log("Animación cargada");
            setTimeout(() => {
                document.getElementById("loader").classList.add("hidden");
            }, 3000);
        }
    });
    window.mostrarLoader = function () {
        document.getElementById("loader").classList.remove("hidden");
    };
});

