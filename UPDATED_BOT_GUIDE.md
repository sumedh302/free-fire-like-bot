# 🎮 Updated Free Fire Like Bot - User Guide

## ✅ What's New

The bot has been updated with a **region selection feature**! Users can now specify the region when using the `/like` command.

### 🆕 New Command Format

**Before:**
```
/like 1901984169
```

**Now:**
```
/like 1901984169 ind
/like 2537964178 me
/like 1192757057 bg
```

## 🎯 Command Usage

### `/like <uid> [region]`

**Parameters:**
- `uid` (required): The Free Fire user ID
- `region` (optional): The player's region (default: `ind`)

**Available Regions:**
- `ind` - India
- `bg` - Bangladesh  
- `me` - Middle East
- And other regions supported by the API

**Examples:**
```
/like 1901984169          # Uses default region (ind)
/like 1901984169 ind      # Indian player
/like 2537964178 me       # Middle East player
/like 1192757057 bg       # Bangladesh player
```

## 🔧 Updated API Integration

**New API Endpoint:**
```
https://likexthug.vercel.app/like?uid={uid}&region={region}&key=GREAT
```

**Changes Made:**
- ✅ Removed old fallback mechanism
- ✅ Added region parameter to command
- ✅ Users can now specify exact region
- ✅ Cleaner, more direct API calls
- ✅ Better error messages with region info

## 🎨 Updated Bot Responses

### ✅ Success Response
```
✅ Likes Sent Successfully!

👤 Player Info
UID: 1901984169
Region: IND
Nickname: SʀㅤᏚᴀʜɪʟ!!

❤️ Likes                    🔑 API Usage
Before: 15,229              Usage: 267/3000
After: 15,229
Added: 0

Requested by Username
```

### ❌ Player Not Found
```
❌ Player Not Found

UID 123456789 not found in region IND.

Please check:
• UID is correct
• Player exists in Free Fire
• Region is correct (try: ind, bg, me, etc.)
• UID format is valid
```

### 🔌 Connection Error
```
❌ Connection Error

HTTP error: 400
Region: ME
```

## 🚀 Bot Features

### ✅ Current Features
- **Region Selection**: Users can specify player region
- **Default Region**: Uses `ind` (India) if no region specified
- **Smart Error Handling**: Clear messages for different error types
- **Channel Restrictions**: `/setlikechannel` for admin control
- **Cooldown System**: 30-second per-user cooldown
- **Beautiful Embeds**: Color-coded Discord responses

### ✅ Admin Features
- **Channel Control**: `/setlikechannel <channel>` to restrict usage
- **Permission-Based**: Only "Manage Channels" permission can configure
- **Persistent Settings**: Configuration saved automatically

## 🧪 Testing Results

**Working Regions:**
- ✅ `ind` (India) - Fully tested and working
- ❓ `me` (Middle East) - May have API limitations
- ❓ `bg` (Bangladesh) - Needs testing

**Recommendations:**
- Use `ind` for Indian players (confirmed working)
- Test other regions as needed
- Bot will show clear error messages if region doesn't work

## 🎉 Ready to Use!

The updated bot is now live and ready for use in your Discord server!

**How to Use:**
1. Type `/like` in Discord
2. Enter the UID
3. Optionally specify region (defaults to `ind`)
4. Bot will send likes and show results

**Example Usage:**
- `/like 1901984169` - Uses India region by default
- `/like 1901984169 ind` - Explicitly uses India region
- `/like 2537964178 me` - Uses Middle East region

The bot now provides more control and clearer feedback for all users! 🎮
