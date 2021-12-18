#Code in replit.com (https://replit.com/@RickMellor/Schrodinger-Bot#main.py)

import discord
from discord.ext import commands
import os
import asyncpraw
import random
from keep_alive import keep_alive
from bs4 import BeautifulSoup
import requests
from replit import db

my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix = "sci ", case_intensive = True)

reddit = asyncpraw.Reddit(client_id="COMVnkC1zKRwMefuoVrE5w", client_secret="ZTu8Tkibe9lXERu7apYt_RnluIl2FQ", username="SchrodingerBot", password="python123", user_agent="pythonpraw")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

bot.remove_command("help")
@bot.command(pass_context = True)
async def help(ctx):
  embed = discord.Embed(
    title = "Yeah man no problem",
    colour = 0x9b59b6)
    
  embed.add_field(
    name="sci hola",
    value="Salúdame!",
    inline = True)
  
  embed.add_field(
    name="sci m",
    value="Memes científicos de r/sciencememes",
    inline = True)
  
  embed.add_field(
    name="sci m math",
    value = "Memes matemáticos de r/mathmemes",
    inline = True)
  
  embed.add_field(
    name="sci m phy",
    value = "Memes relativistas de r/physicsmemes",
    inline = True)
  
  embed.add_field(
    name="sci m che",
    value = "Memes químicos de r/chemistrymemes",
    inline = True)
  
  embed.add_field(
    name="sci m bio",
    value = "Memes orgánicos de r/biologymemes",
    inline = True)
  
  embed.add_field(
    name="sci m code",
    value = "Memes de programación de r/ProgrammerHumor",
    inline = True)
  
  embed.add_field(
    name="sci m eng",
    value = "Memes ingenieriles de r/engineeringmemes",
    inline = True)
  
  embed.add_field(
    name="sci m his",
    value = "Memes históricos de r/HistoryMemes",
    inline = True)
  
  embed.add_field(
    name="sci cita",
    value="Citas filosóficas de científicos y matemáticos reconocidos",
    inline = True)
  
  
  
  await ctx.send(embed = embed)


posts_repes = ['q6eawf', 'q6bzh7', 'q6oray', 'q6qi2a', 'q6fsnm', 'q6ht9l', 'q6kht9', 'q6izqu', 'q6crhz', 'q6v6g8', 'q6q32e', 'q6l594', 'q6tdnh', 'q6hj1u', 'q6ert1', 'q5y2cc', 'q61c77', 'q6fgqy', 'q6rnil', 'q6ka1d', 'q6tsr7', 'q6sx05', 'q6t9jw', 'q6pdsb', 'q5yl6o', 'q6npbz', 'q6365q', 'q6lqgr', 'q6r47c', 'q6nepf', 'q6u068', 'q6k6ya', 'q6jcaz', 'q6if8h', 'q6lems', 'q6stql', 'q6kyer', 'q5shmk', 'q6ston', 'q6jj84', 'q6tao4', 'q6peyx', 'q6pqn4', 'q6vglz', 'q6fe8i', 'q67bw8', 'q35op2', 'q726ao', 'q6v4se', 'q76qpp', 'q77spp', 'q6v0uc', 'q6xv8k', 'q79dti', 'q684mp', 'q6hexo', 'q75xlu', 'q6w9c8', 'q79qqb', 'q6w0d1', 'q6zat4', 'q6ok81', 'q75aqu', 'q76kqz', 'q6xamf', 'q6jzll', 'q6qh6v', 'pzociy']
@bot.command(pass_context = True)
async def m(ctx, item = None):
  
  if item == "code":
    subreddit_order = "ProgrammerHumor"

  elif item == "bio":
    subreddit_order = "biologymemes"

  elif item == "phy":
    subreddit_order = "physicsmemes"

  elif item == "che":
    subreddit_order = "chemistrymemes"
  
  elif item == "eng":
    subreddit_order = "engineeringmemes"

  elif item == "his":
    subreddit_order = "HistoryMemes"

  elif item == "math":
    subreddit_order = "mathmemes"
  
  elif item == None:
    subreddit_order = "sciencememes"

  result = random.randrange(0,21)
  if result != 20:
    subreddit = await reddit.subreddit(subreddit_order)
    list_submissions = []

    async for submission in subreddit.hot(limit=100):
      list_submissions.append(submission)

    #Enviar el embed. No puede ser para adultos
    random_submission = random.choice(list_submissions)
    while str(random_submission) in posts_repes:
      random_submission = random.choice(list_submissions)
    if random_submission.over_18 == False:
      url = random_submission.url
    
      if "youtu.be" in url == False or "jpg" in url or "png" in url or "jpeg" in url:
        title = random_submission.title
        user = random_submission.author
        embed = discord.Embed(title = "r/"+subreddit_order, url = random_submission.url, description = title, color = 0x3498db)
        embed.set_image(url = url)
        embed.set_author(name = str(user))
        await ctx.send(embed = embed)
      
      else:
        await ctx.send(url)
    
    else:
      while random_submission.over_18 == True:
        random_submission = random.choice(list_submissions)

      url = random_submission.url
    
      if "youtu.be" in url == False or "jpg" in url or "png" in url or "jpeg" in url:
        title = random_submission.title
        user = random_submission.author
        embed = discord.Embed(title = "r/"+subreddit_order, url = random_submission.url, description = title, color = 0x3498db)
        embed.set_image(url = url)
        embed.set_author(name = str(user))
        await ctx.send(embed = embed)
      
      else:
        await ctx.send(url)

    posts_repes.append(str(random_submission))
    print(posts_repes)

          
    #Otras opciones
  elif result == 20:
    random_answer = random.randrange(1,4)
    if random_answer == 1:
      await ctx.send("Bah")
    elif random_answer == 2:
      await ctx.send("Nope")
    elif random_answer == 3:
      await ctx.send("Not now...")
    
  elif random.randrange(0,1000 == 420):
    ctx.send("I love you")
  
  
