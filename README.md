
# DAO Governance Alert Bot 🗳

This Telegram bot tracks and alerts DAO members about new proposals from a given **Snapshot space**. It sends updates directly to your Telegram channel, ensuring no one misses important governance events. Designed to make **decentralized governance more accessible**, it simplifies participation by keeping everyone in the loop, whether proposals are upcoming, active, or closed.

---

## 🧠 Features

- Tracks and fetches proposals from **Snapshot.org**
- Sends proposal **title**, **link**, **start time**, and **end time**
- Alerts for new, upcoming, or closed proposals
- Simple setup using the `.env` file for easy configuration

---

## 📦 Stack

- **Python 3.10+**
- `python-telegram-bot` for Telegram API
- **Snapshot GraphQL API** for DAO proposals
- Environment configuration with `.env` for secrets

---

## 🚀 Demo

👉 **Try it**: [@bzdaobot](https://t.me/bzdaobot) | [@blockzhang](https://t.me/blockzhang)  
Command: `/alerts` to receive the latest proposal update.

---

## ⚙️ Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/blockchang/dao-alert-bot.git
   ```

2. Add your bot’s **Telegram token** and **Snapshot space ID** to the `.env` file (refer to `.env.example` for structure).

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot in separate terminal:
   ```bash
   python bot.py
   ```
   ```bash
   python autopush.py
   ```

---

## 📄 Example Output

Once the bot is running, you’ll get alerts like this:

```
📣 New Snapshot Proposal!

📌 Title: “Enable New Voting Mechanism”
📆 Starts: 2025-04-15 12:00 UTC
🕒 Ends: 2025-04-18 12:00 UTC
🔗 https://snapshot.org/#/your-dao.eth/proposal/abc123
```

---

## 🛠️ Future Enhancements

- **Auto-Push Alerts**: Set up real-time automatic notifications for your DAO’s proposals.
- **Multiple DAO Support**: Easily extend the bot to track more than one DAO space.
- **Real-Time Updates**: Eventually, we’ll replace the polling with webhooks, so the bot can send updates the second a proposal goes live.
- **User Reminders**: I’d love to add inline buttons for reminders or voting alerts to encourage more interaction.

---

## Conclusion

This bot is just the beginning. It’s **simple**, **effective**, and ready for most DAOs that want to improve participation and engagement. I’ve made it with the idea that **community feedback** can shape it into something bigger.

So, if you have ideas or want to collaborate on improving it, feel free to reach out. I’m always open to feedback and new ideas.

---

## Setup

1. Clone the repo:  
   `git clone https://github.com/blockchang/dao-alert-bot.git`

2. Install dependencies:  
   `pip install -r requirements.txt`

3. Set up `.env` with your bot token and Snapshot space ID:
   ```env
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   SNAPSHOT_SPACE_ID=arbitrumfoundation.eth
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

5. Optionally, run the autopush loop (alerts every 5 minutes):
   ```bash
   python autopush.py
   ```

---


Made with ⚙️ by **BlockZhang Labs**  
DM [@blockzhang](https://t.me/blockzhang) for deployment or custom integrations in your DAO.

