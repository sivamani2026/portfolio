import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace HTML visual block
old_visual = """      <div class="hero-visual">
        <div class="hero-3d-scene">
          <div class="orbital-ring"></div>
          <div class="hero-photo-wrapper">
            <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
          </div>
        </div>
      </div>"""

new_visual = """      <div class="hero-visual">
        <div class="hero-3d-scene">
          <div class="orbital-ring"></div>
          <div class="floating-geo float-cube"></div>
          <div class="floating-geo float-triangle"></div>
          <div class="floating-geo float-square"></div>
          <div class="hero-photo-wrapper">
            <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
          </div>
        </div>
      </div>"""
content = content.replace(old_visual, new_visual)

# Strip old 3D Overrides
start_idx = content.find("    /* 3D Hero Overrides & Additions */")
end_idx = content.find("  </style>", start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]

css_additions = """
    /* --- HERO CORRECTIONS --- */
    nav {
      max-width: 1500px;
      margin: 0 auto;
    }
    .nav-logo {
      display: inline-block !important;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-family: 'Inter', sans-serif;
      padding-left: 20px;
    }
    .hire-me-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: clamp(110px, 12vw, 140px);
      height: clamp(38px, 4vw, 46px);
      margin-left: 24px;
      border: 1px solid rgba(0, 255, 136, 0.5);
      background: rgba(0, 255, 136, 0.08);
      border-radius: 6px;
      color: var(--white);
      font-weight: 600;
      font-size: 13px;
      letter-spacing: 1px;
      transition: all 0.3s ease;
      box-shadow: 0 0 15px rgba(0, 255, 136, 0.15);
      text-decoration: none;
    }
    .hire-me-btn:hover {
      background: rgba(0, 255, 136, 0.2);
      box-shadow: 0 0 25px rgba(0, 255, 136, 0.4);
      transform: translateY(-2px);
    }
    .hero {
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      background-color: #080808;
    }
    .hero-bg-fx {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 75% 50%, rgba(0, 255, 136, 0.06) 0%, transparent 50%),
                  linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
                  linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
      background-size: 100% 100%, 60px 60px, 60px 60px;
      z-index: 0;
      pointer-events: none;
    }
    .hero-layout {
      position: relative;
      z-index: 1;
      width: min(94vw, 1500px) !important;
      max-width: none !important;
      margin: 0 auto;
      display: grid !important;
      grid-template-columns: 1.05fr 0.95fr !important;
      align-items: center;
      padding-top: 80px;
    }
    .hero-headline {
      font-size: clamp(4rem, 6vw, 7rem) !important;
      line-height: 0.95;
    }
    .hero-desc {
      font-family: 'Inter', sans-serif;
      font-size: 17px;
      color: var(--text-dim);
      line-height: 1.6;
      margin-top: 24px;
      max-width: 90%;
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
    
    /* Right Side 3D Scene */
    .hero-visual {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
    }
    .hero-3d-scene {
      perspective: 1200px;
      position: relative;
      width: clamp(340px, 40vw, 520px);
      aspect-ratio: 4/5;
    }
    .hero-photo-wrapper {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 2;
      border-radius: 12px;
      border: 1px solid rgba(0, 255, 136, 0.25);
      box-shadow: 0 20px 60px rgba(0, 255, 136, 0.15), inset 0 0 20px rgba(0,255,136,0.05);
      background: rgba(10, 10, 10, 0.8);
      overflow: hidden;
      transform-style: preserve-3d;
      transition: transform 0.1s ease-out;
      animation: floatingCard 6s ease-in-out infinite alternate;
      will-change: transform;
    }
    .hero-photo {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block;
    }
    
    /* 3D Elements */
    .orbital-ring {
      position: absolute;
      top: -15%; bottom: -15%; left: -15%; right: -15%;
      border: 1px solid rgba(0, 255, 136, 0.15);
      border-radius: 50%;
      box-shadow: 0 0 40px rgba(0, 255, 136, 0.1);
      animation: spinSlow 20s linear infinite;
      pointer-events: none;
      z-index: 1;
      transform-style: preserve-3d;
    }
    .floating-geo {
      position: absolute;
      z-index: 3;
      pointer-events: none;
      background: rgba(0, 255, 136, 0.1);
      backdrop-filter: blur(4px);
      border: 1px solid rgba(0, 255, 136, 0.3);
      box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
    }
    .float-cube {
      top: -20px; left: -20px;
      width: 50px; height: 50px;
      border-radius: 8px;
      animation: floatGeo1 7s ease-in-out infinite alternate;
    }
    .float-triangle {
      bottom: 10%; left: -40px;
      width: 0; height: 0;
      background: transparent;
      border-left: 30px solid transparent;
      border-right: 30px solid transparent;
      border-bottom: 50px solid rgba(0, 255, 136, 0.15);
      filter: drop-shadow(0 0 15px rgba(0,255,136,0.2));
      animation: floatGeo2 9s ease-in-out infinite alternate;
    }
    .float-square {
      bottom: -15px; right: -15px;
      width: 60px; height: 60px;
      border-radius: 12px;
      background: rgba(10, 10, 10, 0.9);
      animation: floatGeo3 8s ease-in-out infinite alternate;
    }
    
    @keyframes spinSlow {
      0% { transform: rotate3d(1, 1, 1, 0deg) scale(1); }
      50% { transform: rotate3d(1, 1, 1, 180deg) scale(1.05); }
      100% { transform: rotate3d(1, 1, 1, 360deg) scale(1); }
    }
    @keyframes floatingCard {
      0% { transform: translateY(-5px); }
      100% { transform: translateY(5px); }
    }
    @keyframes floatGeo1 {
      0% { transform: translateY(0) rotate(0deg); }
      100% { transform: translateY(-20px) rotate(25deg); }
    }
    @keyframes floatGeo2 {
      0% { transform: translateY(0) rotate(0deg); }
      100% { transform: translateY(25px) rotate(-20deg); }
    }
    @keyframes floatGeo3 {
      0% { transform: translateY(0) rotate(0deg); }
      100% { transform: translateY(-15px) rotate(15deg); }
    }

    /* Scroll Indicator */
    .scroll-indicator {
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      z-index: 5;
    }
    .scroll-indicator span {
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--text-dim);
    }
    .scroll-line {
      width: 1px;
      height: 40px;
      background: linear-gradient(to bottom, var(--green), transparent);
      animation: scrollPulse 2s infinite;
    }
    @keyframes scrollPulse {
      0% { transform: scaleY(0); transform-origin: top; opacity: 0; }
      50% { transform: scaleY(1); transform-origin: top; opacity: 1; }
      50.1% { transform: scaleY(1); transform-origin: bottom; opacity: 1; }
      100% { transform: scaleY(0); transform-origin: bottom; opacity: 0; }
    }

    @media (max-width: 1024px) {
      .hero-layout { grid-template-columns: 1fr 1fr !important; gap: 40px; }
      .hero-headline { font-size: clamp(3rem, 5vw, 5rem) !important; }
      .hero-3d-scene { width: clamp(280px, 40vw, 400px); }
    }
    @media (max-width: 768px) {
      .hero-layout { grid-template-columns: 1fr !important; text-align: center; }
      .hero-text { align-items: center; text-align: center; }
      .hero-desc { max-width: 100%; }
      .hero-cta { flex-direction: column; width: 100%; }
      .hero-3d-scene { width: clamp(280px, 70vw, 400px); margin: 40px auto; }
      .hero { min-height: auto; padding: 120px 0 60px; }
      .scroll-indicator { display: none; }
    }
    @media (prefers-reduced-motion: reduce) {
      .hero-photo-wrapper, .orbital-ring, .floating-geo {
        animation: none !important;
        transform: none !important;
      }
    }
  </style>
"""

content = content.replace("  </style>", css_additions)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied 3D Premium Hero Redesign Corections successfully.")
