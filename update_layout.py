import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .container max-width and padding
content = content.replace('''    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 clamp(20px, 5vw, 80px);
    }''', '''    .container {
      max-width: 1800px;
      margin: 0 auto;
      padding: 0 clamp(30px, 6vw, 120px);
    }''')

# 2. Update nav padding
content = content.replace('''    nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      padding: 24px clamp(20px, 5vw, 80px);
      display: flex;''', '''    nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      padding: 32px clamp(30px, 6vw, 120px);
      display: flex;''')

# 3. Update nav styling
content = content.replace('''    .nav-logo {
      font-size: 18px;''', '''    .nav-logo {
      font-size: 22px;''')

content = content.replace('''    .nav-links {
      display: flex;
      gap: 36px;''', '''    .nav-links {
      display: flex;
      gap: 48px;''')

content = content.replace('''    .nav-links a {
      font-size: 13px;''', '''    .nav-links a {
      font-size: 15px;''')

content = content.replace('''    .nav-number {
      font-size: 11px;''', '''    .nav-number {
      font-size: 12px;''')

# 4. Update hero top positioning and meta
content = content.replace('''    .hero-top {
      position: absolute;
      top: 120px;
      left: clamp(20px, 5vw, 80px);
      right: clamp(20px, 5vw, 80px);
      display: flex;''', '''    .hero-top {
      position: absolute;
      top: 140px;
      left: clamp(30px, 6vw, 120px);
      right: clamp(30px, 6vw, 120px);
      display: flex;''')

content = content.replace('''    .hero-meta {
      font-size: 13px;''', '''    .hero-meta {
      font-size: 15px;''')

content = content.replace('''    .hero-year {
      font-size: 13px;''', '''    .hero-year {
      font-size: 15px;''')

# 5. Update hero headline typography
content = content.replace('''    .hero-headline {
      font-family: 'Playfair Display', serif;
      font-size: clamp(42px, 8vw, 120px);
      font-weight: 700;
      line-height: 0.95;
      letter-spacing: -2px;''', '''    .hero-headline {
      font-family: 'Playfair Display', serif;
      font-size: clamp(52px, 9vw, 170px);
      font-weight: 700;
      line-height: 0.95;
      letter-spacing: -3px;''')

# 6. Update hero dot
content = content.replace('''    .hero-dot {
      display: inline-block;
      width: clamp(16px, 2.5vw, 40px);
      height: clamp(16px, 2.5vw, 40px);''', '''    .hero-dot {
      display: inline-block;
      width: clamp(18px, 3vw, 48px);
      height: clamp(18px, 3vw, 48px);''')

# 7. Update section padding
content = content.replace('''    /* SECTIONS */
    section {
      padding: 120px 0;
    }''', '''    /* SECTIONS */
    section {
      padding: clamp(120px, 15vh, 200px) 0;
    }''')

# 8. Update Javascript nav scroll logic
content = content.replace('''|| 'clamp(20px, 5vw, 80px)';''', '''|| 'clamp(30px, 6vw, 120px)';''')
content = content.replace('''nav.style.padding = '24px clamp(20px, 5vw, 80px)';''', '''nav.style.padding = '32px clamp(30px, 6vw, 120px)';''')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied UI/UX layout improvements.")
