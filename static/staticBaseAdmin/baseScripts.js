// Obtener el botón, el menú y la capa de fondo
const navbarToggle = document.querySelector('.navbar-toggler');
const navbarCollapse = document.getElementById('navbarNav');
const backdrop = document.getElementById('backdrop');
const body = document.body;

// Función para mostrar el menú y la capa de fondo
navbarToggle.addEventListener('click', function() {
    // Alternamos la visibilidad del menú
    navbarCollapse.classList.toggle('show');
    
    // Manejamos la capa de fondo oscurecido
    backdrop.style.display = navbarCollapse.classList.contains('show') ? 'block' : 'none';
    backdrop.style.opacity = navbarCollapse.classList.contains('show') ? '1' : '0';
    body.style.backgroundColor = navbarCollapse.classList.contains('show') ? 'rgba(0, 0, 0, 0.5)' : '';

    // Evitar desplazamiento del contenido cuando el menú esté abierto
    body.classList.toggle('menu-open', navbarCollapse.classList.contains('show'));
});

// Función para cerrar el menú si se hace clic fuera de él
backdrop.addEventListener('click', function() {
    navbarCollapse.classList.remove('show');
    backdrop.style.display = 'none';
    backdrop.style.opacity = '0';
    body.style.backgroundColor = '';
    body.classList.remove('menu-open');
});


document.addEventListener('DOMContentLoaded', function() {
    // Función para abrir el modal de agregar cabalero
    window.openAddModal = function() {
        // Mostrar el modal de agregar cabalero
        document.getElementById('myModal').style.display = 'block';
    }
    // Cerrar el modal de agregar cabalero
    const closeAddModalBtn = document.getElementById('closeModalBtn');
    if (closeAddModalBtn) {
        closeAddModalBtn.onclick = function() {
            document.getElementById('myModal').style.display = 'none'; // Ocultar el modal
        }
    }
});























