#Importando as bibliotecas
import os
from re import match
import discord
from discord import message
from discord.errors import ClientException
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.errors import CommandInvokeError
import requests
import json
import giphy_client
from giphy_client.rest import ApiException
import random
import youtube_dl
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import matplotlib.pyplot as plt

#Pegando o token do bot 
token_bot = 'ODg5OTY3MTk3MjczODYyMTg0.YUo8ig.-YuZyT0B6Z_HmssTgx0wwHKyz0U'

#Conectando com o client 
client = discord.Client()

#Criando o prefix para comandos 
bot = commands.Bot(command_prefix='!')

#---FUNÇÕES---
#Função para xingamento 
def xingamento(user=None):
    response = requests.get("http://xinga-me.appspot.com/api")
    text_json = json.loads(response.text)

    frase_json = text_json['xingamento']

    if user != None:
        frase = "{} é um {}".format(user, frase_json)

        return frase 
    else:
        
        return frase_json

#Função para gifs 
def gifs(text=None):
    api_key = 'L38sX2hSuzSD5HjfbY9xgWIdrArEPmSW'
    api_instance = giphy_client.DefaultApi()

    #Condicional 
    if text == None:
        api_response = api_instance.gifs_trending_get(api_key, limit=10, rating='g')
        lst = list(api_response.data)

        giff = random.choice(lst)

        url = giff.embed_url

        return url

    else:
        api_response = api_instance.gifs_search_get(api_key, q=text, rating='R', limit=10)
        lst = list(api_response.data)

        giff = random.choice(lst)

        url = giff.embed_url

        return url

#Função para pegar a auth do reddit 
def auth_reddit():
    global headers
    global TOKEN

    client_id = 'EJJaBc6O4c0EdTKtAPdsVQ'
    secret_id = 'Y92LFc_WhEfwjwmlsz2yF4NqPXxn5A'

    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_id)

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': 'Secret-Recognition-3',
            'password': 'reddit316712'}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'MyBot/0.0.1'}
    

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    return headers,TOKEN

def search(Text):
    headers, TOKEN = auth_reddit()

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    # while the token is valid (~2 hours) we just add headers=headers to our requests
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

    if Text == 'tits':
        subrreddits = ['https://oauth.reddit.com/r/TittyDrop/hot/',
                       'https://oauth.reddit.com/r/tits/hot/',
                       'https://oauth.reddit.com/r/boobs/hot/',
                       'https://oauth.reddit.com/r/Nipples/hot/']

        sub = random.choice(subrreddits)

        res = requests.get(sub,
                    headers=headers)

        url = []

        for post in res.json()['data']['children']:
            try:
                url.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            
        #Pegando somente gifs 
        url = [s for s in url if 'gifv' in s]

        print(url)

        #escolhendo o número aleatório 
        url_embed = random.choice(url)

        return url_embed 

    elif Text == 'lesbians':
        subrreddits = ['https://oauth.reddit.com/r/LesbiansGIF/hot/',
                'https://oauth.reddit.com/r/LesbiansGifsNSFW/hot/',
                'https://oauth.reddit.com/r/Lesbianskissing/hot/',
                'https://oauth.reddit.com/r/lesbians/hot/']

        sub = random.choice(subrreddits)

        print(sub)

        res = requests.get(sub,
                    headers=headers)

        url = []

        for post in res.json()['data']['children']:
            try:
                url.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            
        #Pegando somente gifs 
        url = [s for s in url if 'gifv' in s]

        print(url)

        #escolhendo o número aleatório 
        url_embed = random.choice(url)

        return url_embed 

    elif Text == 'overwatch':
        subrreddits = ['https://oauth.reddit.com/r/Overwatch_Porn/hot/']

        sub = random.choice(subrreddits)

        print(sub)

        res = requests.get(sub,
                    headers=headers)

        url = []

        for post in res.json()['data']['children']:
            try:
                url.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            
        #Pegando somente gifs 
        url = [s for s in url if 'gifv' in s]

        print(url)

        #escolhendo o número aleatório 
        url_embed = random.choice(url)

        return url_embed

    elif Text == 'ass':
        subrreddits = ['https://oauth.reddit.com/r/assgifs/hot/',
                       'https://oauth.reddit.com/r/ass/hot/',
                       'https://oauth.reddit.com/r/asstastic/hot/',
                       'https://oauth.reddit.com/r/RealGirls/hot/']

        sub = random.choice(subrreddits)

        print(sub)

        res = requests.get(sub,
                    headers=headers)

        url = []

        for post in res.json()['data']['children']:
            try:
                url.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            
        #Pegando somente gifs 
        url = [s for s in url if 'gifv' in s]

        print(url)

        #escolhendo o número aleatório 
        url_embed = random.choice(url)

        return url_embed
    
    else:
        res = requests.get("https://oauth.reddit.com/r/TittyDrop/hot/",
                        headers=headers)

        
        url = []

        
        for post in res.json()['data']['children']:
            try:
                url.append(post['data']['url_overridden_by_dest'])
            except:
                pass
            
        #Pegando somente gifs 
        url = [s for s in url if 'gifv' in s]

        #escolhendo o número aleatório 
        url_embed = random.choice(url)

        return url_embed


