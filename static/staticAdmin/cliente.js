document.addEventListener('DOMContentLoaded', function() {

    // Función para abrir el modal de editar contador y cargar los datos
    window.openEditClienteModal = function(rut) {
        // Realizar una solicitud AJAX para obtener los datos del contador
        fetch(`/obtener_cliente/${rut}/`)
            .then(response => response.json())
            .then(data => {
                // Llenar los campos del formulario con los datos obtenidos
                document.getElementById('nombres').value = data.nombres;
                document.getElementById('apellidos').value = data.apellidos;
                document.getElementById('telefono').value = data.telefono;
                document.getElementById('direccion').value = data.direccion;

                // Establecer la URL de acción del formulario para la edición
                document.getElementById('formEditCliente').action = `/editar_cliente/${rut}/`;

                // Mostrar el modal de edición
                document.getElementById('editModalCliente').style.display = 'block';
            })
            .catch(error => console.error('Error al obtener los datos del cliente:', error));
    }


    // Cerrar el modal de editar contador
    const closeEditModalBtn = document.getElementById('closeEditModalBtnCliente');
    if (closeEditModalBtn) {
        closeEditModalBtn.onclick = function() {
            document.getElementById('editModalCliente').style.display = 'none'; // Ocultar el modal
        }
    }
});
