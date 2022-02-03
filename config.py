# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
NOTIFIED_TEXT_CHANNEL_ID = os.getenv('NOTIFIED_TEXT_CHANNEL_ID')
WATCHED_VOICE_CHANNEL_ID = os.getenv('WATCHED_VOICE_CHANNEL_ID')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_SERVER_ID = os.getenv('DISCORD_SERVER_ID')
