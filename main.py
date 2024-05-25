import discord
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
intents.members = True

#Bot prefix
bot=commands.Bot(command_prefix='/', intents=intents)

#Event
@bot.event
async def on_member_join(member):
	get(member.guild.channels, id=)
	await channel.send(f"{member} Welcome to the union.")
