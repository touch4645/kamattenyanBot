import discord
import config
from datetime import datetime, timedelta

client = discord.Client()

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after): 

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if member.guild.id == config.WATCHED_VOICE_CHANNEL_ID and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        alert_channel = client.get_channel(config.NOTIFIED_TEXT_CHANNEL_ID)

        # 退室通知
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

        # 入室通知
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(config.DISCORD_BOT_TOKEN)