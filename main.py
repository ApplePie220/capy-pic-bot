import discord
from discord.ext import commands
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
settings = {
    'token': os.getenv('TOKEN'),
    'bot': 'sirBara',
    'id': os.getenv('ID_BOT'),
    'prefix': ''
}

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command()
async def капибара(ctx):
    response = requests.get('https://api.capy.lol/v1/capybara?json=true')  # Get-запрос
    json_data = json.loads(response.text)['data']  # Извлекаем JSON
    await ctx.send(json_data['url'])


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
