import discord
from discord.ext import commands
import random

# 設定
TOKEN = 'あなたのBOTトークンをここに貼り付け'
# 反応するキーワードリスト
KEYWORDS = ['淫夢', '先輩', 'いいよ', 'こいよ', '114514']
# 返信用の語録リスト
RESPONSES = ['いいよ！こいよ！', '冷えてるか～？', 'やったぜ。', 'やりますねぇ！', 'ホモは嘘つき']
# 返信する確率 (0.1 = 10%)
PROBABILITY = 0.3

# Botの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました')

@bot.event
async def on_message(message):
    # 自分自身のメッセージには反応しない
    if message.author == bot.user:
        return

    # メッセージの中にキーワードが含まれているかチェック
    if any(keyword in message.content for keyword in KEYWORDS):
        # 指定した確率で実行
        if random.random() < PROBABILITY:
            response = random.choice(RESPONSES)
            await message.channel.send(response)

    # これがないと他のコマンドが動かなくなる
    await bot.process_commands(message)

bot.run(TOKEN)
