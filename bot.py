#<------------------------------------------------------------------------------------------------>
from importlib.resources import path
import discord
from discord.ext import commands, tasks
import requests
import os
from os import system
import subprocess
import shutil
import time
import keep_alive
import string
import random
from itertools import cycle
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
settings = {
    "title" : "Obfuscator Name",
    "desc" : "Made by CrxyScripter"
}
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
status = {
    "check" : "✅",
    "wrong" : "❎",
    "idle" : "🔄",
    "lock" : "🔒"
}
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
def generate_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
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

    if os.path.exists(f".//obfuscated//Python-{author}-Obfuscated.lua"):
        os.remove(f".//obfuscated//Python-{author}-Obfuscated.lua")

    f = open(f".//obfuscated//Python-{author}-Obfuscated.lua", "a")
    f.write(output)
    f.close()

    os.remove(path)
    os.remove(copy)
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
@bot.event
async def on_ready():
    keep_alive.keep_alive()
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
        name=f"{settings['desc']}"
    ))
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
@bot.command(name="delete-ob")
async def dob(message):
    author = str(message.author)
    os.remove(f".//obfuscated//{author}-obfuscated.lua")
    embed = discord.Embed(
        title = f"{settings['title']}", 
        description = "Successfully delete previous obfuscated code!", 
        color = 0x00FF00
    )
    dm = await message.author.create_dm()
    await dm.send(embed=embed) 
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
@bot.event
async def on_message(message):
    author = str(message.author)
    await bot.process_commands(message)
      
    try:
        url = message.attachments[0].url
        if not message.author.bot:
            if message.channel.type is discord.ChannelType.private:
                if message.attachments[0].url:
                    if '.lua' not in url:
                        embed = discord.Embed(
                          title = f"{settings['title']}", 
                          description = f"{status['wrong']} We detect that you're using a other file extension, Please rechange it into `.lua` and try again!", 
                          color = 0xFF0000
                        )
                        dm = await message.author.create_dm()
                        await dm.send(embed=embed) 
                    else:
                        embed = discord.Embed(
                            title = f"{settings['title']}",
                            description = f"{status['idle']} Receive Script File\n{status['idle']} Obfuscating Script File\n{status['idle']} Uploading Script File", 
                            color = 0xFFFF00
                        )
                        dm = await message.author.create_dm()
                        obfustext = await dm.send(embed=embed)
                        
                        time.sleep(1)
                        
                        embed = discord.Embed(
                            title = f"{settings['title']}",
                            description = f"{status['check']} Receive Script File\n{status['idle']} Obfuscating Script File\n{status['idle']} Uploading Script File", 
                            color = 0xFFFF00
                        )
                        await obfustext.edit(embed=embed)
                        
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
                            title = f"{settings['title']}",
                            description = f"{status['check']} Receive Script File\n{status['check']} Obfuscating Script File\n{status['idle']} Uploading Script File", 
                            color = 0xFFFF00
                        )
                        await obfustext.edit(embed=embed)
                        
                        time.sleep(1)
                        
                        embed = discord.Embed(
                            title = f"{settings['title']}",
                            description = f"{status['check']} Receive Script File\n{status['check']} Obfuscating Script File\n{status['check']} Uploading Script File", 
                            color = 0xFFFF00
                        )
                        await obfustext.edit(embed=embed)

                        time.sleep(1)
                        
                        embed = discord.Embed(
                            title = "Success!",
                            description = f"Enable Features :\n{status['lock']} Feature 1\n{status['lock']} Feature 2\n{status['lock']} Feature 3\n{status['lock']} Feature 4\n\n**Obfuscated code will be there in two seconds.**", 
                            color = 0x00FF00
                        )
                        await obfustext.edit(embed=embed)

                        time.sleep(2)
                        
                        dm = await message.author.create_dm()
                        await dm.send(file=discord.File(f".//obfuscated//Python-{author}-Obfuscated.lua"))
    except:
        pass
#<------------------------------------------------------------------------------------------------>

#<------------------------------------------------------------------------------------------------>
bot.run(os.environ['DISCORD_TOKEN'])
keep_alive.keep_alive()
#<------------------------------------------------------------------------------------------------>
