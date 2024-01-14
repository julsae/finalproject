#importing class libraries
import os
import discord
from ec2_metadata  import ec2_metadata as md
from dotenv import load_dotenv

#loads the environment variable
load_dotenv()
#create a discord client
client = discord.Client()

#gets the token from the environment variable
token = str(os.getenv('TOKEN'))

#event handler for when the bot is online
@client.event
async def on_ready():
    try:
        print("Logged in as a bot {0.user}".format(client))
    except Exception as e:
        print(e)

#event handler for when a message is received
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

#extract username and channel from message 
    print(f'{username}: {user_message} in channel: #{channel}')

    if message.author == client.user:
        return

#bot to respond in the channel named random
    if channel == "random":
        if user_message.lower() == 'hello world':
            #responds with hello when sent hello world
            await message.channel.send(f'hello {username}')
            return
        if user_message.lower() == ("tell me about my server"):

#displays ec2 server information
            await message.channel.send(f"""your ec2 server data:\n
                region:{md.region}\n
                public ipv4 address:{md.public_ipv4}\n
                availability zone:{md.availability_zone}\n
                server instance:{md.instance_type}
                """)
        else:
            #lets the user know that command doesn't work
            await message.channel.send(f"I'm sorry, the command '{user_message}' is not a valid command")

#runs the bot
client.run(token)