import discord
import random
import requests
from discord.ext import commands


TOKEN = 'Your Token'


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def hola(ctx):
    """Comando que responde con un saludo."""
    await ctx.send(f"¡Hola {ctx.author.name}! ¿Cómo estás?")


@bot.command()
async def meme(ctx):
    """Comando que responde con un meme."""
    url = "https://meme-api.com/gimme"  
    response = requests.get(url)
    meme_data = response.json()
    
    meme_url = meme_data.get("url")
    if meme_url:
        await ctx.send(meme_url)
    else:
        await ctx.send("Lo siento, no pude encontrar un meme en este momento.")


@bot.command()
async def adios(ctx):
    """Comando que responde con una despedida."""
    await ctx.send(f"Adiós {ctx.author.name}! ¡Nos vemos pronto!")


@bot.event
async def on_ready():
    print(f'Nos hemos conectado como {bot.user}')


bot.run(TOKEN)
