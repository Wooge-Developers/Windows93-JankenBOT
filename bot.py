# JANKENPOOP
import nextcord
import config
from nextcord.ext import commands

client = commands.Bot(command_prefix = 'janken ')
game = nextcord.Game("Legacy Code Course")

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.idle, activity=game)
    print("JANKENPOPP IS HERE HAHAHAHAHAHAH")

@client.command()
async def ping(ctx):
    await ctx.send(f'hey im the best in the world annd is the best programmer and think you can see my latency well i am the fastest in the world but here you go but remember i am the best, pong!: `{round(client.latency * 1000)}ms rtt`')

@client.command()
async def windows96(ctx):
    await ctx.send("WHAT WHAT IS THIS TRASH YOU MAY BE BETTER AT: https://windows93.net")

client.run(config.TOKEN)