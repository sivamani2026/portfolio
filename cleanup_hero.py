import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. HTML: Remove nav numbers
old_nav_links = """    <div class="nav-links">
      <a href="#about"><span class="nav-number">01.</span>Profile</a>
      <a href="#work"><span class="nav-number">02.</span>Education</a>
      <a href="#skills"><span class="nav-number">03.</span>Skills</a>
      <a href="#resume"><span class="nav-number">04.</span>Resume</a>
      <a href="#contact" class="contact-btn">
        <span class="nav-number">+</span> Contact
      </a>
    </div>"""

new_nav_links = """    <div class="nav-links">
      <a href="#about">Profile</a>
      <a href="#work">Education</a>
      <a href="#skills">Skills</a>
      <a href="#resume">Resume</a>
      <a href="#contact" class="contact-btn">Contact</a>
    </div>"""
content = content.replace(old_nav_links, new_nav_links)

# HTML: Remove mobile menu numbers
old_mobile_menu = """    <div class="mobile-menu">
      <a href="#about">01. Profile</a>
      <a href="#work">02. Education</a>
      <a href="#skills">03. Skills</a>
      <a href="#resume">04. Resume</a>
      <a href="#contact">+ Contact</a>
    </div>"""

new_mobile_menu = """    <div class="mobile-menu">
      <a href="#about">Profile</a>
      <a href="#work">Education</a>
      <a href="#skills">Skills</a>
      <a href="#resume">Resume</a>
      <a href="#contact">Contact</a>
    </div>"""
content = content.replace(old_mobile_menu, new_mobile_menu)

# 2. HTML: Clean Hero structure
old_hero_html = """  <!-- HERO -->
  <section class="hero">
    <div class="container hero-layout">
      <div class="hero-left">
        <div class="hero-year">B.Tech<br>Portfolio</div>
      </div>
      
      <div class="hero-center">
        <div class="hero-photo-wrapper">
          <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
        </div>
        <h1 class="hero-headline">
          Building <em>Intelligent</em><br>
          <span class="outline">Systems</span> That<br>
          Solve Problems<span class="hero-dot"></span>
        </h1>
      </div>
      
      <div class="hero-right">
        <div class="hero-meta">
          Mannem Sivamani<br>
          Virudhunagar, Tamil Nadu, India<br>
          mannemsivamani06@gmail.com
        </div>
      </div>
    </div>"""

new_hero_html = """  <!-- HERO -->
  <section class="hero">
    <div class="container hero-layout">
      <div class="hero-center">
        <div class="hero-photo-wrapper">
          <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
        </div>
        <h1 class="hero-headline">
          Building <em>Intelligent</em><br>
          <span class="outline">Systems</span> That<br>
          Solve Problems<span class="hero-dot"></span>
        </h1>
      </div>
    </div>"""
content = content.replace(old_hero_html, new_hero_html)

# 3. CSS: Update hero layout and remove obsolete classes
old_css_hero = """    .hero-layout {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      width: 100%;
    }

    .hero-left {
      display: flex;
      justify-content: flex-start;
    }

    .hero-right {
      display: flex;
      justify-content: flex-end;
    }

    .hero-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 32px;
    }

    .hero-photo-wrapper {
      width: clamp(140px, 15vw, 240px);
      aspect-ratio: 1/1;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid rgba(0, 255, 136, 0.2);
      box-shadow: 0 0 30px rgba(0, 255, 136, 0.1);
      margin: 0 auto;
      animation: fadeUp 1s ease forwards 0.1s;
      opacity: 0;
      transform: translateY(40px);
    }

    .hero-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .hero-meta {
      font-size: clamp(18px, 2vw, 32px);
      color: var(--text-dim);
      line-height: 1.8;
      text-align: right;
    }

    .hero-year {
      font-size: clamp(18px, 2vw, 32px);
      color: var(--text-dim);
    }"""

new_css_hero = """    .hero-layout {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
    }

    .hero-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 32px;
    }

    .hero-photo-wrapper {
      width: clamp(140px, 15vw, 240px);
      aspect-ratio: 1/1;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid rgba(0, 255, 136, 0.2);
      box-shadow: 0 0 30px rgba(0, 255, 136, 0.1);
      margin: 0 auto;
      animation: fadeUp 1s ease forwards 0.1s;
      opacity: 0;
      transform: translateY(40px);
    }

    .hero-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }"""
content = content.replace(old_css_hero, new_css_hero)

# 4. CSS: Remove nav-number class
old_nav_number_css = """    .nav-number {
      font-size: 12px;
      color: var(--text-dim);
      margin-right: 4px;
    }

"""
content = content.replace(old_nav_number_css, "")

# 5. CSS: Update media queries
old_media_query = """    @media (max-width: 1024px) {
      .hero-layout {
        grid-template-columns: 1fr;
        gap: 40px;
        text-align: center;
      }
      .hero-left, .hero-right {
        justify-content: center;
      }
      .hero-meta {
        text-align: center;
      }
    }"""

new_media_query = """    @media (max-width: 1024px) {
      .hero-layout {
        gap: 40px;
        text-align: center;
      }
    }"""
content = content.replace(old_media_query, new_media_query)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Final Hero Cleanup successfully.")
