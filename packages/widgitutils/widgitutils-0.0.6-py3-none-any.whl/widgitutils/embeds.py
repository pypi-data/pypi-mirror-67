from redbot.core import commands
from discord import Colour, Embed, TextChannel
from discord.embeds import EmptyEmbed
import datetime


async def build_embed(parent, ctx: commands.Context, **kwargs):
    """
    Helper to determine whether or not an embed should be used
    """

    return await WidgitEmbed(parent).build(ctx, **kwargs)


class WidgitEmbed:
    def __init__(self, parent):
        self.parent = parent

    async def build(self, ctx: commands.Context, **kwargs):
        """
        Helper to determine whether or not an embed should be used
        """

        if commands.bot_has_permissions(embed_links=True):
            return await self._embed_msg(ctx, **kwargs)

        fallback = kwargs.get("post") or None

        if fallback:
            return await ctx.send(fallback)

        raise WidgitEmbedException(
            self.parent._(
                "I doesn't have permission to post embeds and no fallback post was given!"
            )
        )

    async def _embed_msg(self, ctx: commands.Context, **kwargs):
        """
        Build and display an embed
        """

        color = kwargs.get("colour") or kwargs.get("color") or None

        if not color:
            color = await self._get_embed_color(ctx.channel)

        title = kwargs.get("title", EmptyEmbed) or EmptyEmbed
        _type = kwargs.get("type", "rich") or "rich"
        url = kwargs.get("url", EmptyEmbed) or EmptyEmbed
        description = kwargs.get("description", EmptyEmbed) or EmptyEmbed
        timestamp = kwargs.get("timestamp")
        footer = kwargs.get("footer") or kwargs.get("footer_text")
        footer_icon = kwargs.get("footer_icon")
        thumbnail = kwargs.get("thumbnail")
        image = kwargs.get("image")
        channel = kwargs.get("channel") or ctx

        contents = dict(title=title, type=_type, url=url, description=description)

        embed = kwargs.get("embed") or EmptyEmbed
        embed = embed.to_dict() if hasattr(embed, "to_dict") else {}

        contents.update(embed)

        if timestamp and isinstance(timestamp, datetime.datetime):
            contents["timestamp"] = timestamp

        embed = Embed.from_dict(contents)

        embed.color = color

        if footer:
            if footer_icon:
                embed.set_footer(text=footer, icon_url=footer_icon)
            else:
                embed.set_footer(text=footer)

        if thumbnail:
            embed.set_thumbnail(url=thumbnail)

        if image:
            embed.set_image(url=image)

        return await channel.send(embed=embed)

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


class WidgitEmbedException(Exception):
    """
    Exception handler for WidgetEmbed
    """
