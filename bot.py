import discord
from discord.ext import commands

# Replace these IDs with your own
SOURCE_SERVER_ID = 12824428534776  
SOURCE_CHANNEL_ID = 12834779  
TARGET_SERVER_ID_1 = 1188836809072  
TARGET_CHANNEL_ID_1 = 1327679161142  
TARGET_SERVER_ID_2 = 10008337716  
TARGET_CHANNEL_ID_2 = 132762073  
BOT_TOKEN = "BOT Token here" #enter ur bot token here
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Turned onn {bot.user}")
    print("Get set go")
    await bot.change_presence(status=discord.Status.invisible)
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if (
        message.guild
        and message.guild.id == SOURCE_SERVER_ID
        and message.channel.id == SOURCE_CHANNEL_ID
    ):      
        target_guild_1 = discord.utils.get(bot.guilds, id=TARGET_SERVER_ID_1)
        if target_guild_1:
            target_channel_1 = discord.utils.get(target_guild_1.channels, id=TARGET_CHANNEL_ID_1)
            if target_channel_1 and isinstance(target_channel_1, discord.TextChannel):               
                display_name = message.author.display_name              
                if message.content:
                    await target_channel_1.send(f"**{display_name}:** {message.content}")                     
                for attachment in message.attachments:
                    await target_channel_1.send(
                        content=f"**{display_name}** uploaded:",
                        file=await attachment.to_file()
                    )        
        target_guild_2 = discord.utils.get(bot.guilds, id=TARGET_SERVER_ID_2)
        if target_guild_2:
            target_channel_2 = discord.utils.get(target_guild_2.channels, id=TARGET_CHANNEL_ID_2)
            if target_channel_2 and isinstance(target_channel_2, discord.TextChannel):                
                display_name = message.author.display_name               
                if message.content:
                    await target_channel_2.send(f"**{display_name}:** {message.content}")                     
                for attachment in message.attachments:
                    await target_channel_2.send(
                        content=f"**{display_name}** uploaded:",
                        file=await attachment.to_file()
                    )

bot.run(BOT_TOKEN)
