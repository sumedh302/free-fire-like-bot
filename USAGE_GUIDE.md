# 🎮 Free Fire Like Bot - Usage Guide

## 🚀 Quick Start

Your Free Fire Like Bot is now **LIVE** and ready to use! Here's everything you need to know:

---

## 📋 Bot Status

✅ **Bot Connected:** nezuko-chan#3779  
✅ **Guilds Connected:** 2 servers  
✅ **Commands Synced:** 2 slash commands  
✅ **Flask Server:** Running on port 10000  
✅ **API Endpoint:** Working (230/3000 usage)  

---

## 🎯 Available Commands

### 1. `/like <uid>`
**Purpose:** Send likes to a Free Fire player  
**Usage:** `/like 2537964178`  
**Features:**
- ✅ 30-second cooldown per user
- ✅ Channel restrictions (if configured)
- ✅ Beautiful embed responses
- ✅ Shows player info, likes before/after, API usage
- ✅ Smart region fallback (tries India first, then AG if needed)

### 2. `/setlikechannel <channel>`
**Purpose:** Configure which channels can use the `/like` command  
**Usage:** `/setlikechannel #general`  
**Permission Required:** Manage Channels  
**Features:**
- ✅ Toggle channels on/off
- ✅ Shows current allowed channels
- ✅ Saves configuration automatically

---

## 🔧 Configuration

### Current Settings
```
Discord Token: ✅ Configured
API Endpoint: https://likexthug.vercel.app
API Key: GREAT
Default Region: ind (India)
Usage Limit: 3000 requests
Current Usage: 234 requests
```

### Files Structure
```
├── app.py                 # Main bot application
├── cogs/
│   ├── __init__.py
│   └── likeCommands.py    # Discord commands
├── .env                   # Credentials (secure)
├── like_channels.json     # Channel configuration
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

---

## 🎨 Example Responses

### Successful Like Command
```
✅ Likes Sent Successfully!

👤 Player Info
UID: 2537964178
Region: ME
Nickname: ᴮᵐᶜﾠX-sᴋᴀʏ✊

❤️ Likes                    🔑 API Usage
Before: 18,190              Usage: 230/3000
After: 18,190
Added: 0

Requested by YourUsername
```

### Channel Configuration
```
🔧 Channel Configuration Updated
#general has been added to the allowed channels list.

📋 Currently Allowed Channels
#general
#gaming
```

---

## 🛡️ Security Features

- ✅ **Environment Variables:** Sensitive data stored in `.env`
- ✅ **Permission Checks:** Only admins can configure channels
- ✅ **Rate Limiting:** 30-second cooldown per user
- ✅ **Error Handling:** Graceful error messages
- ✅ **Input Validation:** Secure parameter handling

---

## 🌐 Monitoring

### Flask Status Endpoint
**URL:** `http://localhost:10000`  
**Response:**
```json
{
  "status": "active",
  "bot_name": "Free Fire Like Bot",
  "guilds": 2
}
```

### Bot Logs
The bot outputs real-time logs showing:
- Connection status
- Command synchronization
- Guild information
- Error messages (if any)

---

## 🚨 Troubleshooting

### Common Issues

1. **Bot Not Responding**
   - Check if bot is online in Discord
   - Verify bot has necessary permissions
   - Check console for error messages

2. **Commands Not Showing**
   - Wait a few minutes for Discord to sync
   - Try `/` in a channel to see available commands
   - Restart the bot if needed

3. **API Errors**
   - Check API usage limit (currently 230/3000)
   - Verify API endpoint is accessible
   - Check network connectivity

4. **Permission Errors**
   - Ensure bot has required permissions in server
   - Check channel-specific permissions
   - Verify user has manage channels permission for `/setlikechannel`

---

## 📞 Support Commands

### Restart Bot
```bash
# Stop current bot (Ctrl+C)
python app.py
```

### Test API Connection
```bash
python test_api.py
```

### Check Status
```bash
curl http://localhost:10000
```

---

## 🎉 Ready to Use!

Your Free Fire Like Bot is fully operational and ready for your Discord server! 

**Next Steps:**
1. Invite the bot to your Discord servers
2. Use `/setlikechannel` to configure allowed channels
3. Start using `/like <uid>` to send likes to Free Fire players
4. Monitor usage through the Flask endpoint

**Have fun gaming! 🎮**
