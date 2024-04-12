import discord
from discord.ext import commands

from model import get_class
import os
import requests






intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{file_name}')
            await ctx.send(get_class(model_path='./keras_model.h5', labels_path='labels.txt', image_path=f'./{file_name}'))
    else:
        await ctx.send('Картинка нема :3')











bot.run("MTE2NTE5MzQ3Nzc2MDQ4NzQ0NQ.GLBR5w.8vodHRlE6nyeUbBsw9IYy2_AXdRs53FKDqWoAo")