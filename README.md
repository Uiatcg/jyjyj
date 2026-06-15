# Minecraft Bot

A Python-based Minecraft bot that connects to Minecraft servers and performs automated tasks.

## Features

- ✅ Connects to Minecraft servers
- ✅ Authenticates with Mojang accounts
- ✅ Sends chat messages
- ✅ Auto-respawn support
- ✅ Configurable credentials

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Uiatcg/jyjyj.git
cd jyjyj
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` to set your credentials:

```python
USERNAME = "your_minecraft_username"
PASSWORD = "your_minecraft_password"
SERVER_IP = "play.applemc.fun"
SERVER_PORT = 25565
```

## Usage

Run the bot:
```bash
python bot.py
```

## Server Details

Default server: `play.applemc.fun:25565`

## Security Note

⚠️ **Do NOT commit your credentials to version control!**
- Add `config.py` to `.gitignore` if storing real passwords
- Use environment variables for production deployments

## License

MIT
