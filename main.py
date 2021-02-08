import discord
import requests
import simplejson as json
import emoji
from decouple import config

client = discord.Client()

def soccerData():
    AUTH = config('AUTH')
    response = requests.get('https://api.api-futebol.com.br/v1/campeonatos/10/tabela',
    params={'q':'request+language:python'},
    headers={'Authorization': 'Bearer {}'.format(AUTH)}
    )
    json_data = json.loads(response.text)
    return json_data

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$fut'):
        data = soccerData()
        await message.channel.send(emoji.emojize('----------------------Tabela do Brasileirão🇧🇷-------------------'))
        for x in range(20):
            await message.channel.send('{}º - {} | {} Pontos | {} Jogos | {} Saldo de Gols'.format(data[x]['posicao'], data[x]['time']['nome_popular'], data[x]['pontos'], data[x]['jogos'], data[x]['saldo_gols']))
            await message.channel.send('--------------------------------------------------------------------')

client.run(config('TOKEN'))