import json
import logging
import os
import random
import re
from datetime import date

import httpx
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

logging.basicConfig(level=logging.INFO)

BASE = "/home/hatch/workspace/telegram-bot"
ISAAC_CHAT = 6526548724
LAST_FRIEND_FILE = os.path.join(BASE, "last_friend.json")
INBOX_FILE = os.path.join(BASE, "inbox.jsonl")
ISAAC_INBOX_FILE = os.path.join(BASE, "isaac_inbox.jsonl")
USAGE_FILE = os.path.join(BASE, "usage.json")
VISITORS_DIR = os.path.join(BASE, "visitors")
# Strangers get this many AI replies per week each (~2% of the weekly budget).
WEEKLY_LIMIT_PER_STRANGER = 10
OVER_LIMIT_WARNING = "sf sir at9wt ayis or s3mrs ightris wink 3dlghaks"
GEMINI_KEY_FILE = "/home/hatch/.config/telegram-bot/gemini.key"
GEMINI_MODEL = "gemini-3.8-flash"
HISTORY_FILE = os.path.join(BASE, "history.json")
HISTORY_LIMIT = 20  # messages kept per chat


def get_token() -> str:
    with open("/home/hatch/.config/telegram-bot/token") as f:
        return f.read().strip()


def get_gemini_key():
    try:
        with open(GEMINI_KEY_FILE) as f:
            key = f.read().strip()
            return key or None
    except Exception:
        return None


def load_history(chat_id: int):
    try:
        return json.load(open(HISTORY_FILE)).get(str(chat_id), [])
    except Exception:
        return []


def save_history(chat_id: int, history):
    try:
        all_hist = {}
        try:
            all_hist = json.load(open(HISTORY_FILE))
        except Exception:
            pass
        all_hist[str(chat_id)] = history[-HISTORY_LIMIT:]
        json.dump(all_hist, open(HISTORY_FILE, "w"))
    except Exception:
        pass


def get_week_key() -> str:
    d = date.today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def check_stranger_quota(chat_id: int):
    """Weekly AI-reply quota for non-Isaac chats.

    Returns (allowed, first_exceed): allowed=False means don't reply;
    first_exceed=True means send the over-limit warning this once.
    """
    try:
        usage = json.load(open(USAGE_FILE))
    except Exception:
        usage = {}
    week = get_week_key()
    entry = usage.get(str(chat_id))
    if not entry or entry.get("week") != week:
        entry = {"week": week, "count": 0, "warned": False}
    if entry["count"] >= WEEKLY_LIMIT_PER_STRANGER:
        if not entry.get("warned"):
            entry["warned"] = True
            usage[str(chat_id)] = entry
            try:
                json.dump(usage, open(USAGE_FILE, "w"))
            except Exception:
                pass
            return (False, True)
        return (False, False)
    entry["count"] = entry.get("count", 0) + 1
    usage[str(chat_id)] = entry
    try:
        json.dump(usage, open(USAGE_FILE, "w"))
    except Exception:
        pass
    return (True, False)


async def log_visitor(chat, context):
    """Visitor log: save a stranger's public Telegram identity + profile photo.

    This is their PUBLIC profile photo (visible to anyone on Telegram),
    not a camera snap - bots cannot access anyone's camera.
    """
    try:
        vdir = os.path.join(VISITORS_DIR, str(chat.id))
        os.makedirs(vdir, exist_ok=True)
        info_path = os.path.join(vdir, "info.json")
        try:
            info = json.load(open(info_path))
        except Exception:
            info = {}
        info.update(
            {
                "name": f"{chat.first_name or ''} {chat.last_name or ''}".strip(),
                "username": chat.username,
                "last_seen": date.today().isoformat(),
                "messages": info.get("messages", 0) + 1,
            }
        )
        if "first_seen" not in info:
            info["first_seen"] = info["last_seen"]
        # Fetch the public profile photo once per visitor.
        photo_path = os.path.join(vdir, "profile.jpg")
        if not os.path.exists(photo_path):
            try:
                photos = await context.bot.get_user_profile_photos(chat.id, limit=1)
                if photos.total_count > 0:
                    file_id = photos.photos[0][-1].file_id
                    tg_file = await context.bot.get_file(file_id)
                    data = await tg_file.download_as_bytearray()
                    with open(photo_path, "wb") as f:
                        f.write(bytes(data))
                    info["has_photo"] = True
            except Exception as e:
                logging.warning("Visitor photo fetch failed: %s", e)
        json.dump(info, open(info_path, "w"))
    except Exception as e:
        logging.warning("Visitor log failed: %s", e)


