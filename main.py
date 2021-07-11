import os
import discord
import requests
import json
import random
from replit import db
from discord.ext import tasks,commands
import asyncio
import datetime

from keep_alive import keep_alive
#permet de maintenir un bot créé sur replit 1h après déconnection du site

import threading


import sqlite3

wallpapers = sqlite3.connect('wallpapersDatabase.db')










#connaitre le temps d'attentes avant de request de nouveau
import requests #création d'un évènement 


r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

#permissions par defaut
default_intents = discord.Intents.default()
#permissions pour les membres
default_intents.members = True

triviaDispo=["a"]

#bidoof ecrit de nombreuse facon
#un jour je changerai peut etre ca par ignorer la casse
lebest=["bidoof","Bidoof","BIDOOF","keunotor",
"Keunotor","KEUNOTOR"]

#importation des images de bidoof
bidoofImages=["./images/bidoof1.jpg","./images/bidoofArmy.png","./images/bidoofGif.gif","./images/perfectBidoof.jpg","./images/touchBidoof.jpg","./images/bidoofFriend.jpg","./images/bidoofSnap.jpg","./images/bidoofCard.jpg"]

memesVideos=["https://youtu.be/8nALD25M2yU","https://youtu.be/AINfHRXx1kQ","https://youtu.be/jhp-2qYurWc","https://youtu.be/H9aC5AGY9YU","https://youtu.be/ZtjFsQBuJWw","https://youtu.be/u3K8VlxVLKo","https://youtu.be/pC3AFTLdPz0","https://youtu.be/_W09Hc1EjL8","https://youtu.be/8ZMQcMMbfWU","https://youtu.be/qRofinpW8kU","https://youtu.be/LPOlk22eftg","https://youtu.be/kiDXFIJ7QwE","https://youtu.be/nc7A8magTng","https://youtu.be/NuCElla9mYg","https://youtu.be/ScMS0rlHbOs","https://youtu.be/6OUGNgTZATw","https://youtu.be/HkiPoCy1kjc","https://youtu.be/jAaxVuz0uKk","https://youtu.be/qBGqQo6Pops","https://youtu.be/_zoRoEh-kOA","https://youtu.be/qB09z3oCk4Q","https://youtu.be/LJHZ15s0Tus","https://youtu.be/M_59o1WZSl4","https://youtu.be/i_VI6J-d_dI","https://youtu.be/9Qy-y_rpUFk","https://youtu.be/x3jTaKHWPhE","https://youtu.be/R-C-9DBuAiE","https://youtu.be/esfSH6qmuH0","https://youtu.be/Us2FjKZjvFI","https://youtu.be/tZazFmpeLFA","https://youtu.be/WnzrOSEFUe0","https://youtu.be/x-VBnmsXiOw","https://youtu.be/165n7QEWHSU","https://youtu.be/Ux0YNqhaw0I","https://youtu.be/yBEvE6RGwus","https://youtu.be/euA5D47lFxk","https://youtu.be/rW3LAJrZoQ0","https://youtu.be/tNgcxI1q_BM","https://youtu.be/IOXwdFjuWu4","https://youtu.be/Rk1MYMPDx3s","https://youtu.be/PDogJ8JhuhU","https://youtu.be/cWcJepqle1Q","https://youtu.be/PzJWjXTil7A","https://youtu.be/mRSpaLObDL4","https://youtu.be/EixPRMs2jbY","https://youtu.be/33vUgGjx4a8","Un must see : https://youtu.be/2RlTqFtdlH8","https://youtu.be/67tpcPaglR0","https://youtu.be/EPkhZHu9PHw","https://youtu.be/RFt3p1GqnHQ","https://youtu.be/M8d5Wr9au9I","https://youtu.be/B2NNSvnbuzQ","https://youtu.be/QkzN_cA5WtU","https://youtu.be/FFT1wFZvHCQ","https://youtu.be/nxN_B0jUHog","un must see (pour weebos) : https://youtu.be/JlPkIur_5_4","https://youtu.be/plrlrGtoiik","https://youtu.be/CAXklKrZNis","https://youtu.be/IdyXKJ8NcNI","https://youtu.be/DcrrUuRoWT4","https://youtu.be/u0x0kRrMR7I","https://www.youtube.com/watch?v=lPGipwoJiOM","https://youtu.be/7BG4vPEhABs","https://www.youtube.com/watch?v=oTyxJPaQg3A","https://www.youtube.com/watch?v=3FITaW2i7Mg","https://www.youtube.com/watch?v=RvVMz7PsWqg","https://www.youtube.com/watch?v=SckcB099zrg","https://www.youtube.com/watch?v=w7Ujjx-OHMA","https://www.youtube.com/watch?v=Udk9pbeYMfs","https://www.youtube.com/watch?v=B_3pGTXHlTo","https://www.youtube.com/watch?v=qfxDEZX9K0o","https://www.youtube.com/watch?v=QESmhmR3DW8","https://www.youtube.com/watch?v=T25_s0vK3FA","https://www.youtube.com/watch?v=2jnCwbXaDhM","https://www.youtube.com/watch?v=bZ9-PFes3mM","https://www.youtube.com/watch?v=R1fABpX5Mtg",
"https://youtu.be/flgtJUthKkk","https://youtu.be/aBH_rYkEIJc","https://www.youtube.com/watch?v=s8Pd0we1XFE","https://youtu.be/Ep4ThJ8cQhs"]

