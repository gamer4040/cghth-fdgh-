import discord
from bot_logic import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("bye")
    if message.content.startswith('$какие команды знает этот бот?'):
        await message.channel.send("привет! попробуй напиши эти комманды и посмотри что произойдёт :):$hello ; $bye ; gen_pass")
    elif message.content.startswith('$gen_pass'):
        await message.channel.send(gen_pass(10))

client.run("MTI4OTk4MzY4OTU1MTM4MDYxMA.G2QnH4.CPrwk21m7d2kAptWYghcWOD28Q9NEoLYI2pgDo")
