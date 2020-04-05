import asyncio
import discord
from datetime import datetime
from discord.ext import commands


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.get_cog('Database')

    @commands.group(name="cog", aliases=['cogs'])
    @commands.is_owner()
    async def cog(self, ctx):
        if ctx.invoked_subcommand is None:
            cog_embed = discord.Embed(
                description='``>cog load {cog}`` Loads the mentioned cog\n\n'
                            '``>cog unload {cog}`` Unloads the mentioned cog\n\n'
                            '``>cog reload {cog}`` Reloads the mentioned cog\n\n'
                            '``>cog list`` Lists all loaded cogs.',
                color=self.bot.embed)

            await ctx.send(embed=cog_embed)

    @cog.command(name="load")
    async def load_cog(self, ctx, *, cog: str):
        cog = cog.lower()

        if not cog.startswith('cogs.'):
            cog = f'cogs.{cog}'

        self.bot.load_extension(cog)

        cog_embed = discord.Embed(
            description=f'{self.bot.yes} **Successfully loaded** ``{cog}``',
            color=self.bot.embed
        )
        await ctx.send(embed=cog_embed)

    @cog.command(name="unload")
    async def unload_cog(self, ctx, *, cog: str):
        cog = cog.lower()

        if not cog.startswith('cogs.'):
            cog = f'cogs.{cog}'

        self.bot.unload_extension(cog)

        cog_embed = discord.Embed(
            description=f'{self.bot.yes} **Successfully unloaded** ``{cog}``',
            color=self.bot.embed
        )
        await ctx.send(embed=cog_embed)

    @cog.command(name="reload")
    async def reload_cog(self, ctx, *, cog: str):
        cog = cog.lower()

        if not cog.startswith('cogs.'):
            cog = f'cogs.{cog}'

        self.bot.reload_extension(cog)

        cog_embed = discord.Embed(
            description=f'{self.bot.yes} **Successfully reloaded** ``{cog}``',
            color=self.bot.embed
        )
        await ctx.send(embed=cog_embed)

    @cog.command(name="list")
    async def list_cogs(self, ctx):
        cogs = ',\n'
        cog_list = list(self.bot.cogs)

        for cog in cog_list:
            cog_list[cog_list.index(cog)] = f'``{cog}``'

        cogs = cogs.join(cog_list)
        cogs_embed = discord.Embed(
            description=cogs,
            color=self.bot.embed
        )
        await ctx.send(embed=cogs_embed)

    @commands.command(
        usage=f'``>restart``',
        help='Force restarts the bot.'
    )
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send(f'{  self.bot.yes} **Restarting the bot.**')
        await self.bot.logout()
        exit()


def setup(bot):
    bot.add_cog(Owner(bot))