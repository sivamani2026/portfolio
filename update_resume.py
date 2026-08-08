import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Resume content
resume_pattern = re.compile(r'(<div class="resume-info reveal">.*?<h3>.*?</h3>\s*<p>)(.*?)(</p>\s*<h3>Education</h3>\s*<p>)(.*?)(</p>\s*<h3>Certifications</h3>\s*<p>)(.*?)(</p>)', re.DOTALL)
new_bio = "\n            B.Tech CSE (AI & ML) Student with a strong foundation in Python, Machine Learning, and Software Development. Passionate about creating intelligent systems that solve real-world problems. Experienced in working with modern web technologies, databases, and AI frameworks.\n          "
new_education = "\n            B.Tech in Computer Science (AI & ML)<br>\n            Kalasalingam Academy of Research and Education, 2028\n          "
new_certs = "\n            Machine Learning Training — Corizo (CRZ155377)<br>\n            Cloud Computing with AWS — Beeskilled (Upcoming)\n          "

content = resume_pattern.sub(r'\1' + new_bio + r'\3' + new_education + r'\5' + new_certs + r'\7', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated resume in index.html successfully.")
