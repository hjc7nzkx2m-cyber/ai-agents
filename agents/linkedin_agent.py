import requests
from bs4 import BeautifulSoup

def fetch_linkedin_posts(keyword):
    """
    Version simple : récupère des posts publics liés au mot-clé.
    ⚠️ On ne fait pas de scraping agressif
    """
    url = f"https://www.linkedin.com/search/results/content/?keywords={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = []
    for post in soup.find_all("span", {"class": "feed-shared-text__text-view"}):
        posts.append(post.get_text())
    return posts

if __name__ == "__main__":
    posts = fetch_linkedin_posts("agent IA")
    for p in posts:
        print(p)