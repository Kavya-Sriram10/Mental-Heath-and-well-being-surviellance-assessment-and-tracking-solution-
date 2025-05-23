import requests

# YOUTUBE_API_KEY = "insert_your_api_key_here"
# YOUTUBE_SEARCH_URL = "insert_your_youtube_search_url_here"

def get_youtube_videos(query):
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": 5,  # Fetch top 3 relevant videos
        "type": "video"
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    data = response.json()

    videos = []
    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            video_title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({"title": video_title, "url": video_url})

    return videos

# Example usage 
query = "mental health tips"
videos = get_youtube_videos(query)

# Print video links
for video in videos:
    print(f"{video['title']}: {video['url']}")
