#!/usr/bin/env python3
import logging

import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

logging.basicConfig(filename='/opt/IgnisBot/ignis-bot.log', level=logging.INFO)

cred = credentials.Certificate('/opt/IgnisBot/firebase-sdk.json') #puxa as credenciais do arquivo 
firebase_admin.initialize_app(cred) #inicializa o firebase usando as credenciais fornecidas
db = firestore.client() #cria uma instancia da base de dados para ser acessada
battleJobs = ['pld', 'war', 'drk', 'gnb', 'whm', 'sch', 'ast', 'mnk', 'drg', 'nin', 'sam', 'brd', 'mch', 'dnc', 'blm', 'smn', 'rdm']
crafterJobs = ['gsm', 'ltw', 'wvr', 'arm', 'bsm', 'crp', 'cul', 'alc']

client = commands.Bot(command_prefix="ignisbot ", case_insensitive=True) #define a keyword que chama o bot


@client.event
async def on_ready(): #mostra mensagem que o app está online
    logging.info('%s online', client.user.name)


@client.command()
async def commands(ctx): #TODO precisamos colocar todos os comandos que o bot terá aqui
    await ctx.send('"ignisbot guide <JOB>" for job guides. Ex:For samurai guides send "ignisbot guide sam"\n'
    '"ignisbot leveling <JOB> <LEVEL>" for  leveling guides. Ex: For goldsmith 37 leveling send "ignisbot leveling gsm 37"\n'
    '"ignisbot card <NUMBER OF CARD>" for details on how to get a triple triad card. Ex: For info on the card 142 send "ignisbot card 142"\n'
    )




@client.command()
async def guide(ctx, job):
    dbRef = db.collection('guides')
    if (job in battleJobs):
        docs = dbRef.document(job).get().to_dict()['docs'] #pega os documentos da base de dados
        for doc in docs :
            await ctx.send(doc) #envia cada documento
    else:
        await ctx.send("Sorry, I condn't find that class. Be sure to type the 3 letter code for the class you want to search. Ex: 'ignisbot guide pld' to view the paladin guide")
    

@client.command()
async def leveling(ctx, job, level):
    levelWindow = 0
    intNumber = int(level)
    dbRef = db.collection('leveling')
    if(intNumber > 0 and intNumber < 15) :
        levelWindow = 14
    elif(intNumber >= 14 and intNumber <20) :
        levelWindow = 19
    elif(intNumber >= 20 and intNumber <25) :
        levelWindow = 24
    elif(intNumber >= 25 and intNumber <30) :
        levelWindow = 29
    elif(intNumber > 30 and intNumber <35) :
        levelWindow = 34
    elif(intNumber >= 35 and intNumber <40) :
        levelWindow = 39
    elif(intNumber >= 40 and intNumber <45) :
        levelWindow = 44
    elif(intNumber >= 45 and intNumber <50) :
        levelWindow = 49
    elif(intNumber >= 50 and intNumber <52) :
        levelWindow = 51
    elif(intNumber >= 52 and intNumber <54) :
        levelWindow = 53
    elif(intNumber >= 54 and intNumber <56) :
        levelWindow = 55
    elif(intNumber >= 56 and intNumber <58) :
        levelWindow = 57
    elif(intNumber >= 58 and intNumber <60) :
        levelWindow = 59
    elif(intNumber >= 60 and intNumber <62) :
        levelWindow = 61
    elif(intNumber >= 62 and intNumber <64) :
        levelWindow = 63
    elif(intNumber >= 64 and intNumber <66) :
        levelWindow = 65
    elif(intNumber >= 66 and intNumber <68) :
        levelWindow = 67
    elif(intNumber >= 68 and intNumber <70) :
        levelWindow = 69
    elif(intNumber >= 70 and intNumber <72) :
        levelWindow = 71
    elif(intNumber >= 72 and intNumber <74) :
        levelWindow = 73
    elif(intNumber >= 74 and intNumber <76) :
        levelWindow = 75
    elif(intNumber >= 76 and intNumber <78) :
        levelWindow = 77
    elif(intNumber >= 78 and intNumber <80) :
        levelWindow = 79
    else :
        await ctx.send("Your level must be between 1 and 80")
        return

    
    if (job in crafterJobs):
        if (dbRef.document(job).get().to_dict()[str(levelWindow)]): 
            docs = dbRef.document(job).get().to_dict()[str(levelWindow)] #pega os documentos da base de dados
            await ctx.send(docs) #envia cada documento
        else:
            await ctx.send("Sorry, but this class has not yet been added to our database. But don't worry, it soon will!")
    else:
        await ctx.send("Sorry, I condn't find that class. Be sure to type the 3 letter code for the class you want to search then the level your character is with said class. Ex: 'ignisbot leveling gsm 56' to view the best leveling way os a Goldsmith level 56")


@client.command()
async def card(ctx, number):
    if (number.isnumeric()):
        dbRef = db.collection('cards') 
        cardNumber = int(number)
        if (cardNumber < 1 or cardNumber > 326):
            await ctx.send("There are 326 cards, make sure the number you've entered is within that range.")
        else:
            if (dbRef.document(number).get().to_dict()):
                docs = dbRef.document(number).get().to_dict()
                sources = docs['source']
                await ctx.send(docs['name'])
                await ctx.send('https://arrtripletriad.com/images/cards/big/' + number + '.png')
                for source in sources :
                    await ctx.send(source) 
            else:
                await ctx.send("Sorry, but this card has not yet been added to our database. But don't worry, it soon will!")
    else:
        await ctx.send("Sorry, I couldn't understande that command. Be sure to write in the correct format. To view a cards detail just type 'ignisbot card <number of the card>'. Ex: ignisbot card 17")



@client.command()
async def carnivale(ctx, number):
    if (number.isnumeric()):
        dbRef = db.collection('carnivale') 
        levelNumber = int(number)
        if (levelNumber < 1 or levelNumber > 30):
            await ctx.send("There are 30 levels in the Masked Carnivale, make sure you enter a number within that range")
        else:
            docs = dbRef.document(number).get().to_dict()
            acts = docs['acts']
            await ctx.send(docs['name'])
            for act in acts :
                await ctx.send(act) 
    else:
        await ctx.send("Sorry, I couldn't understande that command. Be sure to write it in the correct format. To view a carnivale level detail just type 'ignisbot carnivale <number of the card>'. Ex: ignisbot carnivale 22")
client.run('ODkzODY0NDU2NjA4NzAyNTA0.YVhqJQ.ycQQIdtZ3rriVX__hGgErW0ErKE')
