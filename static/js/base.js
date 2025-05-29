// Pantalla de carga
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => { // Simula una pequeña carga
        document.getElementById("loader").style.display = "none";
        document.getElementById("contentContainer").style.display = "block";
    }, 1000); // Puedes ajustar el tiempo si lo necesitas
});

$(document).ready(function () {
    $(document).ajaxStart(function () {
        $("#loader").fadeIn();  // Mostrar loader cuando empieza una petición
    }).ajaxStop(function () {
        $("#loader").fadeOut(); // Ocultar loader cuando termina la petición
    });
});

// Token
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith('csrftoken=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}
