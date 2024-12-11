// cabalero
document.addEventListener('DOMContentLoaded', function() {
    // Función para abrir el modal de editar cabalero y cargar los datos
    window.openEditCabaleroModal = function(rut) {
        // Realizar una solicitud AJAX para obtener los datos del cabalero
        fetch(`/obtener_cabalero/${rut}/`)
            .then(response => response.json())
            .then(data => {
                // Llenar los campos del formulario con los datos obtenidos
                document.getElementById('nombres').value = data.nombres;
                document.getElementById('apellidos').value = data.apellidos;
                document.getElementById('telefono').value = data.telefono;
                document.getElementById('direccion').value = data.direccion;

                // Establecer la URL de acción del formulario para la edición
                document.getElementById('editCabaleroForm').action = `/editar_cabalero/${rut}/`;

                // Mostrar el modal de edición
                document.getElementById('editModalCabalero').style.display = 'block';
            })
            .catch(error => console.error('Error al obtener los datos del cabalero:', error));
    }



    // Cerrar el modal de editar cabalero
    const closeEditModalBtn = document.getElementById('closeEditModalBtnCabalero');
    if (closeEditModalBtn) {
        closeEditModalBtn.onclick = function() {
            document.getElementById('editModalCabalero').style.display = 'none'; // Ocultar el modal
        }
    }
});
