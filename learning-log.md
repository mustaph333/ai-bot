# Learning Log

Day-by-day notes on what I am building and learning.

## 2026-10-03
- Set up a professional GitHub profile with a README
- Created the `ai-bot` repo with README, .gitignore and requirements.txt
- Roadmap: echo bot -> AI brain -> PC commands from Telegram
- Pushed the actual bot code (`chat_bot.py`) to `ai-bot` - it is live as @raisxs_bot on Telegram
- Scoped the bot to chat-only for now; PC commands and alerts moved to later ideas
- Kept my Darija/Tashelhit instructions in a local file only - the public code just lists English, German, Japanese and Arabic
- Taught the bot new Tashelhit words and checked its Tashelhit replies to my friends were correct
- The bot now replies to photos too (it was skipping messages with images attached)

## 2026-10-04
- Switched @raisxs_bot to all-human replies: every stranger message gets answered personally in Tashelhit, simple phrases reply instantly, and the 10-replies-per-week limit was removed
- Accepted a second Tashelhit teacher for the bot - words he teaches go into the phrasebook and the bot's language file, same as mine
- Taught the bot new Tashelhit words and rules (ama matgis, ork fhimgh, ma3 = why only, manik standalone, ma trit, gher = only, no-laughing rule) and purged words I never taught (tqim, kandhk)
- Translated 80 English words into Tashelhit in 8 batches of 10 for the phrasebook

## 2026-10-05
- Today's concept (AI): looked into Wan2GP for local AI video generation - needs an NVIDIA CUDA GPU with 6GB+ VRAM, 16GB+ RAM and plenty of disk space; my RTX 2060 meets the stated minimum. No setup started yet.

## 2026-10-06
- No coding or lessons today - the day went to automation orders (usage-limit pause, timezone pinning, German phrases replacing the learn nudges) and security checks.
- Today's concept: `try/except` - wrapping a risky call (like an API request) in `try/except` lets a program catch the error and keep running instead of crashing. My @raisxs_bot uses this idea when it retries the Gemini API up to 3 times with backoff on 429/503 errors.


## 2026-10-07
- No coding or lessons today - the day went to translating Tashelhit words from my WhatsApp chats (40+ words in 4 batches of 10), tuning the bot's voice ("answer like you are me"), and fixing its slow replies with instant answers.
- Today's concept: systemd services - a `.service` file tells Linux how to start a program, restart it automatically if it crashes, and launch it at boot. That is how my @raisxs_bot stays alive on my PC instead of only running while a terminal is open.

## 2026-10-08
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green). Researched the RTX 3080 upgrade: used 10GB models on Avito go for 4,000-5,000 dh, Ti/12GB around 6,000, so selling the RTX 2060 (about 2,000 dh) means roughly 2-3k dh out of pocket. Still deciding whether to start hunting now or after the 2060 sells.
- Today's concept (Python): web scraping basics - fetch a listing page with `requests`, parse the HTML with `BeautifulSoup`, and pull the price and title out of each listing element. The Avito price-tracker project would run that on a schedule and send a Telegram alert when a 3080 drops below my target price.
