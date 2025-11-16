import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
import os

# Caminhos
DATA_PATH = "data/bugs_sprint_15.csv"
TEMPLATE_PATH = "templates"
OUTPUT_PATH = "output/sprint15_report.html"

# Carrega dados
df = pd.read_csv(DATA_PATH)

# Estatísticas básicas
total = len(df)
corrigidos = len(df[df['status'] == 'Corrigido'])
pendentes = len(df[df['status'] == 'Pendente'])
despriorizados = len(df[df['status'] == 'Despriorizado'])
outros_times = len(df[df['time_responsavel'] != 'Time A'])  # exemplo

# Gera gráfico
plt.figure(figsize=(6, 6))
status_counts = df['status'].value_counts()
status_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Status dos Bugs')
plt.ylabel('')
plt.tight_layout()
chart_path = "output/bugs_status_chart.png"
plt.savefig(chart_path)
plt.close()

# Carrega template HTML
env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
template = env.get_template('report_template.html')

# Renderiza HTML
html_content = template.render(
    sprint="Sprint 15",
    total=total,
    corrigidos=corrigidos,
    pendentes=pendentes,
    despriorizados=despriorizados,
    outros_times=outros_times,
    chart_path=chart_path,
    tabela=df.to_html(index=False, classes='table table-striped')
)

# Salva saída
os.makedirs("output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Relatório gerado em: {OUTPUT_PATH}")

# --- NOVO: Gráfico de tendência histórica ---
historico = pd.read_csv("data/historico_bugs.csv")

plt.figure(figsize=(8, 5))
plt.plot(historico['sprint'], historico['corrigidos'], marker='o', label='Corrigidos')
plt.plot(historico['sprint'], historico['pendentes'], marker='o', label='Pendentes')
plt.plot(historico['sprint'], historico['despriorizados'], marker='o', label='Despriorizados')
plt.title("Tendência de Bugs por Sprint")
plt.xlabel("Sprint")
plt.ylabel("Quantidade de Bugs")
plt.legend()
plt.grid(True)
tendencia_path = "output/bugs_trend_chart.png"
plt.savefig(tendencia_path)
plt.close()

# Atualiza o template renderizado
html_content = template.render(
    sprint="Sprint 15",
    total=total,
    corrigidos=corrigidos,
    pendentes=pendentes,
    despriorizados=despriorizados,
    outros_times=outros_times,
    chart_path=chart_path,
    tendencia_path=tendencia_path,
    tabela=df.to_html(index=False, classes='table table-striped')
)

from weasyprint import HTML

pdf_output = OUTPUT_PATH.replace(".html", ".pdf")
HTML(OUTPUT_PATH).write_pdf(pdf_output)

print(f"📄 PDF gerado: {pdf_output}")


