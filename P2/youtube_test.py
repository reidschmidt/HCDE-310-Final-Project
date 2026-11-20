
import json
import ssl
import certifi
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError


# Find the .env file in the main project folder
project_folder = Path(__file__).resolve().parent.parent
env_file = project_folder / ".env"

api_key = ""

if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("YOUTUBE_API_KEY="):
            api_key = line.split("=", 1)[1].strip()
            break

if not api_key:
    raise RuntimeError("YouTube API key not found. Check your .env file.")


# Search YouTube for a song returned by our iTunes API
params = {
    "part": "snippet",
    "q": "girl in red we fell in love in october",
    "type": "video",
    "videoEmbeddable": "true",
    "maxResults": 5,
    "key": api_key
}

url = "https://www.googleapis.com/youtube/v3/search?" + urlencode(params)

context = ssl.create_default_context(cafile=certifi.where())

try:
    with urlopen(url, context=context, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))

    print("Number of results:", len(data.get("items", [])))

    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]

        print({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "video_id": video_id,
            "embed_url": f"https://www.youtube.com/embed/{video_id}"
        })

except HTTPError as error:
    print("YouTube API error:", error.code)
    print(error.read().decode("utf-8"))

except URLError as error:
    print("Connection error:", error.reason)
