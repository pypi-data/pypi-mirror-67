from discord import Colour, TextChannel
from re import search
from redbot.core import commands


async def from_hex(parent, ctx: commands.Context, color: str):
    """
    Helper to convert hex colors into Discord colors
    """

    await WidgitColor(parent).from_hex(ctx, color)


async def get(parent, ctx: commands.Context, color: str):
    """
    Convert a color string to its appropriate Discord color
    """

    await WidgitColor(parent).get(ctx, color)


async def pick(parent, ctx: commands.Context, **kwargs):
    """
    Helper to simplify picking Discord-compatible colors
    """

    await WidgitColor(parent).pick(ctx, **kwargs)


class WidgitColor:

    def __init__(self, parent):
        self.parent = parent

    async def from_hex(self, ctx: commands.Context, color: str):
        """
        Helper to convert hex colors into Discord colors
        """

        color = color.lstrip("#")
        color = color.lstrip("0x")

        if len(color) == 3:
            color = color + color

        if len(color) == 6 and search(r'^(?:[0-9a-fA-F]{3}){1,2}$', color):
            color = tuple(int(color[i:i+2], 16) for i in(0, 2, 4))

            return Colour.from_rgb(*color)

        return await self._get_embed_color(ctx.channel)

    async def get(self, ctx: commands.Context, color: str):
        """
        Convert a color string to its appropriate Discord color
        """

        colors = {
            "teal": "0x1abc9c",
            "dark_teal": "0x11806a",
            "green": "0x2ecc71",
            "dark_green": "0x1f8b4c",
            "blue": "0x3498db",
            "dark_blue": "0x206694",
            "purple": "0x9b59b6",
            "dark_purple": "0x71368a",
            "magenta": "0xe91e63",
            "dark_magenta": "0xad1457",
            "gold": "0xf1c40f",
            "dark_gold": "0xc27c0e",
            "orange": "0xe67e22",
            "dark_orange": "0xa84300",
            "red": "0xe74c3c",
            "dark_red": "0x992d22",
            "lighter_grey": "0x95a5a6",
            "dark_grey": "0x607d8b",
            "light_grey": "0x979c9f",
            "darker_grey": "0x546e7a",
            "blurple": "0x7289da",
            "greyple": "0x99aab5"
        }

        if color in colors:
            return await self.from_hex(ctx, colors[color])

        return await self.from_hex(ctx, color)

    async def pick(self, ctx: commands.Context, **kwargs):
        """
        Helper to simplify picking Discord-compatible colors
        TODO: Add an actual color picker!
        """

    async def _get_embed_color(self, channel: TextChannel) -> Colour:
        """
        Return the default color for an embed
        """

        try:
            if await self.parent.bot.db.guild(channel.guild).use_bot_color():
                return channel.guild.me.colour

            return await self.parent.bot.db.color()
        except AttributeError:
            return await self.parent.bot.get_embed_colour(channel)