#Função para pegar a moeda 

def bolsa(symbol):

    # Pegando a url 
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}.SA&apikey=F7V1K3CSSAL8YCM2'.format(symbol)
    response = requests.get(url)
    data = response.json()

    date = data['Meta Data']['3. Last Refreshed']

    valor = data['Time Series (Daily)'][date]['4. close']

    frase_completa = "O preço de fechamento do dia de hoje ({}) é de R${}".format(date,valor)

    return  frase_completa  

#Função League of Legends - Individual
def lol_me(username):
    api_key = 'RGAPI-1ad63cb4-3db7-47dd-a6d6-4e2738eed02f'
    watcher = LolWatcher(api_key)
    my_region = 'br1'

    me = watcher.summoner.by_name(my_region, username)
    id = me['id']

    stats = watcher.league.by_summoner(my_region, id)
    print(stats)
    nivel = stats[0]['tier']
    rank = stats[0]['rank']

    frase_completa = 'O rank do jogador {} é {} {}'.format(username,nivel,rank)
    
    return frase_completa

#Função League of Legends - Match History 
def lol_match(username):
    api_key = 'RGAPI-0e1fade1-9895-4a2d-af55-83fc448b6d3d'
    watcher = LolWatcher(api_key)
    my_region = 'br1'

    me = watcher.summoner.by_name(my_region, username)
    id = me['accountId']  

    #Pegando todas as partidas
    my_maches = watcher.match.matchlist_by_account(my_region, id)

    #Pegando a última 
    last_match = my_maches['matches'][0]
    id_last_match = last_match['gameId']
    match_detail = watcher.match.by_id(my_region, id_last_match)

    dados = []
    sommoners = []

    print(id_last_match)

    
    for row in match_detail['participants']:
        dados_row = {}
        dados_row['champion'] = row['championId']
        dados_row['win'] = row['stats']['win']
        dados_row['kills'] = row['stats']['kills']
        dados_row['deaths'] = row['stats']['deaths']
        dados_row['assists'] = row['stats']['assists']
        dados_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        dados_row['goldEarned'] = row['stats']['goldEarned']
        dados_row['champLevel'] = row['stats']['champLevel']
        dados_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        dados.append(dados_row)   
       
    for row in match_detail['participantIdentities']:
        sommoners_name = {}
        sommoners_name['username'] = row['player']['summonerName']
        sommoners.append(sommoners_name['username'])

    latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    static_list = watcher.data_dragon.champions(latest, False, 'en_US')

    champ_list = {}
    for key in static_list['data']:
        row = static_list['data'][key]
        champ_list[row['key']] = row['id']
    for row in dados:
        row['championName'] = champ_list[str(row['champion'])]

    df = pd.DataFrame(dados)
    df['Username'] = sommoners
    df = df[['Username','championName','win','deaths','kills','assists','totalDamageDealt','goldEarned','totalMinionsKilled']]
    plt.savefig()
    return 
    



#--BOT FUNCINANDO -----
@bot.event
async def on_ready():
    print("O Bot está funcionando")

# -- Commandos messagens --- 
@bot.event
async def on_message(message):
    if message.content.startswith("!hello"):
        await message.channel.send("Fala parceiro!")

    if message.content.startswith("!xinga"):
        await message.channel.send(xingamento(message.mentions[0]))

    if message.content.startswith("!gif"):
        try:
            await message.channel.send(gifs(message.content.split(" ")[1]))
        except:
            await message.channel.send(gifs())

    if message.content.startswith("!porn"):
        await message.channel.send(search(message.content.split(" ")[1]))

    if message.content.startswith("!!!!delete"):
        await message.channel.purge(limit=100)

    if message.content.startswith("!daily"):
        await message.channel.send(bolsa(message.content.split(" ")[1]))

    if message.content.startswith("!lol_me"):
        await message.channel.send(lol_me(message.content.split(" ")[1]))

    await bot.process_commands(message)

# -- Comandos musicais -- 
@bot.command()
async def play(ctx, url:str):
    global voice 

    try:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
    except:
        pass

    if os.path.isfile("song.mp3"):
        os.remove('song.mp3')
        

    ydl_opts = {'format':'bestaudio/best',
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192'
                }]}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    for file in os.listdir("."):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def stop(ctx):
    channel = ctx.author.voice.channel
    voice.stop()

@bot.command()
async def lol_partida(ctx, username:str):
    embed = lol_match(username)
    await ctx.send(embed=embed)

#--END ---
bot.run(token_bot)