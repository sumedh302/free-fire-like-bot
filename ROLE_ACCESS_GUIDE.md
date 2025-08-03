# 🔐 Role-Based Access Control - Free Fire Like Bot

## ✅ New Security Feature Added

The bot now includes **role-based access control**! Only users with specific roles can use the `/like` command.

## 🎯 Available Commands

### For Regular Users:
- `/like <uid> [region]` - Send likes (requires allowed role)

### For Admins:
- `/setlikechannel <channel>` - Configure allowed channels (requires Manage Channels permission)
- `/setrole <role>` - Configure allowed roles (requires Manage Roles permission)

## 🔧 Setting Up Role Access

### Step 1: Configure Allowed Roles
Use the `/setrole` command to set which roles can use the bot:

```
/setrole @VIP Members
/setrole @Premium Users
/setrole @Free Fire Players
```

### Step 2: Toggle Roles
Running `/setrole` again with the same role will remove it:

```
/setrole @VIP Members  # Adds the role
/setrole @VIP Members  # Removes the role
```

## 🎨 Bot Responses

### ✅ Role Added
```
🔧 Role Configuration Updated
@VIP Members has been added to the allowed roles list.

📋 Currently Allowed Roles
@VIP Members
@Premium Users
```

### ❌ Access Denied
```
❌ Access Denied
You don't have the required role to use this bot. Contact an admin to get access.
```

### 📋 No Role Restrictions
```
📋 Currently Allowed Roles
All users (no role restrictions)
```

## 🛡️ Security Features

### Default Behavior:
- **No roles configured**: All users can use the bot
- **Roles configured**: Only users with specified roles can use the bot
- **Multiple roles**: Users need ANY of the allowed roles (not all)

### Permission Requirements:
- **`/setrole`**: Requires "Manage Roles" permission
- **`/setlikechannel`**: Requires "Manage Channels" permission
- **`/like`**: Requires allowed role (if configured)

### Access Control Flow:
1. User runs `/like` command
2. Bot checks if user has any allowed role
3. If no roles configured → Allow access
4. If roles configured → Check user's roles
5. If user has allowed role → Continue with command
6. If user lacks role → Show access denied message

## 📁 Configuration Files

### `allowed_roles.json`
Stores role configurations per guild:
```json
{
  "1385109245443182662": [
    123456789012345678,
    987654321098765432
  ]
}
```

### `like_channels.json`
Stores channel configurations per guild:
```json
{
  "1385109245443182662": [
    111222333444555666,
    777888999000111222
  ]
}
```

## 🎮 Usage Examples

### Admin Setup:
```
Admin: /setrole @Free Fire VIP
Bot: 🔧 Role Configuration Updated
     @Free Fire VIP has been added to the allowed roles list.
```

### User Access:
```
VIP User: /like 1901984169 ind
Bot: ✅ Likes Sent Successfully! (normal response)

Regular User: /like 1901984169 ind
Bot: ❌ Access Denied
     You don't have the required role to use this bot.
```

## 🔄 Managing Access

### Add Multiple Roles:
```
/setrole @VIP Members
/setrole @Premium Users
/setrole @Moderators
```

### Remove Role Access:
```
/setrole @VIP Members  # Removes if already added
```

### Check Current Roles:
Run `/setrole` with any role to see the current configuration in the response.

## 🎉 Benefits

### For Server Owners:
- **Control Access**: Limit bot usage to specific user groups
- **Monetization**: Restrict access to premium/VIP members
- **Moderation**: Prevent spam by limiting access
- **Organization**: Keep bot usage organized by roles

### For Users:
- **Clear Feedback**: Know exactly why access is denied
- **Role-Based Perks**: Understand the value of having specific roles
- **Fair Usage**: Controlled access prevents abuse

## 🚀 Ready to Use!

The role-based access control is now active! Admins can use `/setrole` to configure which roles can access the `/like` command, providing complete control over bot usage in their Discord server.
