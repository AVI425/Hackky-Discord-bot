import discord, time, asyncio
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import command

class message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #RENAME COMMAND
    @commands.command(pass_context=True)
    async def rename(self, ctx, rename_to):
        await ctx.message.delete()
        for member in list(self.bot.get_all_members()):
            try:
                await member.edit(nick=rename_to)
                print(f"{member.name} has been renamed to {rename_to}")
            except:
                print(f"{member.name} has NOT been renamed")
            print("Action completed: Rename all")

    #DM COMMAND
    @commands.command(pass_context=True)
    async def dm(self, ctx, user_message):
        await ctx.message.delete()
        for member in list(self.bot.get_all_members()):
            await asyncio.sleep(0)
            try:
                await member.send(f"{user_message}")
            except:
                pass
            print("Action completed: Message all")

def setup(bot):
    bot.add_cog(message(bot))