animals=["https://youtu.be/2ft954vXPa4","https://youtu.be/-1n8qfGZgJg","https://youtu.be/yh59FEUOWxQ","https://youtu.be/gZYig7U3i0M","https://youtu.be/29L8ZHQiaxU","https://youtu.be/y1X-RqV_6ME","https://youtu.be/JXkWSgU-CL0","https://youtu.be/jLO1CPYv0hc","https://youtu.be/AfsnHVaScjg","https://www.youtube.com/watch?v=nZp8-puBI3c","https://youtu.be/T78nq62aQgM","https://youtu.be/HJUMWJgYvPs","https://youtu.be/X0DbbZiVMYo","https://youtu.be/Sdn8SNYyjxc","https://youtu.be/ChA4ocxr9sk","https://youtu.be/bh5FDUNAkDY","https://youtu.be/7xkj4XqaynU","https://youtu.be/3Q8TSrDFG6w","https://www.youtube.com/watch?v=Y-3ObKHY8YU","https://www.youtube.com/watch?v=LEtorWba_Fg","https://www.youtube.com/watch?v=dBR5KgEt5wc","https://www.youtube.com/watch?v=p58hAN84oPM","https://www.youtube.com/watch?v=7B4aLgKCPDI","https://www.youtube.com/watch?v=GFAqaoSIAhg","https://www.youtube.com/watch?v=oViBGnPy9MU","https://www.youtube.com/watch?v=uwmeH6Rnj2E","https://www.youtube.com/watch?v=DN0gAQQ7FAQ","https://www.youtube.com/watch?v=dRIueSuykFY","https://www.youtube.com/watch?v=p-zGIS-WWZQ","https://www.youtube.com/watch?v=3f_h0rxhD9I","https://www.youtube.com/watch?v=C8s4cbZOoOI","https://www.youtube.com/watch?v=a7qRuUAyqCg","https://www.youtube.com/watch?v=L2lvOQjiD0Y","https://www.youtube.com/watch?v=CH7tlyvnKLQ","https://www.youtube.com/watch?v=NQ5zFfaupkQ","https://www.youtube.com/watch?v=1Zn958rN-H4","https://www.youtube.com/watch?v=dsuMqClh38M","https://www.youtube.com/watch?v=FIxYCDbRGJc","https://www.youtube.com/watch?v=HBxn56l9WcU",
"https://youtu.be/RKryTwRIaRg",
"https://youtu.be/xzbRffi-qDw","https://youtu.be/0b4TU_R7J3c","https://youtu.be/hLYMD6R6PvU"]


client = discord.Client()

client = discord.Client(intents=default_intents)

#DATABASE DATABASE, JUST LIVE IN THE DATABASE
def update_trivia(unTrivia):
  if "trivia" in db.keys():
    trivia = db["trivia"]
    trivia.append(unTrivia)
    db["trivia"] = trivia
  else:
   db["trivia"] = [unTrivia]

def delete_trivia(index):
  trivia = db["trivia"]
  if len(trivia)>index:
    del trivia[index]
    db["trivia"] = trivia


#------------------------




mots=["chat","chapeau","turban","eau"]




