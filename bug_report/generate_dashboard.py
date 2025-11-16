from jinja2 import Template
import os
# Dados que futuramente virão dos CSV
s1 = {
    "ios": 7,
    "android": 5,
    "web": 5,
    "corrigidos_ios": 6,
    "corrigidos_android": 5,
    "corrigidos_web": 3
}

s2 = {
    "ios": 7,
    "android": 5,
    "web": 5,
    "corrigidos_ios": 6,
    "corrigidos_android": 5,
    "corrigidos_web": 3
}


base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, "templates", "dashboard_template.html")

with open(template_path, "r", encoding="utf-8") as f:

    template = Template(f.read())

with open("output/dashboard_sprints.html", "w", encoding="utf-8") as f:
    f.write(template.render(dados_sprint1=s1, dados_sprint2=s2))

print("Dashboard gerada com sucesso!")
