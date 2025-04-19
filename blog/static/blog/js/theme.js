document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const icon = themeToggle.querySelector('i');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Sistem tercihini kontrol et
    let currentTheme = localStorage.getItem('theme') || 
                      (prefersDarkScheme.matches ? 'dark' : 'light');
    
    // Temayı uygula
    const applyTheme = () => {
        document.body.setAttribute('data-theme', currentTheme);
        localStorage.setItem('theme', currentTheme);
        
        // İkonu güncelle
        if (currentTheme === 'dark') {
            icon.classList.replace('fa-sun', 'fa-moon');
        } else {
            icon.classList.replace('fa-moon', 'fa-sun');
        }
    };
    
    // Toggle butonu işlevi
    themeToggle.addEventListener('click', () => {
        currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme();
    });
    
    // İlk yüklemede temayı uygula
    applyTheme();
});