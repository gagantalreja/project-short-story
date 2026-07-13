# Project Short Story

A curated collection of Hindi short stories with links to read or listen to them online.

## Live Page

Open `index.html` in a browser — no server required.

## Adding a Story

```bash
python3 scripts/add_story.py
```

Prompts for writer name, story name, link, and language. Skips duplicates. Updates `stories.js`.

Devanagari transliteration is handled at runtime by the webpage using the Google Input Tools API.

## Features

- Script toggle (Devanagari / Roman)
- Search by writer or story name (both scripts)
- Paginated card grid (12 per page)
- Video/audio tags for YouTube and Spotify links
- Works offline (except Devanagari transliteration)
