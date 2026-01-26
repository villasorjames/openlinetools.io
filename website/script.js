// Mobile Navigation Toggle
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');
const navClose = document.getElementById('nav-close');

// Toggle mobile menu
hamburger.addEventListener('click', () => {
  navMenu.classList.add('active');
  document.body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
});

navClose.addEventListener('click', () => {
  navMenu.classList.remove('active');
  document.body.style.overflow = 'auto'; // Restore scrolling
});

// Close menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('active');
    document.body.style.overflow = 'auto';
  });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
  if (!navMenu.contains(e.target) && !hamburger.contains(e.target) && navMenu.classList.contains('active')) {
    navMenu.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
});

// Testimonial Slider
const testimonialContents = document.querySelectorAll('.testimonial-content');
const dots = document.querySelectorAll('.dot');
const prevBtn = document.querySelector('.slider-btn-prev');
const nextBtn = document.querySelector('.slider-btn-next');
let currentSlide = 0;

// Function to update testimonial display
function updateTestimonial() {
  // Hide all testimonials
  testimonialContents.forEach(content => {
    content.classList.remove('active');
  });
  
  // Remove active class from all dots
  dots.forEach(dot => {
    dot.classList.remove('active');
  });
  
  // Show current testimonial and activate corresponding dot
  testimonialContents[currentSlide].classList.add('active');
  dots[currentSlide].classList.add('active');
}

// Next testimonial
function nextTestimonial() {
  currentSlide = (currentSlide + 1) % testimonialContents.length;
  updateTestimonial();
}

// Previous testimonial
function prevTestimonial() {
  currentSlide = (currentSlide - 1 + testimonialContents.length) % testimonialContents.length;
  updateTestimonial();
}

// Event listeners for buttons
nextBtn.addEventListener('click', nextTestimonial);
prevBtn.addEventListener('click', prevTestimonial);

// Event listeners for dots
dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    currentSlide = index;
    updateTestimonial();
  });
});

// Auto-rotate testimonials (every 5 seconds)
let testimonialInterval = setInterval(nextTestimonial, 5000);

// Pause auto-rotation on hover
const testimonialSlider = document.querySelector('.testimonial-slider');
testimonialSlider.addEventListener('mouseenter', () => {
  clearInterval(testimonialInterval);
});

testimonialSlider.addEventListener('mouseleave', () => {
  testimonialInterval = setInterval(nextTestimonial, 5000);
});

// Newsletter Form Submission
const subscribeForm = document.querySelector('.subscribe-form');
subscribeForm.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const emailInput = subscribeForm.querySelector('.subscribe-input');
  const email = emailInput.value.trim();
  
  if (email) {
    // In a real application, you would send this to a server
    alert(`Thank you for subscribing with email: ${email}`);
    emailInput.value = '';
    
    // Add success styling
    const subscribeBtn = subscribeForm.querySelector('.btn-subscribe');
    const originalText = subscribeBtn.innerHTML;
    
    subscribeBtn.innerHTML = '<i class="fas fa-check"></i> Subscribed!';
    subscribeBtn.style.background = '#4CAF50';
    
    setTimeout(() => {
      subscribeBtn.innerHTML = originalText;
      subscribeBtn.style.background = '';
    }, 2000);
  } else {
    alert('Please enter a valid email address.');
    emailInput.focus();
  }
});

// Smooth scrolling for anchor links
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

// Add scroll effect to navbar
window.addEventListener('scroll', () => {
  const header = document.querySelector('.header');
  if (window.scrollY > 100) {
    header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
    header.style.background = 'rgba(255, 255, 255, 0.95)';
  } else {
    header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    header.style.background = 'var(--white)';
  }
});

// Initialize the testimonial slider
updateTestimonial();