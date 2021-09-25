from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with !help for the usage of this command or talk to your admin")


def setup(bot):
    bot.add_cog(Basic(bot))