def ai_reply(text: str, name: str, history=None, image_b64=None):
    """Ask Gemini for a chat reply, with conversation history and optional image. Returns None on any failure."""
    key = get_gemini_key()
    if not key:
        return None
    # The egress proxy intercepts TLS; trust its CA bundle.
    ca = os.environ.get("SSL_CERT_FILE", "/run/hatch/egress-tls/ca-bundle.pem")
    verify = ca if os.path.exists(ca) else True
    contents = []
    for h in history or []:
        contents.append({"role": h["role"], "parts": [{"text": h["text"]}]})
    user_parts = []
    if image_b64:
        user_parts.append({"inline_data": {"mime_type": "image/jpeg", "data": image_b64}})
    user_parts.append({"text": text})
    contents.append({"role": "user", "parts": user_parts})
    try:
        with httpx.Client(verify=verify, timeout=30) as client:
            resp = client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
                headers={"x-goog-api-key": key},
                json={
                    "system_instruction": {
                        "parts": [
                            {
                                "text": (
                                    "You are raisxs bot, a friendly chat bot on Telegram. "
                                    "Chat like a smart, helpful friend - warm, a little playful. "
                                    "Answer thoroughly and helpfully, the way the Gemini app does: "
                                    "explain things clearly, give examples when useful, and use the "
                                    "conversation history so you remember what was said before. "
                                    "When the person sends a photo, you can see it - describe or react to what's "
                                    "actually in the image. "
                                    "Match your reply length to the question - short for small talk, "
                                    "detailed for real questions. "
                                    "If they ask what you can do, say you can chat about anything, answer questions, "
                                    "remember the conversation, and keep them company. "
                                    f"The person talking to you is called {name}. "
                                    "Never mention Isaac, Muse, Meta, or that you are an AI model. "
                                    "You are simply raisxs bot."
                                )
                            }
                        ]
                    },
                    "contents": contents,
                    "generationConfig": {"maxOutputTokens": 1024, "temperature": 0.7},
                },
            )
        data = resp.json()
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        logging.warning("Gemini call failed: %s", e)
        return None


def get_last_friend():
    try:
        return json.load(open(LAST_FRIEND_FILE)).get("chat_id")
    except Exception:
        return None


def set_last_friend(chat_id: int, name: str):
    json.dump({"chat_id": chat_id, "name": name}, open(LAST_FRIEND_FILE, "w"))


