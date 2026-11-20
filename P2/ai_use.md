# AI Use

We used AI stage 4. We reviewed and ran the generated test code ourselves to make sure the API requests worked and returned real data. Final design decisions and project direction were determined by our team

Specifically: 

- **Ideation:** Our team completed the initial brainstorming, ideation, and design decisions ourselves.
- **Testing:** We used AI to help write and troubleshoot our API test scripts for Open-Meteo, iTunes Search API, and YouTube Data API.
- **Stage 4 AI:** We used AI at Stage 4 to help with implementation and development tasks while following the course guidelines.

Reflection: AI was helpful throughout our project, especially when writing and troubleshooting our API test scripts. It helped us understand API documentation, fix Python errors, and successfully retrieve real data from our three APIs. This allowed us to spend more time focusing on our design and project direction rather than getting stuck on technical issues. However, we also learned that AI suggestions are not always correct and need to be tested. We made our own ideation and design decisions, and running the generated code ourselves helped us understand how the APIs worked instead of relying entirely on AI. Overall, AI was a useful tool for P2.

Transcript: 

Us: ok for the open meteo code example how do i do that in vs code

Let's do this in two parts: first, run the Open-Meteo request in VS Code

Part 1: Run Open-Meteo in VS Code
We'll create a small Python file that makes a real request to Open-Meteo and prints the current weather data. This version uses Python's built-in tools, so you don't need to install anything.
Step 1. Open your project
1. Open VS Code.
2. Go to File → Open Folder.
3. Open your shared HCDE 310 final project folder (the one containing your P2 folder).
Step 2. Create a Python file
In the VS Code Explorer on the left:
1. Find your P2 folder.
2. Right-click it and select New File.
3. Name the file open_meteo_test.py.
Step 3. Paste this complete code
import jsonfrom urllib.request import urlopenfrom urllib.parse import urlencode# Seattle coordinatesparams = {    "latitude": 47.6062,    "longitude": -122.3321,    "current": "temperature_2m,precipitation,weather_code,is_day",    "temperature_unit": "fahrenheit"}# Build the API requesturl = "https://api.open-meteo.com/v1/forecast?" + urlencode(params)# Send the request and read the responsewith urlopen(url, timeout=20) as response:    data = json.loads(response.read().decode("utf-8"))# Print only the current weather informationprint(json.dumps(data["current"], indent=4))

Step 4. Run the code
1. Save the file with Ctrl + S.
2. Click the triangle Run Python File button in the top-right corner of VS Code.
3. Look at the Terminal panel at the bottom.
VS Code's Python extension supports running a saved Python file directly in the terminal. 
Visual Studio Code+1

You should see output containing fields like temperature_2m, precipitation, weather_code, and is_day.

Important: The actual numbers will depend on Seattle's weather when you run it. Copy the output and send it to me. We'll use the real response in your assignment.

Us: File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 464, in _call_chain
    result = func(*args)
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 1381, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        context=self._context)
                        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 1336, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1082)>
PS C:\documents\Coding\HCDE-310-Final-Project> cd P2
PS C:\documents\Coding\HCDE-310-Final-Project\P2> & 'C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/documents/Coding/HCDE-310-Final-Project/P2/Open-Meteo_Test.py'
Traceback (most recent call last):
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 1333, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              encode_chunked=req.has_header('Transfer-encoding'))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1386, in request
    self._send_request(method, url, body, headers, encode_chunked)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1432, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1381, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1141, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1085, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\http\client.py", line 1527, in connect
    self.sock = self._context.wrap_socket(self.sock,
                ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
                                          server_hostname=server_hostname)
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\ssl.py", line 469, in wrap_socket
    return self.sslsocket_class._create(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        sock=sock,
        ^^^^^^^^^^
    ...<5 lines>...
        session=session
        ^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\ssl.py", line 1087, in _create
    self.do_handshake()
    ~~~~~~~~~~~~~~~~~^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\ssl.py", line 1383, in do_handshake
    self._sslobj.do_handshake()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1082)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\documents\Coding\HCDE-310-Final-Project\P2\Open-Meteo_Test.py", line 18, in <module>
    with urlopen(url, timeout=20) as response:
         ~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 187, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 487, in open
    response = self._open(req, data)
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 504, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
                              '_open', req)
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 464, in _call_chain
    result = func(*args)
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 1381, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        context=self._context)
                        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\Lib\urllib\request.py", line 1336, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1082)>
