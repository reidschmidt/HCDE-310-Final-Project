# Context for Copilot

## Who we are
We're a pair of design students in HCDE 310, learning Python and Flask.

## How we work with AI (Stage 4: spec first)
- Don't write specs or checks for us. Before writing code, ask us for what it should do, its inputs and outputs, and 2 or 3 checks, then wait for our answer. After we write them, you may point out what's missing.
- Build in small pieces. Before you change files, tell us which ones. Don't commit.

## How we like to work
- Work in small, manageable pieces rather than generating or changing large amounts of code at once.
- Explain technical concepts and code changes in beginner-friendly language because we're still learning Python and Flask.
- When making changes, identify the exact file and explain what needs to be added, removed, or changed.
- Keep existing code and project structure intact unless a change is necessary.
- After implementing something, explain how to run and test it.
- Do not assume we understand unfamiliar Python, Flask, API, or Git concepts. Explain them when they are relevant.

## Our project
We're building a music discovery app for UW students who listen to music throughout the day while walking around campus, commuting, studying, or relaxing.

The app uses a user's current weather conditions and time of day to suggest a mood, then recommends songs that match that atmosphere. Users should also be able to customize their mood or music preferences and save favorite songs or playlists.

Our project uses three external APIs:

- **Open-Meteo:** Retrieves current weather conditions, temperature, precipitation, weather codes, and time information. It does not require an API key for our intended use.
- **iTunes Search API:** Searches for songs based on terms generated from the suggested mood. It does not require an API key. We use the returned song title, artist, album, genre, and track URL.
- **YouTube Data API v3:** Searches for YouTube videos that match recommended songs. It requires an API key stored in our local `.env` file. Each `search.list` request costs 100 quota units, with a default daily quota of 10,000 units. We use returned video IDs to create embedded YouTube players rather than downloading audio.

The Python backend will handle API requests, weather-to-mood recommendations, music searches, and saving user information. The frontend will let users view recommendations, interact with songs, customize preferences, and access saved music.

## Not decided yet
- Final app name and visual design.
- The complete weather and time-of-day rules used to determine suggested moods.
- The exact mood-to-search-term mappings and recommendation logic.
- The final JSON structure for saved songs, playlists, and user preferences.
- The final Flask routes and division of responsibilities between backend and frontend files.
- Final user testing participants, testing schedule, and success criteria.

## Wrap up
When we say "wrap up": add an entry to ai_use.md with the date and the files and functions you wrote or changed, one line each, starting with "AI draft: check me." Leave "Reflection:" blank. Suggest a commit message. Don't commit until we say yes.