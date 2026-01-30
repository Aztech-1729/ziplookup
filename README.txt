TELEGRAM BREACH LOOKUP BOT
==========================

SETUP INSTRUCTIONS:
-------------------

1. Install required packages:
   pip install -r requirements.txt

2. Configure the bot:
   - Open config.py
   - Add your BOT_TOKEN (from @BotFather)
   - Add your API_ID (from https://my.telegram.org)
   - Add your API_HASH (from https://my.telegram.org)
   - Add your CHANNEL_PEER_ID (channel username with @ or channel ID like -1001234567890)

3. Run the bot:
   python bot.py

4. On first run, you will be prompted to:
   - Enter your phone number (with country code, e.g., +1234567890)
   - Enter the verification code sent to your Telegram
   - This creates a user session to access the private channel
   
5. The bot will automatically:
   - Download all .7z files from the source channel
   - Extract them locally
   - Create a NEW private channel called "Extracted Breach Files"
   - Upload all extracted .txt files to the new channel
   - Send notifications to admins about progress
   - Share the channel link with admins
   
6. On subsequent runs:
   - Bot will use the existing extracted files channel
   - No re-extraction needed unless you delete the channel
   - Searches are performed directly on channel files

AVAILABLE COMMANDS:
-------------------
/start - Show help message
/domain <domain> - Search for domain breaches
/email <email> - Search for email breaches
/num <number> - Search for phone number
/aadhar <number> - Search for Aadhar number
/pan <number> - Search for PAN card
/ps <password> - Search for password
/tg <username> - Search for Telegram username
/ig <username> - Search for Instagram username
/fb <username> - Search for Facebook username
/lk <username> - Search for LinkedIn username
/x <username> - Search for Twitter/X username
/yt <channel> - Search for YouTube channel
/wa <number> - Search for WhatsApp number
/bi <term> - Search for Binance related data
/ot <text> - General text search (name, any text)

FEATURES:
---------
- ⚡ BLAZING FAST in-memory search (no file downloads during search)
- ⚡ Parallel extraction with thread pool (2x faster processing)
- ⚡ Automatic archive cleanup after extraction (saves disk space)
- ⚡ Progress tracking with download/extract timing
- ✅ Automatic channel creation for extracted files
- ✅ One-time extraction (no repeated extraction on restarts)
- ✅ Smart file tracking (remembers processed archives)
- ✅ Admin notifications for all operations
- ✅ Results returned with timing information
- ✅ Results sent as downloadable .txt files
- ✅ Support for multiple data types and breach formats
- ✅ Public access - anyone can use search commands

ADMIN FEATURES:
---------------
- Receive notifications when:
  * Channel is created
  * Files are being downloaded/extracted
  * Files are being uploaded to channel
  * Upload progress (every 10 files)
  * Upload complete
  * Any errors occur
- Get channel link when created

NOTES:
------
- First run will take time to download, extract, and upload all files
- A new private channel will be automatically created
- Extracted files are stored in Telegram channel (saves local storage)
- Local ./cache directory only used temporarily during extraction
- Subsequent runs will use existing channel files (much faster)
- The EXTRACTED_CHANNEL_ID in config.py is auto-updated after channel creation

SMART TRACKING:
---------------
- Bot creates a "processed_archives.txt" file to track all processed .7z files
- On restart, bot checks this file and skips already processed archives
- Only new .7z files (not in tracking file) will be downloaded and extracted
- This prevents re-processing the same files and creating duplicate channels
- If you want to re-process everything, delete "processed_archives.txt"

ULTRA-FAST PERFORMANCE:
-----------------------
Large Archive Handling (500MB-1GB):
- Download speed: Depends on your internet connection
- Extraction: Uses parallel thread pool for non-blocking extraction
- Archive cleanup: Automatically deletes .7z after extraction to save space
- Memory loading: All extracted text-based files loaded into RAM for instant search

File Type Support:
- ✅ Supports ALL file types in .7z archives
- ✅ Automatically detects text-based files for search indexing
- ✅ Supported text extensions: .txt, .log, .csv, .json, .xml, .sql, .dat, .list, .dump, .leak, and more
- ✅ Files without extensions are auto-detected
- ✅ Binary files (.exe, .dll, .zip, etc.) are skipped from search index
- ✅ ALL files uploaded to channel (text and binary)

Search Performance:
- ⚡ INSTANT search - all text data stored in memory (RAM)
- No file downloads during search (unlike slow bots)
- Typical search time: 0.5s - 3s for millions of lines
- Results limited only by your RAM size
- Searches across ALL text-based files regardless of extension

Example Performance:
- 1GB archive → ~60-120s download (depends on internet)
- Extraction → ~30-60s (parallel processing)
- Loading to memory → ~10-30s (only text files)
- Search → ~1-2s (BLAZING FAST!)
