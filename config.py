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

# Search Mode
USE_DATABASE_INDEX = True  # Use SQLite database for indexing (recommended for 10M+ files)
ENABLE_FULL_CACHE = False  # Legacy: Load all files into RAM (not recommended for large datasets)
MAX_CACHE_SIZE_MB = 4096  # Only used if ENABLE_FULL_CACHE = True

# Database Index Mode (USE_DATABASE_INDEX = True):
# - Indexes all files into SQLite database during upload
# - Search time: 0.5-2s even with 10 MILLION files!
# - Disk usage: ~10-20% of original data size for index
# - RAM usage: Minimal (~100-200MB)
# - Perfect for VPS with limited RAM but large datasets
