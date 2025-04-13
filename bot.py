import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils.snapshot import get_latest_proposals

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SNAPSHOT_SPACE_ID = os.getenv("SNAPSHOT_SPACE_ID")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to BlockZhang DAO Alerts!\n\nUse /alerts to see the latest proposal from your Arbitrum DAO."
    )

# /alerts command
async def alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    proposals = get_latest_proposals(SNAPSHOT_SPACE_ID, count=3)

    for prop in proposals:
        message = f"""🗳 *{prop['status']} Proposal*

📌 *{prop['title']}*
📆 Starts: `{prop['start']}`
🕒 Ends: `{prop['end']}`
"""
        proposal_url = f"https://snapshot.org/#/{SNAPSHOT_SPACE_ID}/proposal/{prop['id']}"
        keyboard = [[InlineKeyboardButton("🔗 View Proposal", url=proposal_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_markdown(message, reply_markup=reply_markup)

# Init bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("alerts", alerts))

print("Bot running...")
app.run_polling()

