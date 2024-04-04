import os
import discord
from discord.ext import commands
from discord import app_commands
import logging



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = "ENTER YOUR TOKEN"


@bot.event
async def on_ready():
  custom_activity = discord.Game(f"ゲームバーのメッセージを記入")
  await bot.change_presence(status=discord.Status.online,activity=custom_activity)

  # スラッシュコマンドの同期
  await bot.tree.sync()

  print(f"login as {bot.user.mention}")



@app_commands.command(name="command_1", description="description")
async def command_1(self, interaction: discord.Interaction):
  await interaction.response.send_message("response message", ephemeral=True)


# ログいっぱいだとウザいのでWARNING以上にしてます。
bot.run(TOKEN, log_level = logging.WARNING)
