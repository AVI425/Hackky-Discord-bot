import discord, time, asyncio
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import command

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #KICK COMMAND
    @commands.command(pass_context=True)
    async def kick(self, ctx):
        await ctx.message.delete()
        guild = ctx.message.guild
        for member in list(self.bot.get_all_members()):
            try:
                await guild.kick(member)
                print(f"{member.name} has been kicked")
            except:
                print(f"{member.name} has FAILED to be kicked")
            print("Action completed: Kick all")

    #BAN COMMAND
    @commands.command(pass_context=True)
    async def ban(self, ctx):
        await ctx.message.delete()
        guild = ctx.message.guild
        for member in list(self.bot.get_all_members()):
            try:
                await guild.ban(member)
                print("User " + member.name + " has been banned")
            except:
                pass
        print("Action completed: Ban all")

def setup(bot):
    bot.add_cog(moderation(bot))