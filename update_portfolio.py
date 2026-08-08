import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Only keep the first HTML document (in case of duplication)
html_end = content.find("</html>")
if html_end != -1:
    content = content[:html_end + 7]

# 1. Global text replacements
content = content.replace("Arun Singh", "Mannem Sivamani")
content = content.replace("arunsingh.work05@gmail.com", "mannemsivamani06@gmail.com")
content = content.replace("Delhi, India", "Virudhunagar, Tamil Nadu, India")
content = content.replace("UI/UX Designer", "AI & ML Student / Developer")
content = content.replace("UI/UX designer", "B.Tech CSE (AI & ML) Student")
content = content.replace("arun<span>.</span>", "siva<span>.</span>")
content = content.replace("2026<br>Portfolio", "B.Tech<br>Portfolio")
content = content.replace("<title>Mannem Sivamani — AI & ML Student / Developer</title>", "<title>Mannem Sivamani — Portfolio</title>")
content = content.replace("Crafting <em>Interfaces</em><br>\n        <span class=\"outline\">& Experiences</span> That<br>\n        Feel Effortless", "Building <em>Intelligent</em><br>\n        <span class=\"outline\">Systems</span> That<br>\n        Solve Problems")

# 2. Update About Section
about_pattern = re.compile(r'(<section id="about">.*?<p class="about-text">)(.*?)(</p>.*?</section>)', re.DOTALL)
new_about_text = "\n            I'm a <strong>B.Tech CSE (AI & ML) Student</strong> based in Virudhunagar with a strong passion for <strong>Python Development</strong> and <strong>Machine Learning</strong>. With a foundation in Artificial Intelligence and Data Science, I focus on building practical systems and learning by doing.<br><br>\n            My approach blends analytical thinking with active exploration — from writing efficient Python scripts to training machine learning models, I believe great software should be intuitive and solve real-world problems.\n          "
content = about_pattern.sub(r'\1' + new_about_text + r'\3', content)

# 3. Update Skills Cards in About Section
skills_cards = """<div class="skill-card" style="transition-delay: 0.1s;">
            <div class="skill-card-icon">◎</div>
            <h4>Python Development</h4>
            <p>Building efficient backends, scripts, and automation tools.</p>
          </div>
          <div class="skill-card" style="transition-delay: 0.2s;">
            <div class="skill-card-icon">◐</div>
            <h4>Machine Learning</h4>
            <p>Training and evaluating predictive models.</p>
          </div>
          <div class="skill-card" style="transition-delay: 0.3s;">
            <div class="skill-card-icon">△</div>
            <h4>Data Science</h4>
            <p>Extracting insights from complex datasets.</p>
          </div>
          <div class="skill-card" style="transition-delay: 0.4s;">
            <div class="skill-card-icon">⬡</div>
            <h4>Web Development</h4>
            <p>Creating responsive interfaces with HTML, CSS, JS.</p>
          </div>"""
content = re.sub(r'<div class="skills-cards">.*?</div>\s*</div>\s*</div>\s*</section>', f'<div class="skills-cards">\n{skills_cards}\n</div>\n</div>\n</div>\n</section>', content, flags=re.DOTALL)