@client.event
async def on_member_join(member): #lorsqu'un nouvel utilisateur rejoint un serveur où le bot est présent, ce dernier lui souhaite la bienvenue
  #identifiant du channel generel A CHANGER POUR UN NOUVEAU SERVER
  general_channel: discord.TextChannel = client.get_channel(568896288859619357)
  await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")






#debut des event"
@client.event
async def on_ready(): #lorsque le bot est connecté au serveur, son status d'activité dans l'applicatione est changé et un message est envoyé dans la console
  activity = discord.Game(name="être en développement")
  await client.change_presence(status=discord.Status.idle, activity=activity)
  #annonce le log
  print('Bot logged in as {0.user}'.format(client))


  
  """
  th = threading.Thread(target=sometask)
  th.start()
"""



#cette fonction gere les messages
@client.event
async def on_message(message): #lorqu'un message est envoyé dans un serveur où le bot est présent

  #si le message est envoyé par le bot lui même, il ne fait rien
  if message.author == client.user:
    return



  
  #la commande !bidoof envoit un message+image random
  if message.content.startswith('!bidoof'):
    await message.channel.send("Tu veux une une brioche ?",file=discord.File(random.choice(bidoofImages)))
  else:
    #s'execute si la commande !bidoof n'est pas dans le message et
    #que le message contient bidoof
    if any(word in message.content for word in lebest):
      await message.channel.send('BIDOOF !!!!!!')


    if (' oof ' in message.content.lower() or message.content.lower().startswith('oof')
    or message.content.lower().endswith('oof')):
        await message.channel.send(file=discord.File(
    "./images/oof.png"))

    if 'issou' in message.content.lower():
      await message.channel.send(file=discord.File(
  "./images/issou.jpg"))

    if 'hey' in message.content.lower():
        await message.channel.send("https://i.imgur.com/9QamQDE.gif?noredirect")

    if 'padoru' in message.content.lower():
        await message.channel.send("https://media.tenor.com/images/9e38efb026f755e38c69cd6f9ba514d8/tenor.gif")

    if any(word in message.content for word in ['AAAA']):
        await message.channel.send("https://cdn.discordapp.com/attachments/568896589523976192/848898399645859850/bdd6502c44019d28990fbe21009669d5.jpg")


    #gags de qualité
    if (message.content.lower().endswith('quoi')):
      await message.channel.send("-feur")

    if (message.content.lower().endswith('oui')):
      await message.channel.send("-stiti")

    if (message.content.lower().endswith('non')):
      await message.channel.send("-bril")

    if (message.content.lower().endswith('hein')):
      await message.channel.send("deux")

    if (message.content.lower().endswith('ouais')):
      await message.channel.send("-stern")

    if (message.content.lower().endswith('sarah')):
      await message.channel.send("-croche")

    if (message.content.lower().endswith('chaud') or 
    message.content.lower().endswith('cho') or
    message.content.lower().endswith('sho')):
      await message.channel.send("-ananas")

    if (message.content.lower().endswith('nan')):
      await message.channel.send(random.choice(["-tes","-terre","-cy"]))




  #commande !help pour lister les fonctions
  # c'est fait à la mano pour le moment
  if message.content.startswith('!help'):
    await message.channel.send("```COMMANDES :\n!bidoof\n!memeVideo\n   #un meme video\n!animal\n   #les animaux c'est rigolo\n!parrot [votre message]\n!del [nbre de messages à supprimer]\n\nTrivias :\n!trivia\n   #affiche un trivia aléatoire\n!newTrivia [votre trivia]\n   #ajouter un trivia à la liste\n\n!wallpaper\n#affiche un wallpaper aléatoire\n!wallpaper <origine>\n#affiche un wallpaper issu de l'origine fournie\n!origines\n#affiche la liste des origines disponibles```")

  #!parrot repete le message de l'utilisateur
  if message.content.startswith('!parrot '):
    await message.channel.send(message.content.split("!parrot ",1)[1])
    # le bot renvoit le message de l'utilisateur (à l'exception du "!parrot "")


  if message.content.lower().startswith('!parrotm'):
    await message.channel.send(message.content.split("!parrotM ",1)[1]),
    await message.delete()
    #idem que la commande parrot, cependant le message de l'utilisateur est ensuite supprimé

  #une commande changeante utilisee pour mes tests perso
  if message.content.startswith('!test'):
    await message.channel.send(file=discord.File(
  "./images/bidoofCard.jpg"
    ))

  #toute la gestion des trivias, je detaillerai peut etre un jour (les peut etre s'accumulent), cette gestion de base de données me vient d'un tuto que ej n'ai pas approfondis
  options=triviaDispo
  if "trivia" in db.keys():
    options.extend(db["trivia"])
  
  if message.content.startswith('!trivia'):
    await message.channel.send(random.choice(options))

  if message.content.startswith('!newTrivia'):
    unTrivia=message.content.split("!newTrivia ",1)[1]
    update_trivia(unTrivia)
    await message.channel.send("Merci pour cette anecdote ^^")

  if message.content.startswith('!deleteTrivia '):
    trivia=[]
    if "trivia" in db.keys():
      index = int(message.content.split("!deleteTrivia",1)[1])
      delete_trivia(index)
      trivia = db["trivia"]
    await message.channel.send(trivia)



  if message.content.startswith('!listeTrivia'):
    trivia = db["trivia"]
    await message.channel.send(trivia)


  if message.content.startswith('!del '):
    number=0
    number=int(message.content.split()[1])
    if (number>0):
      messages = await message.channel.history(limit=number+1).flatten()
      for each_message in messages:
        await each_message.delete()



  if message.content.lower().startswith('!memevideo'):
    await message.channel.send(random.choice(memesVideos))

  else:
     if message.content.startswith('!meme'):
       await message.channel.send("la commande n'existe pas encore...")
  
  if message.content.startswith('!animal'):
    await message.channel.send(random.choice(animals))

  if any(word in message.content.lower() for word in ["tg","gueule"]):
      await message.channel.send(file=discord.File(
  "./images/decide.mp4"))

  if 'taiga best waifu' in message.content.lower():
    emoji = '\N{THUMBS DOWN SIGN}'
    await message.add_reaction(emoji)

  if 'perfect bidoof' in message.content.lower():
    #<:emoji-name:emoji-id>
    emoji = '<:emoji_3:784838336783056936>'
    await message.add_reaction(emoji)

  if 'bowser' in message.content.lower():
    emoji = '<:fat_bowser:855560575110086656>'
    await message.add_reaction(emoji)

  if any(word in message.content.lower() for word in ["menteur","menteuse","tu mens","mentez"]):
    emoji = '<:usoda:855561433727500309>'
    await message.add_reaction(emoji)

  if 'masque' in message.content.lower():
    emoji = '<:masque:855562412543180810>'
    await message.add_reaction(emoji)

  if 'robot' in message.content.lower():
    emoji = '<:getin:855561908877918289>'
    await message.add_reaction(emoji)

  if 'malade' in message.content.lower():
    emoji = '<:kaguya:855562389444100107>'
    await message.add_reaction(emoji)

    


  
