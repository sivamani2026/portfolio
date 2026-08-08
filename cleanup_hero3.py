import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Nav HTML
old_nav = """    <a href="#" class="nav-logo" style="display: none;"></a>
    <div class="nav-links">
      <a href="#about">PROFILE</a>
      <a href="#work">EDUCATION</a>
      <a href="#skills">SKILLS</a>
      <a href="#resume">RESUME</a>
      <a href="#contact">✦ CONTACT</a>
    </div>"""

new_nav = """    <a href="#" class="nav-logo">SIVAMANI<span>.</span></a>
    <div class="nav-links">
      <a href="#about">PROFILE</a>
      <a href="#work">EDUCATION</a>
      <a href="#skills">SKILLS</a>
      <a href="#resume">RESUME</a>
      <a href="#contact">✦ CONTACT</a>
      <a href="#contact" class="hire-me-btn">HIRE ME ↗</a>
    </div>"""
content = content.replace(old_nav, new_nav)

# 2. Mobile Nav HTML
old_mobile = """  <div class="mobile-menu" id="mobileMenu">
    <a href="#about" onclick="toggleMenu()">Profile</a>
    <a href="#work" onclick="toggleMenu()">Education</a>
    <a href="#skills" onclick="toggleMenu()">Skills</a>
    <a href="#resume" onclick="toggleMenu()">Resume</a>
    <a href="#contact" onclick="toggleMenu()">Contact</a>
  </div>"""

new_mobile = """  <div class="mobile-menu" id="mobileMenu">
    <a href="#about" onclick="toggleMenu()">PROFILE</a>
    <a href="#work" onclick="toggleMenu()">EDUCATION</a>
    <a href="#skills" onclick="toggleMenu()">SKILLS</a>
    <a href="#resume" onclick="toggleMenu()">RESUME</a>
    <a href="#contact" onclick="toggleMenu()">CONTACT</a>
    <a href="#contact" onclick="toggleMenu()" style="color: var(--green);">HIRE ME ↗</a>
  </div>"""
content = content.replace(old_mobile, new_mobile)

# 3. Hero HTML
old_hero = """  <!-- HERO -->
  <section class="hero">
    <div class="container hero-layout">
      <div class="hero-text">
        <h1 class="hero-headline">
          Building <em>Intelligent</em><br>
          <span class="outline">Systems</span> That<br>
          Solve Problems<span class="hero-dot"></span>
        </h1>
      </div>
      <div class="hero-visual">
        <div class="hero-photo-wrapper">
          <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
        </div>
      </div>
    </div>"""

new_hero = """  <!-- HERO -->
  <section class="hero">
    <div class="hero-bg-fx"></div>
    <div class="container hero-layout">
      <div class="hero-text">
        <h1 class="hero-headline">
          Building <em>Intelligent</em><br>
          <span class="outline">Systems</span> That<br>
          Solve Problems<span class="hero-dot"></span>
        </h1>
        <p class="hero-desc">
          Computer Science & Engineering Student<br>
          Passionate about AI/ML, Full Stack Development<br>
          and building impactful solutions.
        </p>
        <div class="hero-cta">
          <a href="#work" class="btn-primary">EXPLORE MY WORK ↗</a>
          <a href="#resume" class="btn-secondary">DOWNLOAD RESUME ↓</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-3d-scene">
          <div class="orbital-ring"></div>
          <div class="hero-photo-wrapper">
            <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
          </div>
        </div>
      </div>
    </div>"""
content = content.replace(old_hero, new_hero)


