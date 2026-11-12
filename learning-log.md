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

## 2026-10-09
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch, and Netflix payment/security follow-ups.
- Today's concept (Python): keep secrets out of code - a program should never hardcode API keys or bot tokens. Instead it reads them from environment variables (e.g. `os.environ.get("BOT_TOKEN")`) or from a file with 600 permissions. That is why my @raisxs_bot's token and Gemini key live in `~/.config/telegram-bot/`, never in the public `chat_bot.py` on GitHub.

## 2026-10-10
- Weekend project started: the RTX 3080 Avito price-tracker skeleton is up at `~/workspace/price-tracker/` - it fetches Avito listings and parses prices already.
- Two milestones left for me: write the CSS selectors (the README shows exactly how) and build the price history + Telegram alert.
- Real-world snag: Avito started showing a "verify you're human" checkbox from the server's end (probably blocking datacenter IPs), so the live test data for my selectors is on hold - either a one-time click-through or running the tracker from my home PC where Avito loads normally.
- Today's concept (HTML/CSS): CSS selectors are how a scraper points at the right HTML - `.price` means any element with class "price", `div.title` means a `<div>` with class "title". Writing good selectors is what makes a tracker grab exactly the prices and skip the junk around them.

## 2026-10-12
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), a new batch of Tashelhit words from my WhatsApp chats sent off for translation, and a fresh Avito pull showing six RTX 3080 cards at or below my 4,500 dh target.
- Today's concept (automation): cron - the Linux scheduler behind my @raisxs_bot watchdogs, the 15-minute reel watch and the German phrase jobs. A line like `*/15 * * * * command` means "run every 15 minutes"; the five fields are minute, hour, day-of-month, month and day-of-week.

## 2026-10-13
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch, German phrases and anime checks. Instagram blocked DM reads server-side for a few hours (HTTP 403 gating from Meta, not a broken login); reads worked again later on their own.
- Today's concept (Python): virtual environments - a `venv` is a private folder holding the exact packages one project needs, so the bot's libraries never clash with the system Python. That is what `ai-bot`'s `requirements.txt` is for: inside its venv you run `pip install -r requirements.txt` and the project gets exactly the packages it was built with.

## 2026-10-14
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch, German phrases and anime checks.
- RTX 3080 market update: the 4,000 dh Founders Edition and the 4,400 dh ASUS TUF sold within days; a new Gigabyte Gaming OC 10GB appeared at exactly 4,500 dh in Meknès - cheap cards move in about two days, so a tracker alert has to fire the same day to be useful.
- Today's concept (Python): dictionaries - `seen = {"FEs": 4000}` maps a label to a value, and `seen["FEs"]` reads it back instantly. A price tracker keeps seen listings in a dict so it can alert only when a new card appears or a price actually changes.

## 2026-10-15
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch (two new comedy shares reacted and forwarded), German phrases, and a brief Instagram API outage that fixed itself. The 3080 market was re-checked morning and afternoon: the fresh cards at or under my 4,500 dh target are still the Meknès 4,500 dh Gigabyte Gaming OC and the Rabat 3,000 dh Gigabyte Gaming OC. tracker.py untouched since Oct 10, so the selector milestone is still open.
- Today's concept (Python): JSON - APIs speak JSON, a text format that looks like a Python dict. `json.loads(response.text)` turns an API response into a real dict, and you read values with keys like `data["items"][0]["price"]`. The @raisxs_bot reads Telegram's getUpdates answers this way, pulling each incoming message out of the JSON response.

## 2026-10-16
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch, and German phrases. The 3080 market was re-checked this morning: the Rabat 3,000 dh and the Meknès 4,500 dh Gigabyte Gaming OC cards are still live, but no new cheap cards appeared. tracker.py untouched since Oct 10, so the selector milestone is still open.
- Today's concept (Django): Django is the Python web framework behind my third project idea - a dashboard. It splits a site into Models (the database tables, e.g. `Listing(title, price)`), Views (Python functions that fetch data and decide what to show), and Templates (HTML pages filled with that data). One day the price tracker could be a Django app with a web dashboard instead of a script that prints to the terminal.

