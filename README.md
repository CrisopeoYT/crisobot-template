
# 🤖 CrisoBot Template

A **free and powerful template** to create your own Discord bot using Python 3.11+ (64-bit), developed by [Crisopeo](https://www.youtube.com/@Crisopeo).  
This bot includes user commands, admin tools, multilingual support (🇮🇹 🇬🇧 🇪🇸 🇯🇵), and useful utilities for any server.

> ⭐ If you use this template to build your own bot, please consider **crediting Crisopeo**!

---

## 📦 Required Libraries

Make sure you have **Python 3.11 (64-bit)** installed.  
Install the required libraries with:

```bash
pip install -U discord.py
```

> The following libraries are used (all standard or included in `discord.py`):
- `discord`, `discord.ext.commands`, `discord.app_commands`
- `asyncio`
- `json`
- `os`

---

## 🚀 Quick Start

### Replace your bot token

Open the Python file (e.g., `main.py`) and **replace** the string `"BOT TOKEN"` at the end with your personal token:

```python
bot.run("YOUR_BOT_TOKEN")
```

> 🔐 Never share your bot token with anyone!

---

## 🌐 Language Support

The bot supports multiple languages for commands and messages:

- 🇬🇧 English
- 🇮🇹 Italian (default)
- 🇪🇸 Spanish
- 🇯🇵 Japanese

You can change your preferred language using the `/set_language` slash command.

---

## 🔧 Included Commands

### 👤 User Commands
```bash
!ping             # Show bot latency
!language         # Show or set your language
!helpme           # Show user command list
!afk              # Toggle AFK mode
!qea <number>     # Answer predefined Q&A
!qeahelp          # Show Q&A list
```

### 🔒 Admin Commands
```bash
!helpmeadmin                  # Show admin command list
!createchannel <name> <type> # Create text/voice channel
!createrole <name> <#color>  # Create a HEX-colored role
!modchannel <#channel> <new_name> # Rename a channel
!modrole <@role> <#color>    # Change role color
!rolestemplate <template>    # Create roles from template
!shutdown                    # Shut down the bot
```

---

## 🧠 Special Features

- ✨ **AFK Mode**: Sets a visible AFK tag in nickname
- 🌍 **User-specific language preferences** saved in `lang_prefs.json`
- 💬 **Slash + prefix commands** supported
- 📚 **Built-in Q&A** for educational bots

---

## 📁 Main Files

- `main.py` – The main bot script
- `lang_prefs.json` – User language preferences
- `README.md` – This file

---

## ❤️ Support Crisopeo

- YouTube: [@Crisopeo](https://www.youtube.com/@Crisopeo)
- Discord: *[Click here to open](https://discord.gg/bGsvKC6JTP)*

---

## 📄 License

This project is free to use.  
You’re welcome to modify or extend it for your needs. If published, **crediting Crisopeo is appreciated**.
