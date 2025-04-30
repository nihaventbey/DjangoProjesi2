document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('#themeToggle');  // Burada düzeltildi
    if (!themeToggle) return;  // Eğer bulunamazsa hiçbir şey yapma

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
        if (icon) {
            if (currentTheme === 'dark') {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            } else {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            }
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
