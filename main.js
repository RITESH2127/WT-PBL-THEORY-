// Theme Switcher Logic
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const iconEl = document.getElementById('theme-icon');
    if (iconEl) {
        if (theme === 'dark') {
            iconEl.classList.remove('ph-moon');
            iconEl.classList.add('ph-sun');
        } else {
            iconEl.classList.remove('ph-sun');
            iconEl.classList.add('ph-moon');
        }
    }
}

// Toast Notification System
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    let icon = type === 'success' ? 'ph-check-circle' : 'ph-warning-circle';
    if (type === 'error') icon = 'ph-x-circle';

    toast.innerHTML = `
        <i class="ph ${icon} ph-lg"></i>
        <span>${message}</span>
    `;

    container.appendChild(toast);

    // Remove toast after animation finishes
    setTimeout(() => {
        if (container.contains(toast)) {
            container.removeChild(toast);
        }
    }, 3500);
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Capture existing flask flashes embedded in HTML
    const flashMessages = document.querySelectorAll('.flask-flash-message');
    flashMessages.forEach(flash => {
        showToast(flash.dataset.message, flash.dataset.category);
        flash.remove();
    });
});
