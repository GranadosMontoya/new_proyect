$(document).ready(function () {
    $.ajax({
        url: '/api/categorias/',  // Asegúrate que este sea el endpoint correcto
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            const $categoria = $('#categoria');
            $categoria.empty();  // Limpiamos cualquier opción anterior
            $categoria.append('<option disabled selected>Seleccione una categoría</option>');
            data.forEach(categoria => {
                $categoria.append(
                    $('<option>', {
                        value: categoria.id,
                        text: categoria.nombre
                    })
                );
            });
        },
        error: function (xhr, status, error) {
            console.error('Error al cargar las categorías:', error);
        }
    });

    $.ajax({
        url: '/api/proveedor/',  // Asegúrate que este sea el endpoint correcto
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            const $proveedor = $('#proveedor');
            $proveedor.empty();  // Limpiamos cualquier opción anterior
            $proveedor.append('<option disabled selected>Seleccione una proveedor</option>');
            data.forEach(proveedor => {
                $proveedor.append(
                    $('<option>', {
                        value: proveedor.id,
                        text: proveedor.nombre
                    })
                );
            });
        },
        error: function (xhr, status, error) {
            console.error('Error al cargar los proveedores:', error);
        }
    });
    
});

$("#product_form").submit(function(event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append("nombre", $("#nombre").val());
    formData.append("sku", $("#sku").val());
    formData.append("codigo_barras", $("#codigo_barras").val());
    formData.append("precio_base", $("#precio_base").val());
    formData.append("precio_publico", $("#precio_publico").val());
    formData.append("cantidad", $("#cantidad").val());
    formData.append("stock_minimo", $("#stock_minimo").val());
    formData.append("categoria", $("#categoria").val());
    formData.append("proveedor", $("#proveedor").val());
    formData.append("fecha_vencimiento", $("#fecha_vencimiento").val());
    formData.append("unidad_medida", $("#unidad_medida").val());
    formData.append("control_stock", $("#control_stock").val());
    formData.append("impuesto", $("#impuesto").val());
    formData.append("descuento", $("#descuento").val());
    formData.append("estado", $("#estado").val());
    var imageInput = $('#imagen')[0];
    if (imageInput.files.length > 0) {
        formData.append('imagen', imageInput.files[0]);
    }


    $.ajax({
        url: '/api/products/',
        method: 'POST',
        headers: { 'X-CSRFToken': getCSRFToken() },
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            console.log('Producto creado correctamente:', response);
            // Opcional: limpiar formulario
            $("#product_form")[0].reset();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error al crear producto:', textStatus, errorThrown);
        }
    });
});

