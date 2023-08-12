import discord
from discord.ext import commands
from AntiScam import AntiScam

intents = discord.Intents.default()
intents.messages = True  # Habilita la intención de mensajes
intents.message_content = True  # Habilita la intención de contenido de mensaje

whitelist_bug = [454870967932420097]

bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot=bot, whitelist=whitelist_bug, muted_role='Muted', verified_role='Verificado', logs_channel=958857429590880267)

bot.run('OTU4ODYwNTg5OTYxMjAzNzQz.GbsurD.HbwCa4iNH6nhq2KC6SrzR2z4YfZkcIUZFf9Wvc')













