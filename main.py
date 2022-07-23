import discord
import os
import random
import sys

print(sys.version)
print(sys.version_info)

client = discord.Client()
devList = ["thisnoaskac#1732"]
devIDList = [666149048532860938]

# settings
prefix = "s!"
p = prefix

# temp variables

# log in message
@client.event
async def on_ready():
  print("devList: " + str(devList))
  print('We have logged in as {0.user}'.format(client))
  print("This bot is in " + str(len(client.guilds)) + " servers.")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="s!help"))
# random tips
randTips = ["***TIP:*** Need help using this bot? Trying typing `{}help`.".format(p), "***TIP:*** Ughhhh, I want to change something with this bot!! What do I do? Well-- `{}settings` :)".format(p)]
for i in range(18):
  randTips.append("")

# case variation creator function
def createCaseVariation(st):
  result = ""
  for c in st:
    upperOrLower = random.randint(0, 1);
    if upperOrLower == 0:
      result += c.lower()
    else:
      result += c.upper()
  return result

# bool to on/off function
def toOnOff(b):
  if b:
    return "__***ON***__"
  return "__***OFF***__"

def time_in_range(start, end, x):
  """Return true if x is in the range [start, end]"""
  if start <= end:
    return start <= x <= end
  return start <= x or x <= end

def representsInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def hintWords(st):
  result = ""
  for c in st:
    revealedOrHidden = random.randint(0, 1);
    if c == " ":
      result += " "
    elif revealedOrHidden == 0:
      result += "\_"
    else:
      result += c
  return result

# check if someone has certain permissions
def hasPerms(member, perms):
  for role in reversed(member.roles):
    if not perms.is_subset(role.permissions):
      return False
  return True

# when the bot joins a new server
@client.event
async def on_server_join(server):
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=" s!help"))

# when a message is sent
@client.event
async def on_message(message):
  TOKENS = message.content.split()
  tokens = message.content.lower().split()

  global p

  if message.author == client.user and not message.content.endswith('\u200B'):
    return

  if message.content.lower().startswith('s!troubleshoot') and message.author.id in devIDList:
    tbMsg = "prefix: " + p
    tbMsg += "hi dev! lol! lalala"
    await message.channel.send(tbMsg)
  
  # randTip
  randTip = '\n' + randTips[random.randrange(0, len(randTips))]
  if randTip != "":
    randTip = "\n" + randTip
  
  if "1000179251389141073" in str(message.mentions):
    if random.randrange(0, 5) == 0:
      await message.reply(createCaseVariation("stop phoogkœn pinging me bruh") + " (prefix is `{}`)".format(p))
  
  if message.reference != None:
    reference_message = await message.channel.fetch_message(int(str(message.reference)[29:47]))
    
    if "1000179251389141073" in str(reference_message):
      if random.randrange(0, 5) == 0:
        await message.reply(createCaseVariation("don't phoogkœn rep1y 2 me bruh"))
  
  # prefix commands
  if message.content.lower().startswith(p + "lala") or message.content.lower().startswith(p + "rp"):
    for i in range(4):
      lalaMsg = "stel" + "." * random.randint(3, 300) + "la" * random.randint(1, 100) + "!" * random.randint(1, 30)
      for i in range(random.randint(0, 3)):
        lalaMsg += "\nstel" + "." * random.randint(3, 300) + "la" * random.randint(1, 100) + "!" * random.randint(1, 30)
      await message.channel.send(lalaMsg)
    await message.channel.send("STELL" + "A" * random.randint(20, 100) + "!" * random.randint(2, 30))
  
  # info
  elif message.content.lower().startswith(p + 'info'):
    infoMessage = "LaLaLa was created by thisnoaskac#1732 because he's a simp mofo! :)"
    if (random.random() < 0.35):
      infoMessage += "lol lalala"
    await message.channel.send(infoMessage + randTip)
  
  elif message.content.lower().startswith(p + 'vote'):
    voteMsg = "Make sure to support our bot by voting for it!\nTop.gg: [link]\nDiscord Bot List: [link]\nDisBotList.xyz: [link]\nThanks! :)"
    embed = discord.Embed(title="__**VOTE.**__", url="https://tinyurl.com/youlovethisgamedontyou", description=voteMsg+randTip, color=discord.Color.orange())
    await message.channel.send(embed=embed)
  
  # help
  elif message.content.lower().startswith(p + 'help'):
    helpMsg = "see how many servers this bot is in: `{}servers` or `{}guilds`".format(p, p)
    helpMsg += "\nsettings: `{}settings`".format(p)
    helpMsg += "\nLaLa! `{}lala`".format(p)
    embed = discord.Embed(title="__**Help**__", url="https://tinyurl.com/youlovethisgamedontyou", description=helpMsg+randTip, color=discord.Color.orange())
    await message.channel.send(embed=embed)
  
  # settings
  elif message.content.lower().startswith(p + 'settings') or message.content.lower().startswith(p + 'turn'):
    await message.channel.send("feature to be added")
  
  elif message.content.lower().startswith(p + 'prefix'):
    if len(tokens) != 2:
      await message.channel.send("Sorry, please type `{}prefix [new prefix]` to change the bot prefix.\nCurrent prefix: `{}`".format(p, p))
    else:
      p = tokens[1]
      await message.channel.send("LaLaLa's prefix has now been changed to `{}`".format(p) + randTip)
  
  elif message.content.lower().startswith(p + 'tips'):
    tipsMessage = "Here is a list of the random tips that appear when LaLaLa is triggered:"
    for tip in randTips:
      if tip != "":
        tipsMessage += "\n" + tip
    await message.channel.send(tipsMessage)
  
  elif message.content.lower().startswith(p + 'servers') or message.content.lower().startswith(p + 'guilds'):
    if message.author.id in devIDList:
      guildListMessage = ""
      for guild in client.guilds:
        guildListMessage += '\n' + str(guild)
      embed = discord.Embed(title="__**LaLaLa Servers ({})**__".format(len(client.guilds)), url="https://tinyurl.com/youlovethisgamedontyou", description=guildListMessage, color=discord.Color.orange())
      await message.channel.send(embed=embed)
    else:
      await message.channel.send("This bot is in {} servers.".format(str(len(client.guilds))) + randTip)
  
  elif message.content.lower().startswith(p + 'dev'):
    devListMessage = ""
    for i in range(len(devList)):
      devListMessage += "\n**" + str(i + 1) + ".** " + devList[i]
    embed = discord.Embed(title="__**Developer List**__", url="https://tinyurl.com/youlovethisgamedontyou", description=devListMessage, color=discord.Color.orange())
    await message.channel.send(embed=embed)
  
client.run(os.getenv('TOKEN'))
