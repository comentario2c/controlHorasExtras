document.addEventListener('DOMContentLoaded', function() {
// Initialize Lucide icons
lucide.createIcons();

const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenuIcon = document.getElementById('mobile-menu-icon');
let isCollapsed = false;
let isMobileMenuOpen = false;

// Check screen size on load
checkScreenSize();

// Handle sidebar hover behavior (desktop)
if (window.innerWidth >= 640) {
    sidebar.addEventListener('mouseenter', expandSidebar);
    sidebar.addEventListener('mouseleave', collapseSidebar);
}

// Handle menu item clicks (accordion functionality)
const menuItems = document.querySelectorAll('.menu-item');
menuItems.forEach(item => {
    item.addEventListener('click', function() {
        const submenuId = this.getAttribute('aria-controls');
        const submenu = document.getElementById(submenuId);
        const chevron = this.querySelector('.chevron');
        const isExpanded = this.getAttribute('aria-expanded') === 'true';
        
        // Close all other submenus
        if (!isExpanded) {
            document.querySelectorAll('.submenu').forEach(sm => {
                if (sm.id !== submenuId) {
                    sm.style.maxHeight = '0';
                    sm.previousElementSibling.setAttribute('aria-expanded', 'false');
                    sm.previousElementSibling.querySelector('.chevron').classList.remove('rotate-chevron');
                }
            });
        }
        
        // Toggle current submenu
        this.setAttribute('aria-expanded', !isExpanded);
        chevron.classList.toggle('rotate-chevron');
        
        if (isExpanded) {
            submenu.style.maxHeight = '0';
        } else {
            submenu.style.maxHeight = submenu.scrollHeight + 'px';
        }
    });
});

// Mobile menu toggle
mobileMenuButton.addEventListener('click', function() {
    isMobileMenuOpen = !isMobileMenuOpen;
    sidebar.classList.toggle('sidebar-mobile-open');
    
    // Change icon
    if (isMobileMenuOpen) {
        mobileMenuIcon.innerHTML = '<line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line>';
    } else {
        mobileMenuIcon.innerHTML = '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>';
    }
});

// Window resize handler
window.addEventListener('resize', function() {
    checkScreenSize();
});

function expandSidebar() {
    if (window.innerWidth >= 640 && isCollapsed) {
        sidebar.classList.remove('sidebar-collapsed');
        sidebar.classList.add('sidebar-expanded');
        mainContent.classList.remove('ml-[72px]');
        mainContent.classList.add('ml-[240px]');
        isCollapsed = false;
    }
}

function collapseSidebar() {
    if (window.innerWidth >= 640 && !isCollapsed) {
        sidebar.classList.remove('sidebar-expanded');
        sidebar.classList.add('sidebar-collapsed');
        mainContent.classList.remove('ml-[240px]');
        mainContent.classList.add('ml-[72px]');
        isCollapsed = true;
    }
}

function checkScreenSize() {
    if (window.innerWidth < 640) {
        // Mobile behavior
        sidebar.classList.remove('sidebar-expanded', 'sidebar-collapsed');
        sidebar.classList.add('sidebar-hover-area');
        mainContent.classList.remove('ml-[240px]', 'ml-[72px]');
        isCollapsed = false;
        
        // Remove desktop hover events
        sidebar.removeEventListener('mouseenter', expandSidebar);
        sidebar.removeEventListener('mouseleave', collapseSidebar);
    } else {
        // Desktop behavior
        sidebar.classList.remove('sidebar-mobile-open');
        isMobileMenuOpen = false;
        mobileMenuIcon.innerHTML = '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>';
        
        // Add desktop hover events
        sidebar.addEventListener('mouseenter', expandSidebar);
        sidebar.addEventListener('mouseleave', collapseSidebar);
        
        // Set initial state
        if (!isCollapsed) {
            sidebar.classList.add('sidebar-expanded');
            mainContent.classList.add('ml-[240px]');
        } else {
            sidebar.classList.add('sidebar-collapsed');
            mainContent.classList.add('ml-[72px]');
        }
    }
}
});