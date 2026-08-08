import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We will replace the CSS block for the 3D elements to match the new neon glass aesthetic.

old_css = """    /* Right Side 3D Scene */
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
    }"""

new_css = """    /* Right Side 3D Scene */
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
    
    /* Premium Glass Neon Frame */
    .hero-photo-wrapper {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 2;
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
      opacity: 0.9;
      filter: contrast(1.1) brightness(0.9);
      mix-blend-mode: luminosity;
    }
    
    /* 3D Elements */
    .orbital-ring {
      position: absolute;
      top: 30%; bottom: 30%; left: -30%; right: -30%;
      border: 2px solid rgba(0, 255, 136, 0.6);
      border-radius: 50%;
      box-shadow: 0 0 25px rgba(0, 255, 136, 0.5), inset 0 0 15px rgba(0, 255, 136, 0.3);
      animation: spinOrbit 15s linear infinite;
      pointer-events: none;
      z-index: 1;
      transform: rotateX(70deg);
      transform-style: preserve-3d;
    }
    @keyframes spinOrbit {
      0% { transform: rotateX(70deg) rotateZ(0deg); }
      100% { transform: rotateX(70deg) rotateZ(360deg); }
    }
    
    .floating-geo {
      position: absolute;
      z-index: 3;
      pointer-events: none;
      background: rgba(10, 10, 10, 0.8);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(0, 255, 136, 0.6);
      box-shadow: 0 0 20px rgba(0, 255, 136, 0.3), inset 0 0 10px rgba(0, 255, 136, 0.2);
    }
    
    /* Neon Dark Glass Cube */
    .float-cube {
      top: -30px; left: -40px;
      width: 70px; height: 70px;
      border-radius: 12px;
      animation: floatGeo1 8s ease-in-out infinite alternate;
      background: linear-gradient(135deg, rgba(0,255,136,0.2) 0%, rgba(10,10,10,0.9) 100%);
    }
    
    /* Glowing Pyramid Shape */
    .float-triangle {
      bottom: 5%; left: -50px;
      width: 60px; height: 60px;
      background: linear-gradient(to bottom, rgba(0,255,136,0.4), rgba(10,10,10,0.9));
      clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
      border: none;
      filter: drop-shadow(0 0 20px rgba(0,255,136,0.4));
      animation: floatGeo2 9s ease-in-out infinite alternate;
    }
    
    /* Lower Right Dark Glass Cube */
    .float-square {
      bottom: -20px; right: -30px;
      width: 80px; height: 80px;
      border-radius: 16px;
      background: linear-gradient(135deg, rgba(10,10,10,0.95) 0%, rgba(0,255,136,0.15) 100%);
      animation: floatGeo3 7s ease-in-out infinite alternate;
    }"""

content = content.replace(old_css, new_css)


old_bg = """    .hero-bg-fx {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 75% 50%, rgba(0, 255, 136, 0.06) 0%, transparent 50%),
                  linear-gradient(rgba(255, 255, 255, 0.01) 1px, transparent 1px),
                  linear-gradient(90deg, rgba(255, 255, 255, 0.01) 1px, transparent 1px);
      background-size: 100% 100%, 60px 60px, 60px 60px;
      z-index: 0;
      pointer-events: none;
    }"""

new_bg = """    /* Cyberpunk Perspective Floor Grid */
    .hero-bg-fx {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 75% 50%, rgba(0, 255, 136, 0.1) 0%, transparent 60%);
      z-index: 0;
      pointer-events: none;
      perspective: 1000px;
      overflow: hidden;
    }
    .hero-bg-fx::after {
      content: '';
      position: absolute;
      bottom: -50%; left: -50%; right: -50%; height: 100%;
      background: 
        linear-gradient(rgba(0, 255, 136, 0.15) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 136, 0.15) 1px, transparent 1px);
      background-size: 80px 80px;
      transform: rotateX(75deg);
      mask-image: linear-gradient(to top, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%);
      -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%);
    }"""

content = content.replace(old_bg, new_bg)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Neon Glass 3D Effect successfully.")
