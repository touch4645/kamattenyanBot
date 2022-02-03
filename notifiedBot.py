import discord
import config
from datetime import datetime, timedelta

client = discord.Client()

# Bot起動
@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# チャンネル入室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):
    # メンバーのギルドが対応サーバーかどうか確認する
    if member.guild.id == int(config.DISCORD_SERVER_ID):

        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        text_ch = client.get_channel(int(config.NOTIFIED_TEXT_CHANNEL_ID))

        # 入室通知
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            print(msg)
            await text_ch.send(msg)

        # 退室通知
        if before.channel is None:
            msg = f'{member.name} が退室しました。'
            print(msg)
            await text_ch.send(msg)

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(config.DISCORD_BOT_TOKEN)