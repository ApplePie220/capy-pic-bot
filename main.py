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

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # если сообщение юзера содержит в себе слово капибар, то выдаем картиночку
    if 'капибар' in message.content.lower():
        response = requests.get('https://api.capy.lol/v1/capybara?json=true')  # Get-запрос
        json_data = json.loads(response.text)['data']  # Извлекаем JSON
        await message.channel.send(json_data['url'])


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
