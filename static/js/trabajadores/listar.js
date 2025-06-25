document.addEventListener("DOMContentLoaded", function () {
    const celdasMonetarias = document.querySelectorAll(".monto");

    celdasMonetarias.forEach(celda => {
        let valorTexto = celda.textContent.replace(/[^\d,.-]/g, '');
        let numero = parseFloat(valorTexto.replace(/\./g, '').replace(',', '.'));
        if (!isNaN(numero)) {
            celda.textContent = "$" + numero.toLocaleString('de-DE');
        }
    });
});