## 2026-10-17
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch, German phrases #20-22 and anime alerts. Non-coding threads: researched the European Solidarity Corps (found 6 live projects open to Morocco) and got an 11-page INDH food-truck dossier built for me. tracker.py untouched since Oct 10, so the selector milestone is still open.
- Today's concept (automation): work in UTC, display local time - servers and cron jobs should always run on timezone-less UTC; convert to the user's local time only when showing something to a human. That is why my bot's cron jobs are pinned to UTC: the scheduler's Africa/Casablanca data was stale (+01 instead of +00), and UTC pinning fixed it. In Python: `from datetime import datetime, timezone` and `datetime.now(timezone.utc)` gives the real "now" anywhere on Earth; for display, `astimezone(ZoneInfo("Africa/Casablanca"))` turns it into Morocco time.

## 2026-10-18
- No code written today - the day went to launching the natural-products selling venture: a new Avito seller account "Isaac Rais" was created (phone number WhatsApp-verified) and the combined listing was submitted, sitting "en moderation" (ad ref 78434053); the Facebook Marketplace amlou listing was published (under review). A twice-daily buyer-message watch for the listings was set up. tracker.py/README are untouched since Oct 10 - the CSS selectors and price-history + Telegram alert milestones are still open.
- Today's concept (automation): polling vs webhooks - my @raisxs_bot polls Telegram with getUpdates every few seconds (pulling for new messages); a webhook would have Telegram push updates to my server instead (less delay), but it needs a public URL and an always-on server, so polling is the right call for a bot running on my home PC.
## 2026-10-19
- No code written today - the day went to starting the B1 German Phase 1 drills (phrases #1 and #2 sent via @raisxs_bot from the rebuilt 231-phrase list), delivering the INDH platform-visit checklist (Castilla or El Mers, Wednesday morning recommended after the rain forecast check), and the twice-daily Marketplace buyer watch (no buyer messages yet). tracker.py untouched since Oct 10, so the CSS-selector and price-history + Telegram-alert milestones are still open.
- Today's concept (automation): at-least-once delivery and idempotency - on 2026-10-18 the bot answered my "aff025a" message twice because the reply path answered but never bumped the "seen" file, so the next run thought the message was still unhandled and answered again. The fix pattern: mark each message seen in the same step as replying, and make the handler idempotent (safe if it ever runs twice). Any queue or cron worker that retries jobs needs this, or people get double replies.

## 2026-10-20
- Big shipping day: my animated developer portfolio went live on GitHub Pages - new public repo `portfolio` with one self-contained index.html (particle hero, typewriter roles, animated skill bars, project cards), deployed from branch main. Live at https://mustaph333.github.io/portfolio/ ; branding and title switched to my real name, Mustapha Rais, for public/professional material.
- Built PyREA, a working mini version of the viral REA project in pure Python (stdlib only): an evidence-first analyzer for Python sources (ast), JavaScript (pattern matching) and binaries (magic bytes, entropy, strings with offsets) that labels every finding observation / derivation / inference / unknown. 4 unit tests pass, and the samples reproduce REA's famous Dino findings. Pushed as public repo `pyrea` (MIT) - my first real open-source release.
- Installed the GitHub app on my phone and signed in as mustaph333. Also learned what a commit hash is: just GitHub's receipt label for each save - nothing to paste anywhere.
- Today's concept (AI tooling): an MCP server is a standard plug that lets an AI coding agent (Claude Code, Codex, Cursor, Gemini CLI) call real tools - REA is exactly that: an MCP server wiring AI agents into Ghidra, JADX and APKTool so they can analyze software without the source code. PyREA's roadmap lists an MCP-server mode as a next step.

## 2026-10-21
- No code written today - the day went to planning and decisions: picked the COD order manager (for Instagram/WhatsApp sellers in Morocco) as the first app to build with my Python/Django stack, and settled my Europe-path questions (ALX account ready, no certificate needed for the remote jobs I am aiming at). The full step-by-step build plan for the COD app is waiting on my go.
- Today's concept (Django): forms - when a customer types their name, phone, city and product on the order page, a Django form takes that raw input, validates it (phone number looks right, nothing required is missing) and hands clean data to the view, which saves one `Order` row in the database. That is the whole path from "customer taps send" to an order sitting in the dashboard: HTML form -> Django form (validate) -> model.save() -> dashboard row.
## 2026-10-22
- Portfolio animation upgrade (built, push still landing): after a reel about GSAP, I had GSAP 3.15.0 (all plugins free now) and Lenis installed locally and wired into my portfolio - smooth wave scrolling plus scroll-triggered fade/rise reveals on every section below the hero (trailer, stats, about, skills, services, projects, journey, contact), all driven by one shared GSAP ticker so scrolling stays in sync. Verified it still works with the CDN blocked and respects prefers-reduced-motion; the GitHub Pages push had not landed at check time.
- B1 German drills continued - phrase #12 of 231 from the Phase 1 list, sent via @raisxs_bot.
- Today's concept (frontend JS): a scroll-animation library like GSAP's ScrollTrigger turns the page's scroll position into a progress number - 0 to 1 as a section slides into view - and maps that onto the animation, so opacity and position follow the scroll instead of a fixed timer. It replaces hand-written scroll listeners because every animation updates in one per-frame batch, which is what keeps it smooth.
## 2026-10-23
- Portfolio iteration day (built at my direction): three versions went live - the hero fixed for speed and feel after my report (the WebGL canvas was asking for the weak "low-power" GPU instead of my RTX 2060, so it now uses the default GPU; aurora render scale 0.5 at ~20fps, dots capped at ~30fps, preloader 600ms, and the mouse-following custom cursor removed entirely), the aurora cores re-coloured from near-white to mint-green (#4ade80) at my request, and a full rebuild in Relay's section rhythm using only my own content (hero -> TRAILER -> About -> stack -> Services -> Work -> live PyREA terminal -> metrics -> Journey -> contact footer).
- Published my own language levels and work email on the portfolio: French, English - Fluent, German - Learning, Japanese - Basic, Arabic - Native, plus mustaphaxswork@gmail.com as a visible contact link.
- Judged AI video generators myself on real output clips: Wan 2.1 was "bad clearly ai slop"; ranked Wan 2.2 5B best of the four (Kling 3.0, Veo 3.1, LTX-2.3, Wan 2.2 5B). Concept learned: hosted video APIs cost real credit - Pollinations' Wan 2.2 endpoint answered "payment required" on my account, so I chose the free Colab GPU route. A Wan 2.2 5B text-to-video notebook and a zero-shot Seed-VC voice-conversion notebook (Atlas target sample embedded) are ready in my clipforge repo; first runs still pending.
- B1 German drills continued - phrases #13, #14 and #15 of 231 from the Phase 1 list, sent via @raisxs_bot.
## 2026-10-24
- Portfolio recolor day (built at my direction): sampled Relay's real palette from the GetLayers reel and repainted my portfolio - warm black #0a0a08 background, chartreuse-lime #a3e635 accent replacing emerald #4ade80 everywhere, hero trails sweeping lime -> green -> mint -> cyan. Then fixed two readability bugs I spotted: the "Open to work" line was dim grey (now bright lime and bold) and a scroll fade was washing the whole hero column out to 45% opacity (fade removed, drift kept). Pushed and live-verified.
- Built two stick-figure explainer videos with the HyperFrames HTML-to-MP4 pipeline: "$1 in the 1900s" (46s, Atlas narration, burned subtitles) and "Why do we have to work?" (67s, Bud narration). I rejected the second video's animation ("animation is bad use another tool") and it was rebuilt with Manim (58s, hamster wheel spinning clean) - Manim is now the candidate tool for the whole series.
- B1 German drills continued - phrases #16, #17 and #18 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening).

## 2026-10-25
- Video-tool verdicts changed twice today: the polished Manim v3 of "Why do we have to work?" (58s, Bud narration, tag/subtitle overlap fixed) was delivered, but I ordered a switch to Higgsfield instead, so Manim is not the series tool after all. Higgsfield's free-tier sign-in is still blocked: Google sign-in works from my side, but its Cloudflare "Verify you are human" check keeps failing - no account created, nothing paid, no test clip yet.
- Proved a free alternative end to end: installed OpenMontage (open-source agentic video studio) and rendered a 60s vertical documentary, "How Bees Make Honey", from real stock footage with local narration and burned subtitles - $0, zero API keys, no payment. The narration is local piper-tts (clearly synthetic) and two stock clips' licences still need checking before any public use. My verdict on this style vs the stick-figure route is still open.
- B1 German drills continued - phrase #19 of 231 from the Phase 1 list, sent via @raisxs_bot.

## 2026-10-28
- Portfolio language switcher built at my direction and pushed to mustaph333/portfolio main (commit 2161caf154f70abfbc7dee7ada0abe4584cf7a63): EN/FR/ES/AR switcher in the header, 194 data-i18n keys, Arabic as full RTL, choice saved in localStorage. At last check GitHub Pages was still serving the old version - a propagation lag, not a build failure.
- Video-tool verdict: I ordered a free-tool rerender of the stolen-$10M stick-figure reel and chose Manim - a 69s vertical version was delivered - then rejected it ("only Higgsfield is good in animation") and chose the real Higgsfield route. Sign-in access is now available, but on HOLD: no test clip, payment, or plan change until I say go.
- B1 German drills resumed after the usage-guard pause lifted: evening phrase 24/231 sent via @raisxs_bot ("Er ist heute Morgen zu spät zur Arbeit gekommen." / "He arrived late for work this morning."); index now 25.
- Today's concept (Python): list comprehensions - `[p for p in prices if p <= 4500]` builds a new list in one line, keeping only the items that pass the test. It replaces a loop plus an `if` plus an `append`, and it is exactly how a price tracker would filter Avito listings down to the ones under a target price.

## 2026-10-29
- Orange cartoon explainer test: a 12s vertical Manim scene was built and delivered - pomelo + mandarin circles merge into one orange, Bud narration (voice verified, no Helio), burned-in subtitles. A subtitle defect (subs rendered at the top over the tag) was found on frame check and fixed before delivery. Told him straight that free tools cannot draw the reference reel's cute cartoon faces - verdict on the test still pending.
- 2D cartoon tool research delivered at his ask: ranked Animaker first (best DIY match; free tier watermarked; Arabic voiceover unverified), then Powtoon, Steve AI, Blender (free, steep learning curve), Vyond (best quality, from ~$58/mo). Offered to verify Animaker's Arabic voice before any payment - unanswered.
- B1 German drills: phrase #25 of 231 sent via @raisxs_bot ("Sie hat ein ganzes Brot allein gegessen." / "She ate a whole loaf of bread by herself."); index now 26.
- ESC France (Saint-Brieuc, closes Mon 2 Nov 17:00): sent the full 7-item ask (info only he can supply plus his own EU Login step); the motivation-letter draft is already with him. Unanswered.


## 2026-10-30
- Portfolio recolor day (built at my direction): from an @yacine.off.dev reel screenshot, I ordered the lime scheme swapped to noir-and-blue - near-black #0B0B0F background, bright blue #1E6BFF accents (buttons, links, badges, glows, "Open to work" line, blue light trails). Pushed to mustaph333/portfolio main and live-verified (the page went from 128,685 to 199,546 bytes, lime gone) - and the EN/FR/ES/AR language switcher (pushed 28 Oct) finally went live in the same rebuild after GitHub Pages lag. Concept learned: Pages only serves a push after a build + propagation delay - the first live check still showed the old page, four minutes later it showed the new one. Verify live, never re-push blindly. My verdict on the look is still pending.
- Video tooling facts learned: my Higgsfield account is live ("XS super YT" @raisxs, "Pro Plan", 610 credits, credits expire at cycle end with no rollover) but on HOLD until I say go. Cost math: Kling 4.0 720p at ~11.25 credits per 5 seconds means about 4 full 60-second videos from the balance; Seedance 2.5 720p (35 credits/5s) manages about 1. I chose "Go Higgsfield" over OpenHiggsfield (free studio, but every generation bills my own API key). Also verified from a promo reel: VoiceStudio is a real open-source voice tool, but its default weights are CC-BY-NC - audio made with them cannot be monetised.
- I proposed a new editing plan: bro supplies AI-painted images (vertical 1080x1920), I cut the video myself in DaVinci (zooms, pans, voiceover, music, text). My next move: pick the topic, scene count and style.
- B1 German drills continued - phrases #28, #29 and #30 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening).

## 2026-10-31
- Documentary remake project kicked off (my ask): "like the عبداللطيف+ 'الهنود الحمر' doc, but in my cartoon style, in Arabic and English". I ordered Canva access and signed in with my own account. I picked the format - one 60s reel - and delegated the editorial choices. Today: 8-scene script with AR + EN narration lines, 8 scene images (first 5 painted on my Canva account, last 3 via Pollinations after the Canva image quota ran out), and two narrated voiceovers (EN 49s, AR 61.4s). Assembly into "Red Indians 60s - EN" and "- AR" video designs in my Canva web editor is still in progress - nothing delivered to me yet.
- Tool check on the reel I sent (Stickman Video Director): real and free, but code-drawn stickman animation - the same family as the Manim versions I rejected - and it needs a coding agent plus a paid AI-model subscription to run. Conclusion: it will not pass my bar; my 610 Higgsfield credits stay the quality route (still on HOLD until I say go).
- Today's concept (auth): OAuth - a "Sign in with X" button never hands the app my password; it opens X's own login page and gives the app a limited token for exactly what I approved. That is how Canva got connected. Also learned: Canva's API builds designs but not video - the real video assembly happens in Canva's web editor, which is why that step runs through a signed-in browser session.

## 2026-11-01
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green), the reel watch (funny-share reactions only, no new reels from the three friends), and the evening German drill.
- B1 German drills continued: phrases #34, #35 and #36 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening) - index now 37.
- Today's concept (Python): JSON - my bot saves its memory in JSON files (reel watermarks, seen-line counts, usage-guard state). `json.dump()` turns a Python dict into a text file, and `json.load()` reads it back on the next run. That is how a script "remembers" what it already did after the computer restarts.

## 2026-11-02
- No code written today - the day went to keeping @raisxs_bot healthy (watchdogs, relay, usage guard all green) and flagging two fresh USAFIS immigration lures in my inbox.
- B1 German drill: phrase #39 of 231 sent via @raisxs_bot (evening) - index now 40.
- Today's concept (Python): `sorted()` - it returns a new sorted list without touching the original: `sorted(prices)` for numbers, `sorted(names, reverse=True)` for Z-to-A. Unlike `list.sort()` it never mutates in place, so it is safe to call on data you still need in the original order.

## 2026-11-03
- No code written today - @raisxs_bot ran healthy all day until the weekly usage limit hit 95% at 20:06 and the usage guard paused all automation (resume after the weekly reset). Answered my Dahua camera question (forgotten password -> factory-reset procedure) and flagged another USAFIS lure.
- B1 German drills: phrases #40 and #41 of 231 sent via @raisxs_bot (morning + afternoon) - index now 42; the evening drill was skipped after the pause.

## 2026-11-04
- No code written today - the day went to closing out my wallet question (what a "token code" can and can't do: 12/24 English words = seed phrase, a long letters-and-numbers string = private key - both are the login; a short SMS/email code is not, for Trust Wallet/MetaMask) and riding out the usage-limit pause, which lifted at 17:06 after the weekly reset - all automation back on.
- B1 German drill: phrases #42 and #43 of 231 sent via @raisxs_bot (afternoon + evening) - index now 44.
- Today's concept (Python): `dict.get()` - `config.get("token")` reads a key without crashing if it is missing (returns None instead of raising KeyError), and `config.get("retries", 3)` supplies a fallback default. It is the safe way to read optional settings - one unexpected field in Telegram's JSON reply can't take the whole bot down.

## 2026-11-05
- JINX XS launch day: my brand is now JINX XS (not RAIS XS), @jinx__xs on Instagram, switched to a public Creator account, bio rewritten and links to my YouTube, Facebook and TikTok added. The Red Indians v5 reel (47.8s) went live on all four platforms the same day - Instagram reel DfWfjWBj7LO, YouTube Short ty9khPevrcg, Facebook reel 1706623220797480, TikTok @jinx_xsss (118 views in the first hour).
- Built v5 at my direction with a real ffmpeg pipeline: 8 Higgsfield clips (Kling 4.0, 168.75 credits total, ~325 left) keyed over my own images with my explainer character big and centred. Concept learned: ffmpeg's `blend` filter has no "min" mode - `blend=all_mode=darken` IS the min, so wall and floor green were keyed in parallel branches and combined with darken (chained colorkeys do not compose, each one rewrites the alpha channel). Scene 4's green speckles needed colorkey similarity raised to 0.16.
- Long-form video started: a full 12-scene Arabic script for a ~10-minute Red Indians video was written and delivered, and the complete narration was recorded (Bud voice) - 8:00 of audio, not 10, because the script paces faster than planned. Format agreed: still images with slow zoom/pan plus voiceover, character only in 4 scenes (~45 credits) - a fully animated 10 minutes would cost ~1,350 credits.
- B1 German drills continued - phrases #44, #45 and #46 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening) - index now 47.

## 2026-11-06
- No code written today, but a big shipping day for the nuclear survival series: I generated all the images myself in Meta AI on my phone - 7 scenes for Part 1, then all 20 landscape scenes for the 10-minute YouTube version - and the full video was built and delivered (10:03, Magnus voice, verified Arabic end-to-end). I reviewed it and caught two places where the picture didn't match the words (scene 1: no tea, no children; scene 3: the shelter door still open) and sent replacement images for both.
- Voice lesson from today: the voice I picked (Magnus) was identified by measuring pitch - the TikTok reel voice sits at ~98.5 Hz, which matched Magnus, not Bud. I also learned a TTS voice can translate my Arabic text and speak English instead, and the only way to catch it is to transcribe the finished audio and check it.
- B1 German drills continued - phrases #47, #48 and #49 of 231 from the Phase 1 list, sent via @raisxs_bot - index now 50.
- Today's concept (AI tooling): Whisper transcription as a check - never trust that audio says what the script says. A speech-to-text model (faster-whisper) listens to the finished recording and reports the language it actually hears, so a voice that silently translated Arabic into English gets caught before the video goes out. Same idea as a unit test: don't trust the input, verify the output.

## 2026-11-07
- Big video day for the nuclear survival series: I generated 10 of the 11 missing images myself in Meta AI (scenes 1, 3, 9, 11, 15, 16) so every narration beat gets its own picture; one is still missing (scene 16c, the final detector check and first smile). A re-cut of the 10-minute video is in progress, splitting scenes at each narration beat with a new build script (build-10min-v2.py) that uses Whisper word timestamps to find the cut points.
- Started the English version for my second channel: full English script written, Magnus English narration recorded for all 20 scenes, 18 of 20 video parts built - then I stopped it and parked the build; nothing was uploaded.
- B1 German drills continued - phrases #50, #51 and #52 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening) - index now 53. Also confirmed my Trust Wallet logs in with a 12-word seed phrase (not 24) - the 12 words are the login, a short code is not.
- Fixed a real bug in my bot tooling: the send script (send.sh) still embedded a stale, invalid Telegram token, so phrase #52 never actually went out even though the script printed "sent". It now reads the working token from ~/.config/telegram-bot/token at runtime instead of hardcoding it. Today's concept (automation): a script printing "sent" is not proof of delivery - verify the real result (the API answering ok:true with a message_id) before trusting the output. Same idea as a unit test: check the outcome, not the log line.

## 2026-11-11
- No code written today - the day went to the weekly usage reset (automation paused since 8 Nov, back on after the 17:06 reset), a live GitHub audit of my own repos for the CV Bouchra is redoing, and a new standing rule: every video and reel gets a professional cover/thumbnail before it goes up.
- Live GitHub audit for my CV (checked today, not from memory): I have 5 public repos and 1 star total - ClipForge holds the star; the 4 main projects are the Telegram bot, ClipForge, PyREA and my portfolio. The old "6 repos / 2 stars" figure in yesterday's draft was wrong.
- B1 German drill: phrase #53 of 231 sent via @raisxs_bot (evening) - index now 54.
- Today's concept (Python): reading the GitHub API - `requests.get("https://api.github.com/users/mustaph333/repos")` returns a JSON list, one dict per repo, with fields like `name` and `stargazers_count`. That is how today's audit counted my repos and stars without opening the website: one HTTP call, `response.json()`, then `len(repos)` and `sum(r["stargazers_count"] for r in repos)`. Public data needs no token; private data does.

## 2026-11-12
- New project day: I decided to build the AI shop-camera service myself (from the Take One reel) and got v1 delivered - `count_people.py` counts people entering, measures counter wait, logs visits to CSV with a summary, and runs on my RTX 2060. It takes an IP camera, a Dahua/Hikvision DVR, a webcam or a video file, with an Arabic guide and RTSP formulas. Untested on my own cameras yet - webcam is the easiest first trial; cashier matching and a nightly WhatsApp report are phase 2.
- The internet-blackout video went live on all four platforms today: «ماذا لو انقطع الإنترنت عن العالم؟ — 30 يوماً بلا شبكة», 6:12 pro version with a title card, 126 burned-in Arabic subtitle lines, a JINX XS end card and loudnorm audio. I generated all 33 images myself in Meta AI and sent a new trucks image for scene 5 ("غير القديمة بالجديد"). YouTube m5U5p2Lnvhg, TikTok 7707199935543872774, Instagram Dfouu5UunIU, Facebook 1697292068662149. The vanished-geniuses reel v2 also went live overnight with my two fixes (new restaurant scene for Meyer's "they poisoned me" beat, Tesla redrawn to look like Tesla).
- New video started: my Arabic version of the "why are rich countries cold" reel - 12-scene script and 13 image prompts written, narration next; my character appears in only 2 of the 12 scenes, on my order.
- B1 German drills continued - phrases #54, #55 and #56 of 231 from the Phase 1 list, sent via @raisxs_bot (morning, afternoon, evening) - index now 57.
