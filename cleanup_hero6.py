import re

file_path = "index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Headline resize
content = content.replace("clamp(4rem, 6vw, 7rem) !important;", "clamp(3.8rem, 5.2vw, 6rem) !important;")
content = content.replace("clamp(3rem, 5vw, 5rem) !important;", "clamp(2.8rem, 4.5vw, 4.5rem) !important;") # adjust tablet

# 2. Portrait card sizing and z-index
old_card_css = """    .hero-3d-scene {
      perspective: 1200px;
      position: relative;
      width: clamp(340px, 40vw, 520px);
      aspect-ratio: 4/5;
    }"""
new_card_css = """    .hero-3d-scene {
      perspective: 1200px;
      position: relative;
      width: clamp(400px, 40vw, 500px);
      aspect-ratio: 4/5;
      z-index: 10;
    }"""
content = content.replace(old_card_css, new_card_css)

old_card_mq = """      .hero-3d-scene { width: clamp(280px, 40vw, 400px); }"""
new_card_mq = """      .hero-3d-scene { width: clamp(340px, 45vw, 450px); }"""
content = content.replace(old_card_mq, new_card_mq)

# 3. Fix photo wrapper opacity & visibility permanently!
old_wrapper = """    /* Premium Glass Neon Frame */
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
    }"""
new_wrapper = """    /* Premium Glass Neon Frame */
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
    }"""
content = content.replace(old_wrapper, new_wrapper)

# 4. Remove dark filters from photo so it's fully bright and opaque
old_photo = """    .hero-photo {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block;
      opacity: 0.9;
      filter: contrast(1.1) brightness(0.9);
      mix-blend-mode: luminosity;
    }"""
new_photo = """    .hero-photo {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block;
      opacity: 1 !important;
      visibility: visible !important;
    }"""
content = content.replace(old_photo, new_photo)

# 5. Send orbital ring to the back
old_orbit = """    .orbital-ring {
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
    }"""
new_orbit = """    .orbital-ring {
      position: absolute;
      top: 30%; bottom: 30%; left: -30%; right: -30%;
      border: 2px solid rgba(0, 255, 136, 0.6);
      border-radius: 50%;
      box-shadow: 0 0 25px rgba(0, 255, 136, 0.5), inset 0 0 15px rgba(0, 255, 136, 0.3);
      animation: spinOrbit 15s linear infinite;
      pointer-events: none;
      z-index: -1;
      transform: rotateX(70deg);
      transform-style: preserve-3d;
    }"""
content = content.replace(old_orbit, new_orbit)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Visibility and resize fixes applied successfully.")
