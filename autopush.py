import os
import time
from dotenv import load_dotenv
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from utils.snapshot import get_latest_proposals

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SNAPSHOT_SPACE_ID = os.getenv("SNAPSHOT_SPACE_ID")
CHANNEL_ID = "@blockzhang"  # Replace with your channel handle

bot = Bot(token=BOT_TOKEN)
last_seen_id = None

print("🔁 Auto-alert bot is running...")

while True:
    try:
        prop = get_latest_proposals(SNAPSHOT_SPACE_ID)[0]

        if prop["id"] != last_seen_id:
            last_seen_id = prop["id"]

            message = f"""🗳 *New Snapshot Proposal!*

📌 *{prop['title']}*
📆 Starts: `{prop['start']}`
🕒 Ends: `{prop['end']}`
"""
            proposal_url = f"https://snapshot.org/#/{SNAPSHOT_SPACE_ID}/proposal/{prop['id']}"
            keyboard = [[InlineKeyboardButton("🔗 View Proposal", url=proposal_url)]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode="Markdown", reply_markup=reply_markup)
            print(f"✅ Alert sent for proposal ID: {prop['id']}")
        else:
            print("No new proposal. Checking again soon...")

    except Exception as e:
        print(f"❌ Error: {e}")

    time.sleep(300)  # Wait 5 minutes before checking again
