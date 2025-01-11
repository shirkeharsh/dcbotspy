# Multi-Channel Discord Bot

This is a simple Discord bot that forwards messages and attachments from one channel in a source server to two target channels in different servers. The bot listens for new messages and forwards them, including attachments, while preserving the author's display name.

## Features

- Forwards messages from a source channel to two target channels in different servers.
- Sends both text messages and file attachments.
- Allows for custom server and channel IDs to be specified.
- Changes bot status to invisible upon startup.

## Setup Instructions

### Prerequisites
- Python 3.8+ installed on your machine.
- A Discord bot token. You can create one by following the instructions in the [Discord Developer Portal](https://discord.com/developers/docs/intro).
- The following Python packages:
  - `discord.py` (install via `pip install discord.py`)

### Steps to Deploy

1. Clone the repository or download the `bot.py` file.
   
2. In the `bot.py` file, replace the following placeholders:
   - `SOURCE_SERVER_ID`: The server ID where the bot listens for messages.
   - `SOURCE_CHANNEL_ID`: The channel ID where the bot listens for messages.
   - `TARGET_SERVER_ID_1`: The first target server ID where the bot will forward messages.
   - `TARGET_CHANNEL_ID_1`: The first target channel ID where the bot will forward messages.
   - `TARGET_SERVER_ID_2`: The second target server ID where the bot will forward messages.
   - `TARGET_CHANNEL_ID_2`: The second target channel ID where the bot will forward messages.
   - `BOT_TOKEN`: Your bot's token.

3. Run the bot:
   ```bash
   python bot.py
