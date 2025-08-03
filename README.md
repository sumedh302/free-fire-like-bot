# 🔍 Free Fire Like Bot

[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://img.shields.io/badge/status-active-brightgreen)

A Discord bot and Flask server that allows you to automatically like Free Fire profiles via their user ID.  
Includes advanced features like channel restrictions, cooldowns, JSON config, and support for both RapidAPI and a self-hosted API.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🧰 Requirements](#-requirements)
- [⚙️ Installation](#-installation)
- [💬 Usage](#-usage)
- [🤖 Create a Discord Bot](#-create-a-discord-bot)
- [🌐 Custom or Public API](#-custom-or-public-api)
- [📤 Example Output](#-example-output)
- [🛠 Technologies Used](#-technologies-used)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

## 🚀 Features

- ✅ `/like <uid>`: Send likes to Free Fire users (tries India first, fallback to AG).
- 🔐 `/setlikechannel <channel>`: Restrict usage to selected channels.
- 🔁 Per-user cooldown (30 seconds).
- 🧠 Channel config saved in `like_channels.json`.
- 📡 Flask web server at `http://localhost:10000` for status.
- 🔑 Secure token/key storage via `.env`.
- 🌐 Choose between RapidAPI or your own hosted API.
- 📊 Embedded responses with like count before/after.

---

## 🧰 Requirements

- Python 3.8+
- A Discord bot token
- A RapidAPI key **or** a self-hosted API server
- A `.env` file containing:

```
TOKEN=your_discord_bot_token
RAPIDAPI_KEY=your_rapidapi_key_or_custom_api_key
API_HOST=https://your-api-endpoint.com
```

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/paulafredo/free-freefire-like-bot
   cd free-freefire-like-bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your credentials:
   ```
   TOKEN=your_discord_bot_token
   RAPIDAPI_KEY=your_rapidapi_key_or_empty_if_custom
   API_HOST=https://your-api-endpoint.com
   ```

5. Run the bot:
   ```bash
   python app.py
   ```

## 💬 Usage

- Use `/like <user_id>` in a Discord server where the bot is present.
- Use `/setlikechannel <channel>` to toggle allowed channels for the like command.

## 🛠️ Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"**, and give your bot a name.
3. In the left sidebar, go to the **"Bot"** section and click **"Add Bot"**, then confirm with **"Yes, do it!"**.
4. Under the **Token** section, click **"Reset Token"** or **"Copy"** to get your `TOKEN`.
5. Go to **"General Information"** and copy the `APPLICATION_ID`.
6. Paste both values into your `.env` file:
   ```
   TOKEN=your_bot_token
   ```

## 🌐 Custom or Public API

### ✅ Option 1: Use RapidAPI

1. Go to [Free Fire Like API on RapidAPI](https://rapidapi.com/greatthug/api/free-fire-like1).
2. Subscribe and get your API key.
3. Paste it in your `.env` file:
   ```
   RAPIDAPI_KEY=your_key_here
   ```

### ✅ Option 2: Use Your Own Api

1. Host your own version of the API: [Free Fire Like api](https://github.com/paulafredo/free-api-like-freefire).
2. In your `.env` file, set:
   ```
   API_HOST=http://localhost:5000  # or your public server URL
   RAPIDAPI_KEY=your_custom_key
   ```

## 📤 Example Output

The bot will respond with embedded messages showing:
- Player information (UID, region, nickname)
- Like counts (before/after)
- API usage statistics

## 🛠 Technologies Used

- Python
- Discord.py
- Flask
- dotenv
- aiohttp

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it.

## 👨‍💻 Author

[Paul Alfredo](https://github.com/paulafredo)
