
# formiks automod
# v19

import discord, time

def readfile (path):
	with open(path, 'r') as f:
		_return = f.read()
		f.close()
		return _return

token = readfile('./tkn')

client = discord.Client()

server_id = 800906094729101353
Me = 825470246650511390
chat = 992280083005980703
vc_rep = 953459064082432080
chill_chat = 950185828980752384
bot_cmd = 940663774220783716

staff = 860606861668384828	# staff role
vc_mods = 860542940820668447 # vc mods role


def log(ID, type):
	if type == 'mute/warn' or type == 'warn/mute':
		print(f"\n{ID} has been warned and muted.")
	if type == 'ban':
		print(f"\n{ID} has been banned")
	if type == 'vc-rep':
		printf(f"\n +VC Report")


slurs = (
	"nigger",
	"nigg3r",
	"n!gger",
	"n!gg3r",
	"ni66er",
	"niger",
	"n!ger",
	"negro",
	"n3gro",
	"negr0",
	"n3gr0",
	"fag",
	"f4g",
	"beaner",
	"bner",
	"beener",
	"negger",
	"neggir",
	"neggar",
	"niggar",
	"gger",
	"iger"
)


@client.event
async def on_ready():
	print("Ready.")

@client.event
async def on_message (message):
	if message.guild.id == server_id:
		msg = message.content.lower()
		author = message.author
		roles = message.guild.roles
		for role in roles:
			if role.id == staff or role.id == vc_mods:
				for member in role.members:
					if member.id == author.id:
						return

		aID = author.id
		ctx = message.channel

		if aID == Me:
			return
	
		print(f"\n\nAuthor: {author.name} \t\t ID: {aID}\nMessage: {message.content}")


		if ctx.id == chat or ctx.id == chill_chat or ctx.id == bot_cmd:

			if "speed" in msg and "dead" in msg and "not" not in msg:
				await ctx.send(f"?ban {aID} faking speed's death")
				log(aID, 'ban')

			if msg in slurs:
				await ctx.send(f"?ban {aID} slur")
				log(aID, 'ban')
				
			if ("speed" in msg or "darrel" in msg) and "aunt" in msg:
				await ctx.send(f"?ban {aID} talking about speed's aunt")
				log(aID, 'ban')
				
			if len(msg.split(" ")) > 65 or len(msg) > 225:
				await ctx.send(f"?mute {aID} 1h wall/spam")
				time.sleep(1)
				await ctx.send(f"?warn {aID} wall/spam")
				log(aID, 'mute/warn')
				
			if "kys" in msg or "kill yourself" in msg or "commit suicide" in msg or ("hope" in msg and "die" in msg and ("dont" not in msg or "don't" in msg)):
				await ctx.send(f"?ban {aID} promoting suicide/death")
				log(aID, 'ban')
				
			if ("follow" in msg or "subscribe" in msg) and (("me" in msg or "my" in msg) or ("@" in msg)):
				await ctx.send(f"?warn {aID} promo") 
				time.sleep(1)
				await ctx.send(f"?mute {aID} 1h promo")
				log(aID, 'mute/warn')

			if "rape" in msg.split(" ") or "rapist" in msg:
				await ctx.send(f"?ban {aID} rape/tos")
				log(aID,'ban')

			if ("like" in msg or "love" in msg or "fuck" in msg or "have sex with" in msg or "had sex with") and ("little kid" in msg or "little boy" in msg or "little girl" in msg or "child" in msg or "minors" in msg or "underage" in msg):
				await ctx.send(f"?ban {aID} pedo")
				log(aID,'ban')

		if ctx.id == vc_rep:
			if "ban" in msg or "jail" in msg or "mute" in msg or "kick" in msg or "warn" in msg:
				await ctx.send(msg)
				log(0, "vc-rep")

client.run(token)

