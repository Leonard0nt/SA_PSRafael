document.addEventListener('DOMContentLoaded', function() {

    // Función para abrir el modal de editar contador y cargar los datos
    window.openEditContadorModal = function(rut) {
        // Realizar una solicitud AJAX para obtener los datos del contador
        fetch(`/obtener_contador/${rut}/`)
            .then(response => response.json())
            .then(data => {
                // Llenar los campos del formulario con los datos obtenidos
                document.getElementById('nombres').value = data.nombres;
                document.getElementById('apellidos').value = data.apellidos;
                document.getElementById('telefono').value = data.telefono;
                document.getElementById('direccion').value = data.direccion;

                // Establecer la URL de acción del formulario para la edición
                document.getElementById('formEditContador').action = `/editar_contador/${rut}/`;

                // Mostrar el modal de edición
                document.getElementById('editModalContador').style.display = 'block';
            })
            .catch(error => console.error('Error al obtener los datos del contador:', error));
    }


    // Cerrar el modal de editar contador
    const closeEditModalBtn = document.getElementById('closeEditModalBtnContador');
    if (closeEditModalBtn) {
        closeEditModalBtn.onclick = function() {
            document.getElementById('editModalContador').style.display = 'none'; // Ocultar el modal
        }
    }
});