# 4. CSS Additions
css_additions = """
    /* 3D Hero Overrides & Additions */
    .nav-logo {
      display: inline-block !important;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-family: 'Inter', sans-serif;
    }
    .hire-me-btn {
      display: inline-block;
      margin-left: 24px;
      padding: 10px 24px;
      border: 1px solid rgba(0, 255, 136, 0.4);
      background: rgba(0, 255, 136, 0.05);
      border-radius: 30px;
      color: var(--white);
      font-weight: 600;
      font-size: 13px;
      letter-spacing: 1px;
      transition: all 0.3s ease;
      box-shadow: 0 0 15px rgba(0, 255, 136, 0.1);
    }
    .hire-me-btn:hover {
      background: rgba(0, 255, 136, 0.15);
      box-shadow: 0 0 25px rgba(0, 255, 136, 0.3);
      transform: translateY(-2px);
    }
    .hero {
      position: relative;
    }
    .hero-bg-fx {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 70% 50%, rgba(0, 255, 136, 0.04) 0%, transparent 60%),
                  linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
                  linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      background-size: 100% 100%, 40px 40px, 40px 40px;
      z-index: 0;
      pointer-events: none;
    }
    .hero-layout {
      position: relative;
      z-index: 1;
    }
    .hero-desc {
      font-family: 'Inter', sans-serif;
      font-size: 18px;
      color: var(--text-dim);
      line-height: 1.6;
      margin-top: 24px;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeUp 1s ease forwards 0.5s;
    }
    .hero-cta {
      display: flex;
      gap: 16px;
      margin-top: 32px;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeUp 1s ease forwards 0.7s;
    }
    .btn-primary, .btn-secondary {
      padding: 14px 28px;
      border-radius: 4px;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 13px;
      letter-spacing: 1px;
      transition: all 0.3s ease;
      text-transform: uppercase;
      text-decoration: none;
    }
    .btn-primary {
      background: rgba(0, 255, 136, 0.1);
      border: 1px solid rgba(0, 255, 136, 0.5);
      color: var(--green);
      box-shadow: 0 4px 20px rgba(0, 255, 136, 0.15);
    }
    .btn-primary:hover {
      background: rgba(0, 255, 136, 0.2);
      transform: translateY(-3px);
      box-shadow: 0 6px 25px rgba(0, 255, 136, 0.25);
    }
    .btn-secondary {
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: var(--white);
    }
    .btn-secondary:hover {
      border-color: var(--white);
      transform: translateY(-3px);
      background: rgba(255,255,255,0.05);
    }
    .hero-3d-scene {
      perspective: 1000px;
      position: relative;
      width: clamp(260px, 30vw, 360px);
    }
    .orbital-ring {
      position: absolute;
      top: -30px; bottom: -30px; left: -30px; right: -30px;
      border: 1px solid rgba(0, 255, 136, 0.2);
      border-radius: 50%;
      box-shadow: 0 0 30px rgba(0, 255, 136, 0.05);
      animation: spinSlow 20s linear infinite;
      pointer-events: none;
      z-index: 0;
    }
    @keyframes spinSlow {
      0% { transform: rotate(0deg) scale(1); opacity: 0.3; }
      50% { transform: rotate(180deg) scale(1.05); opacity: 0.8; }
      100% { transform: rotate(360deg) scale(1); opacity: 0.3; }
    }
    .hero-photo-wrapper {
      position: relative;
      z-index: 1;
      width: 100% !important;
      margin: 0 !important;
      transform-style: preserve-3d;
      transition: transform 0.1s ease-out;
      animation: floatingCard 6s ease-in-out infinite alternate;
      background: rgba(10, 10, 10, 0.5);
    }
    @keyframes floatingCard {
      0% { transform: translateY(0px); }
      100% { transform: translateY(-20px); }
    }
    @media (max-width: 1024px) {
      .hero-desc { font-size: 16px; }
      .hero-cta { flex-direction: column; width: 100%; }
      .btn-primary, .btn-secondary { text-align: center; }
      .hero-3d-scene { width: clamp(220px, 40vw, 300px); }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-photo-wrapper, .orbital-ring {
        animation: none !important;
        transform: none !important;
      }
    }
  </style>
"""
content = content.replace("  </style>", css_additions)

# 5. JS Additions
js_additions = """
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
"""
content = content.replace("  </script>", js_additions)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied 3D Premium Hero Redesign successfully.")
