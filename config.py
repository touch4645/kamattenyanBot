# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
DISCORD_SERVER_ID = os.getenv('DISCORD_SERVER_ID').split(',')
NOTIFIED_TEXT_CHANNEL_ID = os.getenv('NOTIFIED_TEXT_CHANNEL_ID').split(',')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
