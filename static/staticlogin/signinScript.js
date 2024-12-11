document.addEventListener("DOMContentLoaded", function () {
  // Obtener el campo de contraseña y el checkbox para ver la contraseña
  const showPasswordCheckbox = document.getElementById('showPassword');
  var passwordField = document.querySelector('input[name="password"]');// Obtener el id del campo de contraseña generado por Django

  // Verificamos si el checkbox existe antes de agregar el listener
  if (showPasswordCheckbox) {
    showPasswordCheckbox.addEventListener('change', function () {
      if (this.checked) {
        // Si el checkbox está marcado, mostrar la contraseña
        passwordField.type = 'text';  // Cambiar el tipo de campo a 'text' para mostrar la contraseña
      } else {
        // Si el checkbox no está marcado, ocultar la contraseña
        passwordField.type = 'password';  // Cambiar el tipo de campo a 'password' para ocultarla
      }
    });
  }
});


