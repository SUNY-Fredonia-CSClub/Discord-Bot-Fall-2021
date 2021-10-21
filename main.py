import discord
client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.idle, activity=discord.Game('Ready to help!'))
	print ('Bot is ready! \n')
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.content.startswith("$hello"):
		await message.channel.send ("Hello I'm a bot")
		emoji = "👍🏿"
		await message.add_reaction(emoji)

client.run('')