PS C:\documents\Coding\HCDE-310-Final-Project\P2>

AI: Your Python code is fine. The problem is an **SSL certificate verification error**. Python is having trouble verifying the security certificate when it connects to Open-Meteo.

This can happen when Python's trusted certificate list is outdated. Let's fix that without disabling security verification.

## **Step 1. Update Python's certificates**

In your VS Code terminal, copy and run:

```
& 'C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\python.exe' -m pip install --upgrade certifi
```

This installs or updates `certifi`, which provides a trusted collection of security certificates.

## **Step 2. Replace your Python file**

Open `P2/Open-Meteo_Test.py` and replace its contents with this:

```
import jsonimport sslimport certififrom urllib.request import urlopenfrom urllib.parse import urlencode# Seattle coordinatesparams = {    "latitude": 47.6062,    "longitude": -122.3321,    "current": "temperature_2m,precipitation,weather_code,is_day",    "temperature_unit": "fahrenheit"}# Build the API requesturl = "https://api.open-meteo.com/v1/forecast?" + urlencode(params)# Use updated trusted certificatescontext = ssl.create_default_context(cafile=certifi.where())# Send request and read responsewith urlopen(url, context=context, timeout=20) as response:    data = json.loads(response.read().decode("utf-8"))# Print current weather informationprint(json.dumps(data["current"], indent=4))
```

## **Step 3. Run it again**

Save with `Ctrl + S`, then run:

```
python Open-Meteo_Test.py
```

Make sure your terminal is still inside the `P2` folder.

## **Step 4. Send me the result**

If it works, you should see something similar to:

```
{
    "time": "2026-11-19T13:00",
    "interval": 900,
    "temperature_2m": 52.0,
    "precipitation": 0.0,
    "weather_code": 3,
    "is_day": 1
}
```

Those numbers are illustrative, not actual weather data.

**If you still get the certificate error**, check that Windows has the correct date, time, and automatic time synchronization enabled. Then send me the new error.

Once it works, we'll have the real API response needed for your HCDE 310 assignment.

Us: [notice] A new release of pip is available: 26.2.1 -> 26.3
[notice] To update, run: C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install --upgrade pip
PS C:\documents\Coding\HCDE-310-Final-Project\P2> python Open-Meteo_Test.py
{              
    "time": "2026-11-19T21:15",
    "interval": 900,
    "temperature_2m": 49.6,
    "precipitation": 0.0,
    "weather_code": 3,
    "is_day": 1
}

AI: Perfect! Your Open-Meteo API request worked. You now have a real API response that you can use in your P2 assignment.

Us: is getting a youtube api key easy

AI: Yes! Getting a YouTube API key is pretty straightforward. You don't need to pay, email anyone, or set up OAuth for what we're doing.

For your project, you only need an **API key** to search public YouTube videos.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://developers.google.com\&sz=32)

Google for Developers+1



## **How to get your YouTube API key**

1. **Open Google Cloud Console**

   Go to [Google Cloud Console](https://console.cloud.google.com/?utm_source=chatgpt.com) and sign in with your Google account.
2. **Create a project**
   - Click the project selector at the top.
   - Select **New Project**.
   - Name it `Weather Music Discovery`.
   - Click Create.
3. **Enable YouTube Data API v3**

   Go to [YouTube Data API v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com?utm_source=chatgpt.com).

   Make sure your new project is selected, then click **Enable**.
4. **Create your API key**

   Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials?utm_source=chatgpt.com).
   - Click **Create Credentials**.
   - Select **API key**.
   - Copy the generated key.
5. **Restrict your API key**

   In the key settings:
   - API restrictions: Restrict key.
   - Select **YouTube Data API v3**.
   - Save.

## **What are the limits?**

According to Google's current documentation:

- Search requests: 100 per day by default.
- Other API requests: 10,000 quota units per day by default.
- Searching for a video costs one search request.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://developers.google.com\&sz=32)

  Google for Developers+1



That's plenty for a class project if we cache search results.

## **Once you have the key**

We'll put it in your `.env` file:

