import discord
from discord.ext import commands
import mcrcon
import json

with open('config.json', 'r') as f:
    data = json.load(f)

host = data['servip']
port = int(data['rconport'])
password = data['rconpass']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

rcon_client = mcrcon.MCRcon(host, password, port)
rcon_client.connect()


# Функция проверки наличия роли
def has_required_role(ctx):
    role_id = int(data["roleid"])
    role = ctx.guild.get_role(role_id)
    if role and role in ctx.author.roles:
        return True
    else:
        return False


@bot.command()
@commands.check(has_required_role)
async def sendc(ctx, *, command):
    if ctx.author.bot:
        return
    try:
        response = rcon_client.command(command)
        await ctx.send(f"Response from Minecraft server: {response}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
@commands.check(has_required_role)
async def sendt(ctx, *, text):
    if ctx.author.bot:
        return
    try:
        response = rcon_client.command(f"say {text}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
@commands.check(has_required_role)
async def helpcom(ctx):
    if ctx.author.bot:
        return
    await ctx.send("text = sendt 'text' ")
    await ctx.send("command = sendc 'command' ")


bot.run(data['bottok'])
