document.addEventListener('DOMContentLoaded', function() {

    // Función para abrir el modal de editar contador y cargar los datos
    window.openEditCabalaModal = function(idCavala) {
        // Realizar una solicitud AJAX para obtener los datos del contador
        fetch(`/obtener_cabala/${idCavala}/`)
            .then(response => response.json())
            .then(data => {
                // Llenar los campos del formulario con los datos obtenidos
                document.getElementById('sector').value = data.sectorCavala;

                // Establecer la URL de acción del formulario para la edición
                document.getElementById('editCabalaForm').action = `/editar_cabala/${idCavala}/`;

                // Mostrar el modal de edición
                document.getElementById('editCabalaModal').style.display = 'block';
            })
            .catch(error => console.error('Error al obtener los datos del cabala:', error));
    }


    // Cerrar el modal de editar contador
    const closeEditModalBtn = document.getElementById('closeEditCabalaModalBtn');
    if (closeEditModalBtn) {
        closeEditModalBtn.onclick = function() {
            document.getElementById('editModalCabala').style.display = 'none'; // Ocultar el modal
        }
    }
});
