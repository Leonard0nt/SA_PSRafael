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
            document.getElementById('editCabalaModal').style.display = 'none'; // Ocultar el modal
        }
    }
});

/* globals Chart:false */

(() => {
    'use strict'
  
    // Graphs
    const ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    const myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          'Sunday',
          'Monday',
          'Tuesday',
          'Wednesday',
          'Thursday',
          'Friday',
          'Saturday'
        ],
        datasets: [{
          data: [
            15339,
            21345,
            18483,
            24003,
            23489,
            24092,
            12034
          ],
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        }]
      },
      options: {
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            boxPadding: 3
          }
        }
      }
    })
  })()
  