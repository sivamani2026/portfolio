import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_html = """  <!-- HERO -->
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

new_html = """  <!-- HERO -->
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

old_css = """    .hero-layout {
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
    }"""

new_css = """    .hero-layout {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      align-items: center;
      gap: 4vw;
      width: 100%;
    }

    .hero-text {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }

    .hero-visual {
      display: flex;
      justify-content: flex-end;
    }

    .hero-photo-wrapper {
      width: clamp(260px, 30vw, 360px);
      aspect-ratio: 4/5;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(0, 255, 136, 0.15);
      box-shadow: 0 10px 40px rgba(0, 255, 136, 0.05);
      margin: 0 auto;
      animation: fadeUp 1s ease forwards 0.1s;
      opacity: 0;
      transform: translateY(40px);
    }"""

old_mq1 = """    @media (max-width: 1024px) {
      .hero-layout {
        gap: 40px;
        text-align: center;
      }
    }"""

new_mq1 = """    @media (max-width: 1024px) {
      .hero-layout {
        grid-template-columns: 1fr 1fr;
        gap: 24px;
      }
    }"""

old_mq2 = """    @media (max-width: 768px) {
      .nav-links {"""

new_mq2 = """    @media (max-width: 768px) {
      .hero-layout {
        grid-template-columns: 1fr;
        text-align: center;
      }
      .hero-text {
        align-items: center;
        text-align: center;
        order: 1;
      }
      .hero-visual {
        justify-content: center;
        order: 2;
        margin-top: 32px;
      }
      .hero-photo-wrapper {
        width: clamp(220px, 70vw, 300px);
      }
      .nav-links {"""

content = content.replace(old_html, new_html)
content = content.replace(old_css, new_css)
content = content.replace(old_mq1, new_mq1)
content = content.replace(old_mq2, new_mq2)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Asymmetrical Layout successfully.")
