import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace HTML structure
old_html = """  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-top">
        <div class="hero-year">B.Tech<br>Portfolio</div>
        <div class="hero-meta">
          Mannem Sivamani<br>
          Virudhunagar, Tamil Nadu, India<br>
          mannemsivamani06@gmail.com
        </div>
      </div>
      <h1 class="hero-headline">
        Building <em>Intelligent</em><br>
        <span class="outline">Systems</span> That<br>
        Solve Problems<span class="hero-dot"></span>
      </h1>
    </div>"""

new_html = """  <!-- HERO -->
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

content = content.replace(old_html, new_html)


# 2. Replace CSS structure
old_css_hero = """    /* HERO */
    .hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding-bottom: 60px;
      position: relative;
    }

    .hero-top {
      position: absolute;
      top: 140px;
      left: clamp(30px, 6vw, 120px);
      right: clamp(30px, 6vw, 120px);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }"""

new_css_hero = """    /* HERO */
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      padding-top: 120px;
      padding-bottom: 60px;
    }

    .hero-layout {
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
    }"""

content = content.replace(old_css_hero, new_css_hero)


# 3. Fix Headline margin
old_headline = """      color: var(--white);
      text-transform: uppercase;
      margin-bottom: 40px;
      opacity: 0;"""

new_headline = """      color: var(--white);
      text-transform: uppercase;
      margin: 0;
      opacity: 0;"""

content = content.replace(old_headline, new_headline)


# 4. Add Responsive Media Query rules for tablet/laptop
responsive_addition = """    @media (max-width: 1024px) {
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
    }

    @media (max-width: 768px) {"""

content = content.replace("    @media (max-width: 768px) {", responsive_addition)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Hero Layout fixes successfully.")
