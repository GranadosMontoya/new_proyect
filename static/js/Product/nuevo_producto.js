// ======================================================
// PUNTO DE ENTRADA
// ======================================================
document.addEventListener('DOMContentLoaded', function () {
    cargarCategorias();
    cargarProveedores();
    inicializarFormularioCategoria();
    inicializarFormularioProducto();
});


// ======================================================
// FORMULARIO: CREAR CATEGORÍA (MODAL)
// ======================================================
function inicializarFormularioCategoria() {
    const form = document.getElementById('formCategoria');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const nombre = document.getElementById('nombre_categoria').value.trim();
        const descripcion = document.getElementById('descripcion_categoria').value;

        if (!nombre) {
            alert('La categoría es obligatoria');
            return;
        }

        try {
            const response = await fetch('/api/categorias/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    nombre: nombre,
                    descripcion: descripcion
                })
            });

            if (!response.ok) {
                const error = await response.json();
                throw error;
            }

            const data = await response.json();

            agregarCategoriaAlSelect(data);
            cerrarModalCategoria();
            form.reset();

        } catch (error) {
            console.error('Error al crear categoría:', error);
        }
    });
}


// ======================================================
// FORMULARIO: CREAR PRODUCTO (PRINCIPAL)
// ======================================================
function inicializarFormularioProducto() {
    const form = document.getElementById('product_form');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('/api/products/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            });

            if (!response.ok) {
                const error = await response.json();
                throw error;
            }

            const data = await response.json();
            console.log('Producto creado correctamente:', data);

            form.reset();

        } catch (error) {
            console.error('Error al crear producto:', error);
        }
    });
}


// ======================================================
// CARGAR CATEGORÍAS (GET)
// ======================================================
async function cargarCategorias() {
    try {
        const response = await fetch('/api/categorias/');

        if (!response.ok) {
            throw new Error('Error al cargar categorías');
        }

        const data = await response.json();
        const select = document.getElementById('categoria');

        select.innerHTML = '<option disabled selected>Seleccione una categoría</option>';

        data.forEach(categoria => {
            const option = document.createElement('option');
            option.value = categoria.id;
            option.textContent = categoria.nombre;
            select.appendChild(option);
        });

    } catch (error) {
        console.error('Error al cargar categorías:', error);
    }
}


// ======================================================
// CARGAR PROVEEDORES (GET)
// ======================================================
async function cargarProveedores() {
    try {
        const response = await fetch('/api/proveedor/');

        if (!response.ok) {
            throw new Error('Error al cargar proveedores');
        }

        const data = await response.json();
        const select = document.getElementById('proveedor');

        select.innerHTML = '<option disabled selected>Seleccione un proveedor</option>';

        data.forEach(proveedor => {
            const option = document.createElement('option');
            option.value = proveedor.id;
            option.textContent = proveedor.nombre;
            select.appendChild(option);
        });

    } catch (error) {
        console.error('Error al cargar proveedores:', error);
    }
}


// ======================================================
// HELPERS
// ======================================================
function agregarCategoriaAlSelect(categoria) {
    const select = document.getElementById('categoria');

    const option = document.createElement('option');
    option.value = categoria.id;
    option.textContent = categoria.nombre;
    option.selected = true;

    select.appendChild(option);
}

function cerrarModalCategoria() {
    const modalElement = document.getElementById('modalCategoria');
    const modal = bootstrap.Modal.getInstance(modalElement);
    modal.hide();
}
