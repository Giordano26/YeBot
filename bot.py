from discord.ext import commands

#you can change the prefix for anything of your desire
bot = commands.Bot(command_prefix='-') 

#lava node setup
bot.lava_nodes = [
  {
    'host' : 'lava.link',
    'port' : 80,
    'rest_uri' : f'http://lava.link:80',
    'identifier' : 'MAIN',
    'region' : 'brazil',
    'password' : 'any'
  }
]

@bot.event
async def on_ready():
    print('Bot online') #online message
    bot.load_extension('dismusic') #music extension
    bot.load_extension('dch') #custom command extensions

bot.run("") #your bot token here