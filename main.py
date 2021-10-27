import discord
import re
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

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	pattern_re = re.compile(r'grinding', re.IGNORECASE)
	pattern_re2 = re.compile(r'grind', re.IGNORECASE)
	if re.search(pattern_re, message.content):
		await message.add_reaction('👍🏿')
		await message.channel.send("The grind doesn't stop!")

	if re.search(pattern_re2,message.content):
		await message.add_reaction('👍🏿')
		await message.channel.send("The grind doesn't stop!")

client.run('ODk3OTY4OTAwNTQ3OTU2NzQ2.YWdYtQ.x9E748wKq8HpjU0w2AE5ABIqC6Y')