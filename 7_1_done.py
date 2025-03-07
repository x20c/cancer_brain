from typing import List, Dict
import requests


def get_repository_info(repo_name: str) -> Dict[str, str]:
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch repository info: {response.status_code}"}

    data = response.json()

    return {
        "Repository Name": data.get("name"),
        "Owner": data.get("owner", {}).get("login"),
        "Description": data.get("description"),
        "License": data.get("license", {}).get("name") if data.get("license") else "None",
        "Creation Date": data.get("created_at")
    }

print(get_repository_info("octocat/Hello-World"))

def get_recent_commits(repo_name: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo_name}/commits"
    response = requests.get(url, params={"per_page": 5})

    if response.status_code != 200:
        return []

    data = response.json()
    return [
        {
        "Commit message": commit.get("message"),
        "Author": commit.get("author", {}).get("login"),
        "Date": commit.get("committed_at"),
        "Link": commit.get("html_url")
        }
        for commit in data[:5]
    ]

print(get_recent_commits("octocat/Hello-World"))