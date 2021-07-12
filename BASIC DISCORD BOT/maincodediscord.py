import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

nice_words= ["happy", "excited", "cheer", "joy", "happiness"]

motivation= ["KEEP FIGHTING!", "CHEER UP", "HURRAY!"]

poem = ["CINDERELLA", "SNOW WHITE", "PETER PAN", "BEAUTY AND THE BEAST", "PINOCCHIO"]



@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("hello") :
    await message.channel.send(f" {message.author.mention}HELLO there!")

  if msg.startswith("ping"):
    await message.channel.send("pong")

  if msg.startswith("ding"):
    await message.channel.send("dong")  

  if msg.startswith("First 10 numbers"): 
    await message.channel.send("1,2,3,4,5,6,7,8,9,10")

  if msg.startswith("story"):
    await message.channel.send(random.choice(motivation))

  

client.run(os.getenv("TOKEN"))

