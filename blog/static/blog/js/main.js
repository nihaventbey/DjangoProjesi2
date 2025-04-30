document.addEventListener('DOMContentLoaded', function() {
  // Login Form Toggle
  const loginToggle = document.getElementById('loginToggle');
  const loginForm = document.getElementById('loginForm');

  if (loginToggle && loginForm) {
    loginToggle.addEventListener('click', function(e) {
      e.preventDefault();
      loginForm.classList.toggle('active');
      
      function closeForm(event) {
        if (!loginForm.contains(event.target) && event.target !== loginToggle) {
          loginForm.classList.remove('active');
          document.removeEventListener('click', closeForm);
        }
      }
      
      document.addEventListener('click', closeForm);
    });
  }

  // Logout butonu onayı
  document.querySelectorAll('form[action*="logout"]').forEach(form => {
    form.addEventListener('submit', (e) => {
      if (!confirm('Çıkış yapmak istediğinize emin misiniz?')) {
        e.preventDefault();
      }
    });
  });
});