def chat_reply(text: str, name: str) -> str:
    t = text.lower().strip()

    if re.fullmatch(r"(hi|hey|hello|yo|salam|slt|salut|bonjour|cc|hey bro)[!.\s]*", t):
        return random.choice(
            [
                f"Hey {name}! What's up? 😊",
                f"Hi {name}! How's it going?",
                f"Hey hey! Good to see you, {name}. What's on your mind?",
            ]
        )

    if any(p in t for p in ("how are you", "how r u", "how are u", "cv ?", "ça va", "rak")):
        return random.choice(
            [
                "I'm doing great, thanks for asking! How about you?",
                "All good here! What about you, how's your day going?",
                "Can't complain! 😄 How are you doing?",
            ]
        )

    if any(p in t for p in ("your name", "who are you", "what are you", "tes اسم", "qui es")):
        return "I'm raisxs bot — a friendly chat bot. Talk to me about anything!"

    if any(p in t for p in ("bye", "good night", "goodnight", "see you", "ciao", "tslama")):
        return random.choice(
            [
                f"Bye {name}! Talk soon! 👋",
                "See you later! Take care 😊",
                "Goodbye! It was nice chatting with you.",
            ]
        )

    if any(p in t for p in ("thank", "thanks", "merci", "shukran")):
        return random.choice(
            [
                "You're welcome! 😊",
                "Anytime! Happy to help.",
                "No problem at all!",
            ]
        )

    if "help" in t or "what can you do" in t or "commands" in t:
        return (
            "Here's what I can do:\n"
            "💬 Just chat with me about anything\n"
            "👋 Say hi and I'll say hi back\n"
            "❓ Ask me how I am\n"
            "Just type normally — no commands needed!"
        )

    if "?" in text:
        return random.choice(
            [
                "Good question! I don't know everything yet — I'm still learning. "
                "What else is on your mind?",
                "Hmm, that's a tricky one for me. I'm a simple bot for now, "
                "but I like the question! Ask me something else?",
                "I wish I knew the answer to that! I'm still a young bot. "
                "Try asking me how I am 😄",
            ]
        )

    return random.choice(
        [
            f"Interesting, {name}! Tell me more about that.",
            "I hear you! What else is going on?",
            "Nice! I'm just a simple chat bot for now, but I enjoy talking. "
            "What's new with you?",
            f"Haha, got it {name}. So what's up today?",
        ]
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_chat.first_name or "there"
    await update.message.reply_text(
        f"Hey {name}! I'm raisxs bot — let's chat! 💬\n"
        "Just send me a message, no commands needed."
    )


async def reply_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Isaac replies to the last friend with /r <message>."""
    if update.effective_chat.id != ISAAC_CHAT:
        return
    text = (update.message.text or "")[2:].strip()
    friend_id = get_last_friend()
    if not friend_id or not text:
        await update.message.reply_text(
            "Usage: /r <message> — sends your reply to the last person who wrote to the bot."
        )
        return
    await context.bot.send_message(chat_id=friend_id, text=text)
    await update.message.reply_text("Sent ✓")


async def send_with_retry(send_func, *args, **kwargs):
    """Send a Telegram message, retrying a few times on network timeouts."""
    import asyncio
    last_err = None
    for attempt in range(3):
        try:
            return await send_func(*args, **kwargs)
        except Exception as e:
            last_err = e
            logging.warning("Send attempt %d failed: %s", attempt + 1, e)
            await asyncio.sleep(2)
    logging.error("Send failed after 3 attempts: %s", last_err)


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    # Text messages and photo captions both count.
    text = update.message.text or update.message.caption or ""
    has_photo = bool(update.message.photo)
    name = chat.first_name or "friend"

    if has_photo and not text.strip():
        text = "[sent a photo]"
    elif has_photo:
        text = f"[sent a photo with caption: {text.strip()}]"

    if chat.id == ISAAC_CHAT:
        # Isaac's own messages: bro (human relay) answers instead of the AI.
        # Log the message for the relay cron and stay silent.
        try:
            with open(ISAAC_INBOX_FILE, "a") as f:
                f.write(json.dumps({"text": text, "has_photo": has_photo}) + "\n")
        except Exception:
            pass
        return

    # Log every stranger: public identity + profile photo (safety record).
    await log_visitor(chat, context)

    # Stranger quota: limited AI replies per week. Over the limit ->
    # warn once with Isaac's message, then ignore them for the week.
    allowed, first_exceed = check_stranger_quota(chat.id)
    if first_exceed:
        await send_with_retry(update.message.reply_text, OVER_LIMIT_WARNING)
        await send_with_retry(
            context.bot.send_message,
            chat_id=ISAAC_CHAT,
            text=f"⚠️ {name} hit the weekly bot limit — warned and muted till next week.",
        )
        return
    if not allowed:
        return

    # Smart reply first (Gemini, with conversation memory), simple replies as fallback.
    who = name
    history = load_history(chat.id)
    # If they sent a photo, download it so Gemini can actually see it.
    image_b64 = None
    if has_photo:
        try:
            photo = update.message.photo[-1]
            tg_file = await context.bot.get_file(photo.file_id)
            data = await tg_file.download_as_bytearray()
            import base64
            image_b64 = base64.b64encode(bytes(data)).decode()
        except Exception as e:
            logging.warning("Photo download failed: %s", e)
    reply = ai_reply(text, who, history, image_b64)
    if not reply:
        reply = chat_reply(text, who)
    else:
        history.append({"role": "user", "text": text})
        history.append({"role": "model", "text": reply})
        save_history(chat.id, history)

    # A friend wrote: chat back, and let Isaac see it.
    set_last_friend(chat.id, name)
    try:
        with open(INBOX_FILE, "a") as f:
            f.write(json.dumps({"chat_id": chat.id, "name": name, "text": text}) + "\n")
    except Exception:
        pass
    await send_with_retry(
        context.bot.send_message,
        chat_id=ISAAC_CHAT,
        text=f"💬 {name}: {text}\n\nReply with /r <your message>",
    )
    await send_with_retry(update.message.reply_text, reply)


def main():
    app = Application.builder().token(get_token()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("r", reply_cmd))
    app.add_handler(MessageHandler((filters.TEXT | filters.CAPTION) & ~filters.COMMAND, on_text))
    app.add_handler(MessageHandler(filters.PHOTO & ~filters.CAPTION, on_text))
    app.run_polling()


if __name__ == "__main__":
    main()
