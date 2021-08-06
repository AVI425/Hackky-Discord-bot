import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.core import command


class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #PING COMMAND
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.message.delete()
        member = ctx.message.author
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await channel.trigger_typing()
        t2 = time.perf_counter()
        embed = discord.Embed(title='Ping Test Result.', description='Ping: {}'.format(round((t2 - t1) * 1000)), color=discord.Colour.Red())
        await member.send(embed=embed)
        print("Action completed: Server ping")

    #INFO COMMAND
    @commands.command(pass_context=True)
    async def info(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        member = ctx.message.author
        channel = ctx.message.channel
        if member is None:
            pass
        else:
            await channel.send(
                "**The user's name is: {}**".format(member.name) +
                "\n**The user's ID is: {}**".format(member.id) +
                "\n**The user's current status is: {}**".format(member.status) +
                "\n**The user's highest role is: {}**".format(member.top_role) +
                "\n**The user joined at: {}**".format(member.joined_at))
        print("Action completed: User Info")

def setup(bot):
    bot.add_cog(information(bot))