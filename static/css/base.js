document.addEventListener('DOMContentLoaded', function () {
    const toggles = document.querySelectorAll('.dropdown-toggle');
  
    toggles.forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
  
        const currentDropdown = toggle.closest('.sidebar-dropdown');
        const isActive = currentDropdown.classList.contains('active');
  
        // Cierra todos los menús
        document.querySelectorAll('.sidebar-dropdown.active').forEach(function (dropdown) {
          dropdown.classList.remove('active');
        });
  
        // Si no estaba activo, activarlo
        if (!isActive) {
          currentDropdown.classList.add('active');
        }
      });
    });
  });
  