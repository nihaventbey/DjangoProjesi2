document.addEventListener('DOMContentLoaded', function() {
  // Tema Değiştirme Fonksiyonu
  const themeToggle = document.getElementById('themeToggle');
  const currentTheme = localStorage.getItem('theme') || 'dark';

  // Başlangıç temasını ayarla
  document.body.setAttribute('data-theme', currentTheme);
  updateThemeIcon();

  // Tema değiştirme butonu
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      const newTheme = document.body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.body.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeIcon();
    });
  }

  function updateThemeIcon() {
    if (!themeToggle) return;
    const currentTheme = document.body.getAttribute('data-theme');
    themeToggle.innerHTML = currentTheme === 'dark' 
      ? '<i class="fas fa-sun"></i>' 
      : '<i class="fas fa-moon"></i>';
  }

  // Login Form Toggle
  const loginToggle = document.getElementById('loginToggle');
  const loginForm = document.getElementById('loginForm');

  if (loginToggle && loginForm) {
    loginToggle.addEventListener('click', function(e) {
      e.preventDefault();
      loginForm.classList.toggle('active');
      
      // Dışarı tıklamada kapat
      document.addEventListener('click', function closeForm(event) {
        if (!loginForm.contains(event.target) {
          loginForm.classList.remove('active');
          document.removeEventListener('click', closeForm);
        }
      });
    });
  }

  // Logout butonu onayı
  const logoutBtn = document.querySelector('.logout-btn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', function(e) {
      if (!confirm('Çıkış yapmak istediğinize emin misiniz?')) {
        e.preventDefault();
      }
    });
  }
});