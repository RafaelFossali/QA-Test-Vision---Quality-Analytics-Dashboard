import csv
from jinja2 import Template

def carregar_dados(caminho_csv):
    dados = {}
    with open(caminho_csv, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for categoria, quantidade in reader:
            dados[categoria] = quantidade
    return dados

def gerar_html(sprint, dados):
    with open("templates/report_template.html", "r", encoding="utf-8") as file:
        template = Template(file.read())

    html = template.render(sprint=sprint, dados=dados)

    output_path = f"output/{sprint}_report.html"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Relatório gerado em: {output_path}")

if __name__ == "__main__":
    sprint = "Sprint_1"
    dados = carregar_dados("data/sprint_1.csv")
    gerar_html(sprint, dados)
