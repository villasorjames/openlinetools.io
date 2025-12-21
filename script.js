// DOM Elements
const navLinks = document.querySelector('.nav-links');
const menuToggle = document.querySelector('.menu-toggle');
const downloadBtn = document.getElementById('downloadBtn');
const contactForm = document.getElementById('contactForm');
const skillLevels = document.querySelectorAll('.skill-level');

// Toggle Mobile Menu
menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    
    // Change menu icon
    const icon = menuToggle.querySelector('i');
    if (navLinks.classList.contains('active')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        const icon = menuToggle.querySelector('i');
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Animate skill bars on scroll
function animateSkillBars() {
    skillLevels.forEach(skill => {
        const skillWidth = skill.getAttribute('data-skill') + '%';
        skill.style.width = skillWidth;
    });
}

// Check if skill bars are in viewport
function checkSkillVisibility() {
    const skillsSection = document.querySelector('.skills-section');
    const sectionPosition = skillsSection.getBoundingClientRect().top;
    const screenPosition = window.innerHeight / 1.3;
    
    if (sectionPosition < screenPosition) {
        animateSkillBars();
        // Remove event listener after animation
        window.removeEventListener('scroll', checkSkillVisibility);
    }
}

// Handle form submission
contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    
    // In a real application, you would send this data to a server
    // For this example, we'll just show a success message
    alert(`Thank you ${name}! Your message has been sent. I'll get back to you soon at ${email}.`);
    
    // Reset form
    contactForm.reset();
});

// Handle resume download
downloadBtn.addEventListener('click', function(e) {
    e.preventDefault();
    
    // In a real application, this would link to an actual PDF file
    // For this example, we'll simulate a download
    alert('In a real portfolio, this would download your resume PDF. For now, consider this a simulation!');
    
    // You can replace the alert with actual download code:
    // window.open('path-to-your-resume.pdf', '_blank');
});

// Add scroll effect to navbar
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
        navbar.style.backdropFilter = 'blur(10px)';
    } else {
        navbar.style.backgroundColor = 'white';
        navbar.style.backdropFilter = 'none';
    }
});

// Initialize animations when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Start checking for skill section visibility
    window.addEventListener('scroll', checkSkillVisibility);
    
    // Initial check in case skills section is already in view
    checkSkillVisibility();
    
    // Add current year to footer
    const currentYear = new Date().getFullYear();
    const yearElement = document.querySelector('.footer p:first-child');
    if (yearElement) {
        yearElement.innerHTML = `&copy; ${currentYear} My Professional Portfolio. All rights reserved.`;
    }
    
    // Add typing effect to hero title (optional enhancement)
    const heroTitle = document.querySelector('.hero-title .highlight');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        heroTitle.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < originalText.length) {
                heroTitle.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        // Start typing after a short delay
        setTimeout(typeWriter, 500);
    }
});