#cette commande fait appel à une base sql créée par moi, pour renvoyer des liens de wallpaper
  if message.content.lower().startswith('!wallpaper'):
      lesWallpapers=[]
      if message.content.lower()==('!wallpaper') or message.content.lower()==('!wallpaper '):
        commande=("SELECT lien from wallpapersTable") #la commande seule envoit un wallpaper aléatoire
        
      else:
        origineSpecifie = (message.content.split("!wallpaper ",1)[1]) #si le message contient un paramètre, le fond d'écran renvoyé à pour origine le paramètre
        commande=("SELECT lien from wallpapersTable where origine='"+origineSpecifie+"'")
        
      print(commande)
      lesLignes=wallpapers.execute(commande)
      for row in lesLignes:
        lesWallpapers.append(row[0])
      
      if len(lesWallpapers)==0:
        await message.channel.send("origine du wallpaper invalide")
      else:
        await message.channel.send(random.choice(lesWallpapers))

  if message.content.lower().startswith('!origines'): 
    lesOrigines="origines : "
    lesLignes=wallpapers.execute("SELECT DISTINCT origine from wallpapersTable")
    for row in lesLignes:
        lesOrigines=lesOrigines+(row[0])+", "
    lesOrigines=lesOrigines[0:len(lesOrigines)-2] #supprime la virgule à la fin
    await message.channel.send(lesOrigines)

    



    
    




keep_alive()
client.run(os.environ['token'])