```
YOUTUBE_API_KEY=your_actual_key_here
```

**Don't commit your&#x20;**`.env`**&#x20;file to GitHub or share the actual key here.**

Once you've created the key, tell me and we'll test a real YouTube search in VS Code, just like we did with Open-Meteo.

Us: ok first lets do the itunes section

AI: Great. We'll use **Apple's iTunes Search API** as your second data source, replacing Last.fm. It requires no API key or account, and it can return song titles, artists, album artwork, and preview URLs.

One important distinction for your project: iTunes provides short song previews, while YouTube will provide the embedded music videos for playback.

## **Data Source 2: Apple iTunes Search API**

**1. Name and documentation link**

[Apple iTunes Search API – Official Documentation](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/?utm_source=chatgpt.com)

**2. What we use it for**

We use iTunes in **Action 2: Discover and Play Music**. After our Python code generates a mood, the app searches for songs using terms related to that mood and the user's preferred genre. It returns song titles, artist names, and other information that we can use when searching YouTube for playable versions.

**3. Key or limits**

- No API key or account is required.
- Apple's documentation states that the API supports approximately 20 requests per minute, although this limit can change.
- Search requests can return up to 200 results, but we will request only 10.
- Apple restricts the use of promotional content, including previews and artwork, to promoting content in its stores.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://performance-partners.apple.com\&sz=32)

  Apple Services Performance Partners+1



**4. The call**

We'll search for 10 songs using the terms `chill indie`, with the US music catalog.

Example URL:

```
https://itunes.apple.com/search?term=chill+indie&media=music&entity=song&limit=10&country=US
```

For your actual project, create this file:

`P2/itunes_test.py`

Paste this complete code:

```
import jsonimport sslimport certififrom urllib.request import urlopenfrom urllib.parse import urlencodeparams = {    "term": "chill indie",    "media": "music",    "entity": "song",    "limit": 10,    "country": "US"}url = "https://itunes.apple.com/search?" + urlencode(params)context = ssl.create_default_context(cafile=certifi.where())with urlopen(url, context=context, timeout=20) as response:    data = json.loads(response.read().decode("utf-8"))print("Number of results:", data["resultCount"])for song in data["results"]:    print({        "song": song.get("trackName"),        "artist": song.get("artistName"),        "album": song.get("collectionName"),        "genre": song.get("primaryGenreName"),        "track_url": song.get("trackViewUrl")    })
```

**5. One real response**

We need to run the request in VS Code to capture the actual results. I couldn't retrieve the live endpoint through my browser, so I don't want to invent song results.

The output should look like this structurally:

```
{
    "song": "Actual Song Title",
    "artist": "Actual Artist",
    "album": "Actual Album",
    "genre": "Actual Genre",
    "track_url": "Actual Apple URL"
}
```

Your program will print up to 10 actual results. We'll paste the first two or three into your assignment.

**6. What we noticed or were surprised by**

The iTunes API searches its music catalog using text rather than providing dedicated mood categories. This means our app will need to translate its generated mood into search terms, such as `chill indie` or `happy pop`, to find relevant songs.

## **Your next step**

1. Save `itunes_test.py` inside `P2`.
2. Open your VS Code terminal.
3. Make sure you're in the `P2` directory.
4. Run:

```
python itunes_test.py
```

Send me the output, and I'll turn it into the final polished iTunes section with your actual API response.

