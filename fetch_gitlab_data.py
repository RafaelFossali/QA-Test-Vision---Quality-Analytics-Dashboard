import os
import requests
import pandas as pd

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")

headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}

def get_issues():
    url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/issues"
    params = {"state": "all"}  # pode filtrar: opened, closed
    response = requests.get(url, headers=headers, params=params)

    issues = response.json()

    dataset = []
    for item in issues:
        dataset.append({
            "id": item["iid"],
            "title": item["title"],
            "state": item["state"],        # opened / closed
            "author": item["author"]["name"],
            "labels": ",".join(item["labels"]),
            "created_at": item["created_at"],
            "closed_at": item["closed_at"] if item["closed_at"] else None
        })

    df = pd.DataFrame(dataset)
    df.to_csv("data/issues_gitlab.csv", index=False)
    print("📥 Dados coletados do GitLab com sucesso!")

    return df


if __name__ == "__main__":
    get_issues()
