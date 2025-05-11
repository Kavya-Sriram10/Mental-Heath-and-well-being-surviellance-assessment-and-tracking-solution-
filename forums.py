import requests

API_KEY = "insert_your_api_key_here"
SEARCH_ENGINE_ID = "insert_your_search_engine_id_here"

def get_forums(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    results = response.json()
    
    forums = []
    for item in results.get("items", []):
        forums.append({"title": item["title"], "link": item["link"]})

    return forums[:5]

# Example
forums = google_search("Depression mental health forums")
for f in forums:
    print(f"{f['title']}: {f['link']}")
