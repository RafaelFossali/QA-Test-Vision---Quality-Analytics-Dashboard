import requests
import csv

# CONFIGURAÇÕES
GITLAB_URL = "https://gitlab.com"  # ou sua instância privada
PROJECT_ID = 12345678
TOKEN = "SEU_TOKEN_AQUI"

# URL da API
issues_url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/issues"

# Cabeçalhos
headers = {
    "PRIVATE-TOKEN": TOKEN
}

# Parâmetros (opcionalmente filtre por label)
params = {
    "per_page": 100,
    "page": 1
}

all_issues = []

# Paginação da API
while True:
    response = requests.get(issues_url, headers=headers, params=params)
    data = response.json()

    if not data:
        break

    all_issues.extend(data)
    params["page"] += 1

# Gerando o CSV
csv_filename = "gitlab_board.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow([
        "ID",
        "Title",
        "Description",
        "State",
        "Labels",
        "Author",
        "Assignee",
        "Created At",
        "Updated At",
        "Closed At",
        "Web URL"
    ])
    
    for issue in all_issues:
        writer.writerow([
            issue["id"],
            issue["title"],
            issue["description"] if issue["description"] else "",
            issue["state"],
            ", ".join(issue["labels"]),
            issue["author"]["name"],
            issue["assignee"]["name"] if issue.get("assignee") else "",
            issue["created_at"],
            issue["updated_at"],
            issue["closed_at"],
            issue["web_url"]
        ])

print(f"CSV gerado com sucesso: {csv_filename}")
