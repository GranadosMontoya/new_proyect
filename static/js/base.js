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

//Token global
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrfToken = getCookie('csrftoken');

// Mostrar Toasts
function mostrarToast(mensaje, tipo) {
    const contenedor = document.getElementById('contenedorToasts')

    const clase = tipo === 'success' ? 'toast-success' : tipo === 'error'   ? 'toast-error' :
  ''

    const toastHTML = `
        <div class="toast align-items-center ${clase}" role="alert">
        <div class="d-flex">
            <div class="toast-body">
            ${mensaje}
            </div>
            <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
        </div>
    `

    // Crear elemento
    const wrapper = document.createElement('div')
    wrapper.innerHTML = toastHTML

    const toastElement = wrapper.firstElementChild
    contenedor.appendChild(toastElement)

    // Inicializar y mostrar
    const toast = new bootstrap.Toast(toastElement)
    toast.show()

    // Eliminar del DOM cuando desaparezca
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove()
    })
}