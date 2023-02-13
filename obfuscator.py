#<------------------------------------------------------------>#
from importlib.resources import path
import discord
from discord.ext import commands, tasks
import requests
import os
from os import system
import subprocess
import shutil
import keep_alive
from itertools import cycle
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
token = os.environ['Token-847294729741009580259999485992']
channel_id = 000000000000
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
bot = commands.Bot(command_prefix="$")
bot.remove_command("help")
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
status = cycle([
    f"{bot.command_prefix}obfuscate",
    f"{bot.command_prefix}obfuscate",
    f"{bot.command_prefix}obfuscate",
])
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
def obfuscation(path, author):
    copy = f".//obfuscated//{author}.lua"
    
    if os.path.exists(copy):
        os.remove(copy)
        
        shutil.copyfile(path, copy)

        text_file = open(f".//obfuscate.lua", "r")
        data = text_file.read()
        text_file.close()
        f = open(copy, "a")
        f.truncate(0)
        f.write(data)
        f.close()

        originalupload = open(path, "r")
        originalupload_data = originalupload.read()
        originalupload.close()

        with open(copy, "r") as in_file:
            buf = in_file.readlines()

        with open(copy, "w") as out_file:
            for line in buf:
                if line == "--SCRIPT\n":
                    line = line + originalupload_data + '\n'
                    out_file.write(line)
                    output = subprocess.getoutput(f'bin/luvit {copy}')

            f = open(f".//obfuscated//{author}-obfuscated.lua", "a")
            f.write(output)
            f.close()

            os.remove(path)
            os.remove(copy)
            print(f"\n✅ [{path}] Source Removed.\n")
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
@bot.event
async def on_ready():
    change_status.start()
    print(f"\n-- Connected Via Discord --\n> Name : {bot.user}\n> Prefix : {bot.command_prefix}\n> Command : {bot.command_prefix}help\n")
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(
        type=discord.ActivityType.playing,
        name=next(status)
    ))
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(
        type=discord.ActivityType.playing,
        name=next(status)
    ))
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
@bot.event
async def on_message(message):
    channel = str(message.channel)
    author = str(message.author)
    channel = bot.get_channel(channel_id)

    try:
        url = message.attachments[0].url
        if not message.author.bot:
            if message.channel.type is discord.ChannelType.private:
                if message.attachments[0].url:
                    if '.lua' not in url:
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"Only **'.lua', '.txt'** Allowed!",
                            color=0xFFFF00
                        )
                        dm = await message.author.create_dm()
                        await dm.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"Obfuscating, Please Wait!",
                            color=0xFFFF00
                        )
                        dm = await message.author.create_dm()
                        await dm.send(embed=embed)
                        
                        uploads_dir = f".//uploads//"
                        obfuscated_dir = f".//obfuscated//"

                        if not os.path.exists(uploads_dir):
                            os.makedirs(uploads_dir)
                            
                        if not os.path.exists(obfuscated_dir):
                            os.makedirs(obfuscated_dir)

                        response = requests.get(url)
                        path = f".//uploads//{author}.lua"

                        if os.path.exists(path):
                            os.remove(path)

                        open(path, "wb").write(response.content)
                        obfuscation(path, author)
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"File Obfuscated!",
                            color=0xFFFF00
                        )
                        dm = await message.author.create_dm()
                        await dm.send(embed=embed, file=discord.File(f".//obfuscated//{author}-obfuscated.lua"))
                        
            if message.channel.id == channel_id:
                if message.attachments[0].url:
                    if '.lua' not in url:
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"Only **'.lua'** Allowed!",
                            color=0xFFFF00
                        )
                        await channel.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"Obfuscating, Please Wait!",
                            color=0xFFFF00
                        )
                        await channel.send(embed=embed)

                        uploads_dir = f".//uploads//"
                        obfuscated_dir = f".//obfuscated//"

                        if not os.path.exists(uploads_dir):
                            os.makedirs(uploads_dir)
                            
                        if not os.path.exists(obfuscated_dir):
                            os.makedirs(obfuscated_dir)

                        response = requests.get(url)
                        path = f".//uploads//{author}.lua"

                        if os.path.exists(path):
                            os.remove(path)

                        open(path, "wb").write(response.content)
                        obfuscation(path, author)
                        embed = discord.Embed(
                            title=f"**Coin Hub**",
                            description=f"File Obfuscated!",
                            color=0xFFFF00
                        )
                        await channel.send(embed=embed,file=discord.File(f".//obfuscated//{author}-obfuscated.lua"))
    except:
        pass
#<------------------------------------------------------------>#

#<------------------------------------------------------------>#
keep_alive.keep_alive()
bot.run(token)
#<------------------------------------------------------------>#