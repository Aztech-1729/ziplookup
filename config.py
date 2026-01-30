# Telegram Bot Configuration

# Bot Token from @BotFather
BOT_TOKEN = "8590221101:AAHia-LlDgx0sPmHcmDq4voL6UPFlVbiylo"

# API ID from my.telegram.org
API_ID = "36345385"

# API Hash from my.telegram.org
API_HASH = "738ba4acd0d4b025e97051a51479a407"

# Source Channel Peer ID (channel with .7z files)
SOURCE_CHANNEL_ID = -1003811969023

# Extracted Files Channel ID (will be created automatically on first run, leave as None)
EXTRACTED_CHANNEL_ID = -1003740062026

# Admin User IDs (receive notifications)
ADMIN_IDS = [6670166083, 5525319674]

# Memory Cache Settings
MAX_CACHE_SIZE_MB = 4096  # Maximum memory cache size in MB (4GB for 8GB VPS - leaves 4GB for system)
ENABLE_FULL_CACHE = True  # Set to True to load files into RAM (up to MAX_CACHE_SIZE_MB), False for on-demand loading

# For datasets larger than RAM:
# - Bot will load files until MAX_CACHE_SIZE_MB is reached
# - Remaining files will be searched on-demand from channel
# - Example: 10TB data, 4GB RAM → First 4GB cached (ultra-fast), rest on-demand (5-10s per search)
