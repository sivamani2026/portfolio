import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace HTML
old_visual = """      <div class="hero-visual">
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

new_visual = """      <div class="hero-visual">
        <div class="hero-3d-scene">
          <div class="orbital-ring"></div>
          
          <div class="orbit-anchor anchor-cube">
            <div class="floating-geo float-cube"></div>
          </div>
          
          <div class="orbit-anchor anchor-triangle">
            <div class="floating-geo float-triangle"></div>
          </div>

          <div class="hero-photo-wrapper">
            <img src="profile.jpg" alt="Mannem Sivamani" class="hero-photo">
          </div>
        </div>
      </div>"""

content = content.replace(old_visual, new_visual)

# Replace CSS block
start_idx = content.find("    /* Right Side 3D Scene */")
end_idx = content.find("    /* Scroll Indicator */")

new_css = """    /* Right Side 3D Scene */
    .hero-visual {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
    }
    .hero-3d-scene {
      perspective: 1400px;
      position: relative;
      width: clamp(400px, 40vw, 500px);
      aspect-ratio: 4/5;
      z-index: 10;
      margin-top: clamp(40px, 5vw, 70px);
      transform-style: preserve-3d;
    }
    
    /* Premium Glass Neon Frame */
    .hero-photo-wrapper {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 10;
      border-radius: 20px;
      border: 2px solid rgba(0, 255, 136, 0.8);
      box-shadow: 0 0 40px rgba(0, 255, 136, 0.4), inset 0 0 40px rgba(0, 255, 136, 0.3);
      background: rgba(5, 5, 5, 0.6);
      backdrop-filter: blur(10px);
      overflow: hidden;
      transform-style: preserve-3d;
      transition: transform 0.1s ease-out;
      animation: floatingCard 6s ease-in-out infinite alternate;
      will-change: transform;
      opacity: 1 !important;
      visibility: visible !important;
      transform: translateZ(0); /* Anchor to Z=0 */
    }
    
    /* Glass Reflection Overlay */
    .hero-photo-wrapper::after {
      content: '';
      position: absolute;
      top: -50%; left: -50%; right: -50%; bottom: -50%;
      background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0) 40%, rgba(255,255,255,0) 100%);
      transform: rotate(15deg);
      pointer-events: none;
      z-index: 3;
    }
    
    .hero-photo {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block;
      opacity: 1 !important;
      visibility: visible !important;
    }

    /* 3D Orbit Track */
    .orbital-ring {
      position: absolute;
      top: -15%; bottom: -15%; left: -25%; right: -25%;
      border: 2px solid rgba(0, 255, 136, 0.3);
      border-radius: 50%;
      box-shadow: 0 0 25px rgba(0, 255, 136, 0.2), inset 0 0 15px rgba(0, 255, 136, 0.1);
      pointer-events: none;
      transform: translateZ(-80px) rotateX(65deg);
      transform-style: preserve-3d;
      z-index: -1;
    }

    /* 3D Floating Geometrics Anchors */
    .orbit-anchor {
      position: absolute;
      top: 50%; left: 50%;
      width: 0; height: 0;
      transform-style: preserve-3d;
      z-index: 5;
    }
    
    .anchor-cube {
      animation: orbitY1 12s linear infinite;
    }
    
    .anchor-triangle {
      animation: orbitY2 16s linear infinite;
    }
    
    @keyframes orbitY1 {
      0% { transform: rotateX(-15deg) rotateY(0deg); }
      100% { transform: rotateX(-15deg) rotateY(360deg); }
    }
    
    @keyframes orbitY2 {
      0% { transform: rotateX(20deg) rotateY(180deg); }
      100% { transform: rotateX(20deg) rotateY(540deg); }
    }

    /* The Objects inside the anchors */
    .floating-geo {
      position: absolute;
      pointer-events: none;
      background: rgba(10, 10, 10, 0.8);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(0, 255, 136, 0.6);
      box-shadow: 0 0 20px rgba(0, 255, 136, 0.3), inset 0 0 10px rgba(0, 255, 136, 0.2);
      transform-style: preserve-3d;
    }
    
    .float-cube {
      transform: translateZ(350px) rotateX(45deg) rotateY(45deg);
      width: 60px; height: 60px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(0,255,136,0.2) 0%, rgba(10,10,10,0.9) 100%);
      margin-top: -30px; margin-left: -30px;
    }
    
    .float-triangle {
      transform: translateZ(300px) rotateX(15deg);
      width: 50px; height: 50px;
      background: linear-gradient(to bottom, rgba(0,255,136,0.4), rgba(10,10,10,0.9));
      clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
      border: none;
      filter: drop-shadow(0 0 20px rgba(0,255,136,0.4));
      margin-top: -25px; margin-left: -25px;
    }

    @keyframes floatingCard {
      0% { transform: translateZ(0) translateY(-6px); }
      100% { transform: translateZ(0) translateY(6px); }
    }

"""

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_css + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied TRUE 3D orbit system successfully.")
