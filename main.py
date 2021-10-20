import discord
client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.idle, activity=discord.Game('Ready to help!'))
	print ('Bot is ready! \n')
	print('We have logged in as {0.user}'.format(client))

client.run('')