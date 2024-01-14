import os
import discord
from ec2_metadata  import ec2_metadata as md
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

token = str(os.getenv('TOKEN'))


@client.event
async def on_ready():
    try:
        print("Logged in as a bot {0.user}".format(client))
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'{username}: {user_message} in channel: #{channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == 'hello world':
            await message.channel.send('hello')
            await message.channel.send(f'{username} ec2 data:{md.region}')
            return

        if user_message.lower() == ("tell me about your server"):

            await message.channel.send(f"""your ec2 server data:\n
                                       region:{md.region}\n
                                       public ipv4 address:{md.public_ipv4}\n
                                       availability zone:{md.availability_zone}\n
                                       server instance:{md.instance_type}
                                       """)
        else:
            await message.channel.send(f"I'm sorry, the command '{user_message}' is not a valid command")


client.run(token)