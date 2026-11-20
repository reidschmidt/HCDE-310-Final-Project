
import json
import ssl
import certifi
from urllib.request import urlopen
from urllib.parse import urlencode

params = {
    "term": "chill indie",
    "media": "music",
    "entity": "song",
    "limit": 10,
    "country": "US"
}

url = "https://itunes.apple.com/search?" + urlencode(params)

context = ssl.create_default_context(cafile=certifi.where())

with urlopen(url, context=context, timeout=20) as response:
    data = json.loads(response.read().decode("utf-8"))

print("Number of results:", data["resultCount"])

for song in data["results"]:
    print({
        "song": song.get("trackName"),
        "artist": song.get("artistName"),
        "album": song.get("collectionName"),
        "genre": song.get("primaryGenreName"),
        "track_url": song.get("trackViewUrl")
    })
