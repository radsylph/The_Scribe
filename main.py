import unittest
import discord
from datetime import datetime
from discord import app_commands
from discord.ext import commands, tasks
from decouple import config
from response import Selenium

TOKEN = config("TOKEN")

zip_codes = [{33112: "miami"}, {77450: "katy"}, {77354: "magnolia"}]


WSM = Selenium()


class Bot(commands.Bot):
    def __init__(self, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix="!", intents=intents, case_insensitive=True)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        await self.tree.sync()


intents = discord.Intents.all()
bot = Bot(intents=intents)


def get_upc_code(message: str):
    try:
        parts = message.split(" ")
        print(parts)
        for part in parts:
            if part.__contains__("https://barcode.live/?upc="):
                upc_code = part.split("=")[1]
                return upc_code
    except Exception as e:
        print(e)


@bot.hybrid_command(
    name="get_code",
    description="Get the UPC code from the message",
)
@app_commands.describe(arg="Message with the UPC code")
@app_commands.rename(arg="code")
async def response(interaction: discord.Interaction, arg: str):
    try:
        upc_code = get_upc_code(arg)
        if upc_code is None:
            await interaction.reply(content="No UPC code found in the message")

        else:
            await interaction.reply(content=upc_code + " is the code")
    except Exception as e:
        print(e)
        await interaction.reply(content="Something went wrong")
    try:
        upc_code = get_upc_code(arg)
        await interaction.reply(content=upc_code + " is the code")
    except Exception as e:
        print(e)
        await interaction.response.send_message("Something went wrong")


@bot.hybrid_command(
    name="test_selenium",
    description="testing selenium",
)
async def response(interaction: discord.Interaction):
    try:
        test = WSM.giveDolar()
        await interaction.reply(content=f"the price of the dolar is {test}")
    except Exception as e:
        print(e)
        await interaction.reply(content="Something went wrong")


@bot.hybrid_command(
    name="test_brickseek1",
    description="testing brickseek 1",
)
async def response(interaction: discord.Interaction):
    try:
        test2 = WSM.brickSeekTest1()        
        await interaction.reply(content=f"it should work", )
    except Exception as e:
        print(e)
        await interaction.reply(content="Something went wrong")


bot.run(TOKEN)