Us: PS C:\documents\Coding\HCDE-310-Final-Project\P2> python Open-Meteo_Test.py
{              
    "time": "2026-11-19T21:15",
    "interval": 900,
    "temperature_2m": 49.6,
    "precipitation": 0.0,
    "weather_code": 3,
    "is_day": 1
}
PS C:\documents\Coding\HCDE-310-Final-Project\P2> & 'C:\Users\schmi\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:/documents/Coding/HCDE-310-Final-Project/P2/itunes_test.py'
Number of results: 8
{'song': 'we fell in love in october', 'artist': 'girl in red', 'album': 'we fell in love in october / forget her - Single', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/we-fell-in-love-in-october/1441416633?i=1441416638&uo=4'}
{'song': 'Chill Indie', 'artist': 'Alira Beats', 'album': 'Chill Indie - Single', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/chill-indie/1890165327?i=1890165329&uo=4'}
{'song': 'Self Control', 'artist': 'Frank Ocean', 'album': 'Blonde', 'genre': 'Pop', 'track_url': 'https://music.apple.com/us/album/self-control/1146195596?i=1146195718&uo=4'}
{'song': 'Get You (feat. Kali Uchis)', 'artist': 'Daniel Caesar', 'album': 'Freudian', 'genre': 'R&B/Soul', 'track_url': 'https://music.apple.com/us/album/get-you-feat-kali-uchis/1799080774?i=1799080775&uo=4'}
{'song': 'Too Sweet', 'artist': 'Hozier', 'album': 'Unheard - EP', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/too-sweet/1735414393?i=1735414394&uo=4'}
{'song': 'Ribs', 'artist': 'Lorde', 'album': 'Pure Heroine', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/ribs/1440818584?i=1440818666&uo=4'}
{'song': 'Thinkin Bout You', 'artist': 'Frank Ocean', 'album': 'channel ORANGE', 'genre': 'Pop', 'track_url': 'https://music.apple.com/us/album/thinkin-bout-you/1440765580?i=1440766128&uo=4'}
{'song': 'Chill (feat. Julia Gomez)', 'artist': 'Anthony Amorim', 'album': 'LO:ST', 'genre': 'Indie Pop', 'track_url': 'https://music.apple.com/us/album/chill-feat-julia-gomez/1833969242?i=1833969245&uo=4'}
PS C:\documents\Coding\HCDE-310-Final-Project\P2>

AI: Perfect! Your iTunes API request worked, and you got 8 real results from your search for chill indie.

Us: ok perfect yep lets do the youtube one next

AI: Perfect. YouTube will be your **third data source**, and it fills the playback part of the app: iTunes finds songs that match the suggested mood, then YouTube finds a video users can actually play.

One important distinction for the proposal: **the YouTube Data API finds videos and returns their IDs; the YouTube embedded player plays them.** Your app won't download or play raw audio files.

Let's set it up and test a real search before writing the final P2 section.

## **YouTube Data API v3**

**Official documentation:** [YouTube Data API overview](https://developers.google.com/youtube/data/getting-started?utm_source=chatgpt.com) and [Search: list reference](https://developers.google.com/youtube/v3/docs/search/list?utm_source=chatgpt.com).

### **1. What we'll use it for**

In **Action 2: Discover and play music**, our app will:

1. Take a song title and artist returned by the iTunes Search API.
2. Search YouTube for that song.
3. Request videos that can be embedded in a webpage.
4. Use the returned video ID to display the YouTube player inside our app.

### **2. Key or limits**

- **API key required:** Yes. You can use a Google Cloud API key for public video searches; OAuth is not needed for this feature.

- **Cost:** No charge for the standard included quota.

- **Quota:** The default allocation includes 100 `search.list` calls per day. Each search uses one call from that separate daily search quota. Other API methods have a separate 10,000-unit daily quota.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://developers.google.com\&sz=32)

  Google for Developers+1

- **Limitations:** Some videos cannot be embedded, so we'll request embeddable videos and handle cases where no suitable result is returned.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://developers.google.com\&sz=32)

  Google for Developers



### **3. Create your API key**

1. Open [Google Cloud Console](https://console.cloud.google.com/?utm_source=chatgpt.com).
2. Sign in with your Google account.
3. Create a project. You can call it `Weather Music Discovery`.
4. Open the [YouTube Data API v3 page](https://console.cloud.google.com/apis/library/youtube.googleapis.com?utm_source=chatgpt.com) and click **Enable**.
5. Open [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials?utm_source=chatgpt.com).
6. Click **Create Credentials → API key**.
7. Restrict the key to the **YouTube Data API v3** if the console offers API restrictions.

Keep the key private. We'll store it in `.env`, not directly in our Python code or GitHub repository.

### **4. The API call we'll test**

The endpoint is:

```
https://www.googleapis.com/youtube/v3/search
```

We'll use these parameters:

| Parameter         | Value                                    | Purpose                       |
| ----------------- | ---------------------------------------- | ----------------------------- |
| `part`            | `snippet`                                | Get video details             |
| `q`               | `we fell in love in october girl in red` | Search for the song           |
| `type`            | `video`                                  | Only return videos            |
| `videoEmbeddable` | `true`                                   | Only return embeddable videos |
| `maxResults`      | `5`                                      | Return up to five results     |
| `key`             | Your API key                             | Authenticate the request      |

### **5. What I need from you**

Have you already created the YouTube API key, or do you need to create it first?

Once you have it, I'll give you the complete contents for `P2/youtube_test.py` and the exact `.env` setup. Then we'll run it in VS Code and use your **actual returned video title, channel, and video ID** in the P2 proposal rather than making up an example.

Us: I got my key

AI: Great! Now let's connect it to your project securely and test a real YouTube search.

We'll put the key in a `.env` file so it doesn't get exposed in your Python code or GitHub.

### **Step 1: Create your&#x20;**`.env`**&#x20;file**

In VS Code, create a new file in your project folder:

`C:\documents\Coding\HCDE-310-Final-Project\.env`

Add this line, replacing the placeholder with your actual key:

```
YOUTUBE_API_KEY=paste_your_actual_key_here
```

Don't add quotation marks, and don't share the key here.

### **Step 2: Make sure Git ignores the key**

Open your project's root `.gitignore`:

`C:\documents\Coding\HCDE-310-Final-Project\.gitignore`

Make sure it contains these lines (add them if they aren't already there):

```
.env
.venv/
```

This prevents Git from tracking your API key and virtual environment.

### **Step 3: Create the YouTube test script**

Create this file:

`C:\documents\Coding\HCDE-310-Final-Project\P2\youtube_test.py`

Paste in the complete code below:

```
import jsonimport sslfrom pathlib import Pathfrom urllib.error import HTTPError, URLErrorfrom urllib.parse import urlencodefrom urllib.request import urlopenimport certifi# Read the API key from the .env file in the project root.project_folder = Path(__file__).resolve().parent.parentenv_file = project_folder / ".env"api_key = ""if env_file.exists():    for line in env_file.read_text(encoding="utf-8").splitlines():        if line.startswith("YOUTUBE_API_KEY="):            api_key = line.split("=", 1)[1].strip()            breakif not api_key:    raise RuntimeError(        "YOUTUBE_API_KEY was not found. Check the .env file "        "in the main project folder."    )# Search YouTube for a song.params = {    "part": "snippet",    "q": "girl in red we fell in love in october",    "type": "video",    "videoEmbeddable": "true",
```

This searches for an actual song and asks YouTube to return only videos that can be embedded in our app.

### **Step 4: Run the test**

In your VS Code terminal, make sure you're in the `P2` folder:

```
cd C:\documents\Coding\HCDE-310-Final-Project\P2
```

Then run:

```
python youtube_test.py
```

You should see up to five matching videos, including their titles, channel names, video IDs, and embed URLs.

If you get a `ModuleNotFoundError` for `certifi`, run:

```
python -m pip install certifi
```

### **Step 5: What we'll document for P2**

Here are the important details for our third data source:

- **Name and docs:** [YouTube Data API – Search: list](https://developers.google.com/youtube/v3/docs/search/list?utm_source=chatgpt.com).

- **What we use it for:** Action 2. After iTunes finds songs matching the recommended mood, YouTube searches for playable videos of those songs.

- **Key or limits:** Requires a Google API key. The default quota allows 100 `search.list` calls per day. We should cache results and avoid searching again unnecessarily.&#x20;

  [image](https://www.google.com/s2/favicons?domain=https://developers.google.com\&sz=32)

  Google for Developers+1

- **The call:** `https://www.googleapis.com/youtube/v3/search`, with the song query, `type=video`, and `videoEmbeddable=true`.

- **One real response:** We'll use the actual output from your test.

- **What we noticed:** YouTube returns video metadata and IDs, not downloadable music files. We can use the video ID to embed the YouTube player in our app.

**Run the test and send me the terminal output.** Then I'll turn all three data-source sections into polished P2-ready writing, using your actual API responses.

Us: ile "c:\documents\Coding\HCDE-310-Final-Project\P2\itunes_test.py", line 4, in <module>
    import certifi
ModuleNotFoundError: No module named 'certifi'
(.venv) PS C:\documents\Coding\HCDE-310-Final-Project> python -m pip install certifi
Collecting certifi
  Using cached certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
Installing collected packages: certifi
Successfully installed certifi-2026.10.23

[notice] A new release of pip is available: 26.2.1 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) PS C:\documents\Coding\HCDE-310-Final-Project> python -c "import certifi; print(certifi.where())"
C:\documents\Coding\HCDE-310-Final-Project\.venv\Lib\site-packages\certifi\cacert.pem
(.venv) PS C:\documents\Coding\HCDE-310-Final-Project> & 'c:\documents\Coding\HCDE-310-Final-Project\.venv\Scripts\python.exe' 'c:/documents/Coding/HCDE-310-Final-Project/P2/itunes_test.py'
Number of results: 8
{'song': 'we fell in love in october', 'artist': 'girl in red', 'album': 'we fell in love in october / forget her - Single', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/we-fell-in-love-in-october/1441416633?i=1441416638&uo=4'}
{'song': 'Chill Indie', 'artist': 'Alira Beats', 'album': 'Chill Indie - Single', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/chill-indie/1890165327?i=1890165329&uo=4'}
{'song': 'Self Control', 'artist': 'Frank Ocean', 'album': 'Blonde', 'genre': 'Pop', 'track_url': 'https://music.apple.com/us/album/self-control/1146195596?i=1146195718&uo=4'}
{'song': 'Get You (feat. Kali Uchis)', 'artist': 'Daniel Caesar', 'album': 'Freudian', 'genre': 'R&B/Soul', 'track_url': 'https://music.apple.com/us/album/get-you-feat-kali-uchis/1799080774?i=1799080775&uo=4'}
{'song': 'Too Sweet', 'artist': 'Hozier', 'album': 'Unheard - EP', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/too-sweet/1735414393?i=1735414394&uo=4'}
{'song': 'Ribs', 'artist': 'Lorde', 'album': 'Pure Heroine', 'genre': 'Alternative', 'track_url': 'https://music.apple.com/us/album/ribs/1440818584?i=1440818666&uo=4'}
{'song': 'Thinkin Bout You', 'artist': 'Frank Ocean', 'album': 'channel ORANGE', 'genre': 'Pop', 'track_url': 'https://music.apple.com/us/album/thinkin-bout-you/1440765580?i=1440766128&uo=4'}
{'song': 'Chill (feat. Julia Gomez)', 'artist': 'Anthony Amorim', 'album': 'LO:ST', 'genre': 'Indie Pop', 'track_url': 'https://music.apple.com/us/album/chill-feat-julia-gomez/1833969242?i=1833969245&uo=4'}
(.venv) PS C:\documents\Coding\HCDE-310-Final-Project> & 'c:\documents\Coding\HCDE-310-Final-Project\.venv\Scripts\python.exe' 'c:/documents/Coding/HCDE-310-Final-Project/P2/youtube_test.py'
Number of results: 5
{'title': 'girl in red - we fell in love in october', 'channel': 'girl in red', 'video_id': 'iggmiF7DNoM', 'embed_url': 'https://www.youtube.com/embed/iggmiF7DNoM'}
{'title': 'girl in red - we fell in love in october (Lyrics)', 'channel': 'Dan Music', 'video_id': 'AmTMNntVmbQ', 'embed_url': 'https://www.youtube.com/embed/AmTMNntVmbQ'}
{'title': 'girl in red | We fell in love in october (Sub. Español)', 'channel': 'Ángel DM', 'video_id': '7T7-cqhRvIc', 'embed_url': 'https://www.youtube.com/embed/7T7-cqhRvIc'}
{'title': 'girl in red - we fell in love in october (Lyrics)', 'channel': 'MAYELEVRSE', 'video_id': '0u71SGkEJA4', 'embed_url': 'https://www.youtube.com/embed/0u71SGkEJA4'}
{'title': 'Girl in Red - We Fell In Love In October', 'channel': 'ST∆R', 'video_id': 'Cq1sAJApmOQ', 'embed_url': 'https://www.youtube.com/embed/Cq1sAJApmOQ'}
(.venv) PS C:\documents\Coding\HCDE-310-Final-Project>

AI: Awesome — both APIs are now working successfully!