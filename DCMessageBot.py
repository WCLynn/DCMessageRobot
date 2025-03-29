
import discord
from discord.ext import commands
import os
from KeepAlive import keep_alive

# 設定機器人指令前綴
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
#當機器人完成啟動時
async def on_ready():
    game = discord.Game('裝忙中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print(f"已登入為 {bot.user}")
    
@bot.event    
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@bot.command()
async def close(ctx):
    """關閉機器人"""
    await ctx.send("關閉機器人中")
    await bot.close()
    
    
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  keep_alive()
  bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e