# 4. Replace Work/Case Studies with Education & Experience
work_section = """<!-- EDUCATION & TRAINING -->
  <section id="work">
    <div class="container">
      <div class="section-label reveal">Journey</div>
      <h2 class="section-title reveal">Education & Training</h2>
      <div class="work-list">

        <!-- Education 1 -->
        <div class="work-item reveal" onclick="toggleCaseStudy(0)">
          <div class="work-item-header">
            <div class="work-item-left">
              <div class="work-item-number">01</div>
              <div class="work-item-title">B.Tech – Computer Science (AI & ML)</div>
              <div class="work-item-tags">
                <span class="tag">Kalasalingam Academy</span>
                <span class="tag">Aug 2024 - Jul 2028</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Education 2 -->
        <div class="work-item reveal" onclick="toggleCaseStudy(1)">
          <div class="work-item-header">
            <div class="work-item-left">
              <div class="work-item-number">02</div>
              <div class="work-item-title">Intermediate – MPC</div>
              <div class="work-item-tags">
                <span class="tag">Sri Chaitanya College</span>
                <span class="tag">Jun 2022 - Apr 2024</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Training 1 -->
        <div class="work-item reveal" onclick="toggleCaseStudy(2)">
          <div class="work-item-header">
            <div class="work-item-left">
              <div class="work-item-number">03</div>
              <div class="work-item-title">Machine Learning Training (Corizo)</div>
              <div class="work-item-tags">
                <span class="tag">07 May 2026 - 04 Jun 2026</span>
                <span class="tag">Cert ID: CRZ155377</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Internship 1 -->
        <div class="work-item reveal" onclick="toggleCaseStudy(3)">
          <div class="work-item-header">
            <div class="work-item-left">
              <div class="work-item-number">04</div>
              <div class="work-item-title">Cloud Computing with AWS (Beeskilled)</div>
              <div class="work-item-tags">
                <span class="tag">Upcoming Internship</span>
                <span class="tag">04 Aug 2026 - 15 Sep 2026</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>"""
content = re.sub(r'<!-- WORK -->.*?</section>', work_section, content, flags=re.DOTALL)


# 5. Update Skills Section
skills_grid = """<div class="skills-grid">
        <div class="skill-item reveal">
          <div class="skill-item-icon">🐍</div>
          <h4>Python</h4>
          <p>Core Language</p>
        </div>
        <div class="skill-item reveal">
          <div class="skill-item-icon">🤖</div>
          <h4>Artificial Intelligence</h4>
          <p>Concepts & Apps</p>
        </div>
        <div class="skill-item reveal">
          <div class="skill-item-icon">🧠</div>
          <h4>Machine Learning</h4>
          <p>Model Training</p>
        </div>
        <div class="skill-item reveal">
          <div class="skill-item-icon">🗄️</div>
          <h4>SQL</h4>
          <p>Database</p>
        </div>
        <div class="skill-item reveal">
          <div class="skill-item-icon">💻</div>
          <h4>HTML/CSS/JS</h4>
          <p>Web Development</p>
        </div>
        <div class="skill-item reveal">
          <div class="skill-item-icon">📦</div>
          <h4>Git & GitHub</h4>
          <p>Version Control</p>
        </div>
      </div>"""
content = re.sub(r'<div class="skills-grid">.*?</div>\s*</div>\s*</section>', f'{skills_grid}\n    </div>\n  </section>', content, flags=re.DOTALL)

# 6. Update Nav Link
content = content.replace('<a href="#work"><span class="nav-number">02.</span>Work</a>', '<a href="#work"><span class="nav-number">02.</span>Education</a>')
content = content.replace('<a href="#work" onclick="toggleMenu()">Work</a>', '<a href="#work" onclick="toggleMenu()">Education</a>')


# 7. Update Contact Phone and Email explicitly
contact_section_pattern = re.compile(r'(<section id="contact">.*?</form>\s*<div class="contact-info reveal">\s*<p>)(.*?)(</p>)', re.DOTALL)
new_contact_text = "\n            I'm currently looking for internships and project collaborations in AI/ML and software development. Whether you have an opportunity or just want to connect, feel free to reach out.<br><br>\n            <strong>Email:</strong> mannemsivamani06@gmail.com<br>\n            <strong>Phone:</strong> +91 9701947061\n          "
content = contact_section_pattern.sub(r'\1' + new_contact_text + r'\3', content)

# Update LinkedIn link
content = re.sub(r'<a href="#" class="social-link">\s*<span class="social-link-icon">.*?</span>\s*LinkedIn\s*</a>', r'<a href="https://linkedin.com/in/mannem-sivamani-280b293b3" target="_blank" class="social-link"><span class="social-link-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-4 0v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg></span>LinkedIn</a>', content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully.")