#Quotes

@bot.command(pass_context = True)
async def cita(ctx):
  html_text = requests.get("https://dayinlab.com/citas")
  soup = BeautifulSoup(html_text.content, "html.parser")
  blockquote = soup.find("div", class_="entry-content")
  text = blockquote.find_all("p")
  list = []
  for quotes in text:
    list.append(quotes.text)
  quote = str(random.choice(list))
  await ctx.send(quote)
  

  #saludos

@bot.command(pass_context = True)
async def hola(ctx):
  rick = 800115110286589982
  daniel = 503913621668102149
  joan = 337595148768641024
  biel = 419131594796695552
  mar = 612286906201407570
  marzia = 752686663054000148
  lucas = 843564357916819467
  pula = 752686663054000148
  tolo = 604017034547953704
  nic = 515968743617331212
  miquel = 734130369246396478
  if str(ctx.message.author.id == rick):
    await ctx.send("Hola creador")
  elif str(ctx.message.author.id == daniel):
    await ctx.send("Mis humildes saludos, Kami-Sama")
  elif str(ctx.message.author.id == joan):
    await ctx.send("hola... senpai")
  elif str(ctx.message.author.id == biel):
    await ctx.send("01001000 01101111 01101100 01100001 00100000 01110000 01110010 01101111 01100111 01110010 01100001 01101101 01100001 01100100 01101111 01110010 00100000 01101010 01110101 01100100 01101111 01101011 01100001")
  elif str(ctx.message.author.id == mar):
    await ctx.send("Hola @rainbow_craftuli, me retratas? Pago en memes")
  elif str(ctx.message.author.id == lucas):
    await ctx.send("Y tú quién eres?")
  elif str(ctx.message.author.id == pula):
    await ctx.send("heyo bitch")
  elif str(ctx.message.author.id == tolo):
    await ctx.send("hola guapo")
  elif str(ctx.message.author.id == nic):
    await ctx.send("shut up")
  elif str(ctx.message.author.id == miquel):
    await ctx.send("what's up")
  else:
    await ctx.send("Hola humano")


keep_alive()
bot.run(my_secret)
