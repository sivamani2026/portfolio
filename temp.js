  <script>
    // Scroll Reveal
    const revealElements = document.querySelectorAll('.reveal, .skill-card');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealElements.forEach(el => observer.observe(el));

    // Case Study Toggle
    function toggleCaseStudy(index) {
      const detail = document.getElementById('cs' + index);
      const allDetails = document.querySelectorAll('.case-study-detail');

      allDetails.forEach((d, i) => {
        if (i !== index) d.classList.remove('open');
      });

      detail.classList.toggle('open');
    }

    // Mobile Menu
    function toggleMenu() {
      const menu = document.getElementById('mobileMenu');
      const hamburger = document.querySelector('.hamburger');
      menu.classList.toggle('active');

      const spans = hamburger.querySelectorAll('span');
      if (menu.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(4px, 4px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(4px, -4px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    }

    // Form Submit
    async function handleSubmit(e) {
      e.preventDefault();
      
      const form = e.target;
      const btn = form.querySelector('button[type="submit"]');
      const btnText = btn.querySelector('span');
      const messageContainer = document.getElementById('formMessage');
      
      const originalHTML = btn.innerHTML;
      
      // Get values
      const name = document.getElementById('contactName').value;
      const email = document.getElementById('contactEmail').value;
      const message = document.getElementById('contactMessage').value;
      const honey = document.getElementById('_honey').value;
      
      // Update UI to sending state
      if(btnText) btnText.innerText = 'SENDING...';
      btn.style.opacity = '0.7';
      btn.style.pointerEvents = 'none';
      messageContainer.innerText = '';
      
      try {
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            name: name,
            email: email,
            message: message,
            _honey: honey
          })
        });
        
        const result = await response.json();
        
        console.log("CONTACT RESPONSE:", {
          status: response.status,
          ok: response.ok,
          result
        });
        
        if (!response.ok || result.success !== true) {
          throw new Error(result.message || "Failed to send message.");
        }

        messageContainer.innerText = "Message sent successfully. I'll get back to you soon.";
        messageContainer.style.color = "var(--green)";
        form.reset();
      } catch (error) {
        console.error('Error:', error);
        messageContainer.innerText = "Something went wrong. Please try again or email me directly.";
        messageContainer.style.color = "#ff4444";
      } finally {
        btn.innerHTML = originalHTML;
        btn.style.opacity = '1';
        btn.style.pointerEvents = 'auto';
      }
    }

    // Smooth anchor scroll offset for fixed nav
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          const offset = 80;
          const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    });

    // Parallax-style nav shrink
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const nav = document.querySelector('nav');
      if (window.scrollY > 50) {
        nav.style.background = 'rgba(13, 13, 13, 0.9)';
        nav.style.backdropFilter = 'blur(10px)';
        nav.style.padding = '16px ' + getComputedStyle(document.documentElement).getPropertyValue('--nav-px') || 'clamp(20px, 2vw, 40px)';
        nav.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.1)';
      } else {
        nav.style.background = 'transparent';
        nav.style.backdropFilter = 'none';
        nav.style.mixBlendMode = 'difference';
      }
      lastScroll = window.scrollY;
    });

    // 3D Tilt Effect for Hero Photo
    const scene = document.querySelector('.hero');
    const card = document.querySelector('.hero-photo-wrapper');
    if (scene && card && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      scene.addEventListener('mousemove', (e) => {
        const rect = scene.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = ((y - centerY) / centerY) * -15;
        const rotateY = ((x - centerX) / centerX) * 15;
        
        card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      });
      scene.addEventListener('mouseleave', () => {
        card.style.transform = `rotateX(0deg) rotateY(0deg)`;
        card.style.transition = 'transform 0.5s ease-out';
      });
      scene.addEventListener('mouseenter', () => {
        card.style.transition = 'transform 0.1s ease-out';
      });
    }
  </script>
