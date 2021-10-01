import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="!!", case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user.name} online')


@client.command()
async def listacomandos(ctx):
    await ctx.send('Para visualizar salted do job desejado envie: "!!SIGLA DO JOB"\n EX:!!SAM para visualizar'
                   'salted do samurai')


@client.command()
async def pld(ctx):
    await ctx.send('https://docs.google.com/document/d/1JY2t2GvNaNnQhZ5Isp-HIso2JgGMY6WXk5IGAY2v8AU/edit')
    await ctx.send('https://saltedxiv.com/wp-content/uploads/2020/05/XLVyDMd.png')
    await ctx.send('BiS 2.43 https://etro.gg/gearset/c36ead01-8464-454c-87ac-5844c226cd54'
                   '\nBiS 2.42 https://etro.gg/gearset/f3986a7d-667e-46b5-aa4d-22a0900b42ba'
                   '\nBiS 2.41 https://etro.gg/gearset/9a05f867-9160-4c87-8856-5749f3080b5e'
                   '\nBiS 2.40 https://etro.gg/gearset/6e5ba8fa-8b27-48f6-9fe4-2452aa92ec8c')
    await ctx.send('Para mais informações sobre o PLD visite: https://saltedxiv.com/pld')


@client.command()
async def war(ctx):
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2021/02/WB2SEtL.png')
    await ctx.send('BiS 2.43 https://etro.gg/gearset/6b4a9646-3d72-4c85-ae3f-c77e28875389'
                   '\nBiS 2.38 https://etro.gg/gearset/717a06ac-8373-4490-9834-c5d1c321b0a7'
                   '\nBiS 2.37 https://etro.gg/gearset/f344710e-37b1-4c42-a422-76188ab680cf')
    await ctx.send('Para mais informações sobre o WAR visite: https://saltedxiv.com/war')


@client.command()
async def drk(ctx):
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2021/02/drkstandard1.png')
    await ctx.send('BiS 2.43 https://etro.gg/gearset/8f4ec40d-89be-4f9c-89e9-242502d63164'
                   '\nBiS 2.41 https://etro.gg/gearset/9889b11f-585d-45d0-af26-62819bb1841b'
                   '\nBiS 2.38 https://etro.gg/gearset/67fa1f50-ac71-443c-8711-a082bafe29d6')
    await ctx.send('Para mais informações sobre o DRK visite: https://saltedxiv.com/drk')


@client.command()
async def gnb(ctx):
    await ctx.send('opener: https://saltedxiv.com/wp-content/uploads/2021/02/r0bShYl.png')
    await ctx.send('https://www.youtube.com/watch?v=YPmcRG1csHY')
    await ctx.send('BiS 2.43 https://etro.gg/gearset/ec8a3fa3-4f6e-46df-9fe7-7127bfc0607d'
                   '\nBiS 2.42 https://etro.gg/gearset/dbf4ec08-1714-4417-b771-b586e2eaf89f'
                   '\nBiS 2.41 https://etro.gg/gearset/6d5d5df2-30f5-4d51-977e-e5879de04236'
                   '\nBiS 2.40 https://etro.gg/gearset/8f905aac-5c3c-4f2a-8130-da671c87ec6d')
    await ctx.send('Para mais informações sobre o GNB visite: https://saltedxiv.com/gnb')


@client.command()
async def whm(ctx):
    await ctx.send('Healing guide: '
                   'https://docs.google.com/document/d/1yoq1zU2VgMJQ53PaJHaUtwA3S2aSz1C69qkLDaOmZY8/edit')
    await ctx.send('BiS https://etro.gg/gearset/502c5c88-c1b4-4cd5-8a39-c0508f5900db')
    await ctx.send('Para mais informações sobre o WHM visite: https://saltedxiv.com/whm')


@client.command()
async def sch(ctx):
    await ctx.send('Healing guide: '
                   'https://docs.google.com/document/d/1yoq1zU2VgMJQ53PaJHaUtwA3S2aSz1C69qkLDaOmZY8/edit')
    await ctx.send('BiS https://etro.gg/gearset/4f21e0e3-d02e-4c58-a11d-a5cb062efcf8')
    await ctx.send('Para mais informações sobre o SCH visite: https://saltedxiv.com/sch')


@client.command()
async def ast(ctx):
    await ctx.send('Healing guide: '
                   'https://docs.google.com/document/d/1yoq1zU2VgMJQ53PaJHaUtwA3S2aSz1C69qkLDaOmZY8/edit')
    await ctx.send('BiS https://etro.gg/gearset/f76ddad7-1cf5-4b03-946b-cd63598157b0')
    await ctx.send('Para mais informações sobre o AST visite: https://saltedxiv.com/ast')


@client.command()
async def mnk(ctx):
    await ctx.send('https://docs.google.com/document/d/1TRcqNaiGYjUEHbYizHDg3-hEW0eUiU9AXyCY7p0lF5A/view')
    await ctx.send('https://www.youtube.com/watch?v=sz8laGlhSTg')
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2021/02/vaEhjJQ.png')
    await ctx.send('BiS https://etro.gg/gearset/388e7ee7-2919-49bf-b1d8-75fcfae73ce5')
    await ctx.send('Para mais informações sobre o MNK visite: https://saltedxiv.com/mnk')


@client.command()
async def drg(ctx):
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2020/06/DnKcFqr.png')
    await ctx.send('BiS 2.50GCD https://etro.gg/gearset/fc688f35-2df5-4e5d-9866-5ecee25cbce9'
                   '\n BiS 2.46GCD https://etro.gg/gearset/46473f8d-5174-4ca8-96bc-0ac24b054d19')
    await ctx.send('Para mais informações sobre o DRG visite: https://saltedxiv.com/drg')


@client.command()
async def nin(ctx):
    await ctx.send('https://www.youtube.com/watch?v=Im1HAm8-HgE')
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2020/06/NINreadibleRotation.png')
    await ctx.send('BiS https://etro.gg/gearset/dec9811d-c02c-4378-b046-d3cebe42eccb')
    await ctx.send('Para mais informações sobre o NIN visite: https://saltedxiv.com/nin')


@client.command()
async def sam(ctx):
    await ctx.send('https://docs.google.com/document/d/1rwJpp7iVnar2HeetfvOoZgiYlfAGAEyq7SRNBQ_F4S0/edit')
    await ctx.send('https://www.youtube.com/watch?v=7mCoCOIAWqo')
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2020/05/sam-cheat-sheet.jpg')
    await ctx.send('BiS 2.14GCD https://etro.gg/gearset/74252e32-cab1-4d8b-8068-c37926353ac9'
                   '\nBiS 2.07GCD https://etro.gg/gearset/0e5ae40a-6641-4118-9500-15199b423228'
                   '\nBiS 2.00GCD https://etro.gg/gearset/53b1f776-8d5f-4969-9cbf-6153f5228c9d')
    await ctx.send('Para mais informações sobre o SAM visite: https://saltedxiv.com/sam')


@client.command()
async def brd(ctx):
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2020/06/brd_quickstart.jpg')
    await ctx.send('BiS https://etro.gg/gearset/8418d22e-d70e-4b1a-87e0-d2b79dc3bd91')
    await ctx.send('Para mais informações sobre o BRD visite: https://saltedxiv.com/brd')


@client.command()
async def mch(ctx):
    await ctx.send('https://docs.google.com/document/d/1TEXy7k22cyffrkgiBCSi63s8NOqNqFZvdAYrfw2denc/edit')
    await ctx.send('Opener high ping: https://imgshare.io/images/2020/05/26/ShB_MCH_general_HighPing_5WF.png')
    await ctx.send('BiS https://etro.gg/gearset/44e9f4d8-7a77-4524-bd05-21c2e17295bc')
    await ctx.send('Para mais informações sobre o MCH visite: https://saltedxiv.com/mch')


@client.command()
async def dnc(ctx):
    await ctx.send('https://docs.google.com/document/d/1iktjQ-kW7Vp-iWy_xEWh6t62FaXqjfGELGmcWOtPQfM/edit')
    await ctx.send('Opener: https://saltedxiv.com/wp-content/uploads/2020/06/Ff7LvIQ.png')
    await ctx.send('BiS https://etro.gg/gearset/e4cd5da5-6365-4e30-bd26-8e5fadf8a17f')
    await ctx.send('Para mais informações sobre o DNC visite: https://saltedxiv.com/dnc')


@client.command()
async def blm(ctx):
    await ctx.send('https://www.youtube.com/watch?v=_g5jnFTe6dE')
    await ctx.send('Opener: https://www.akhmorning.com/assets/webp/guide/5.x/openers/blm/jp-opener.webp')
    await ctx.send('BiS https://etro.gg/gearset/1c64d9a9-892b-48a8-b7d1-f760839d659c')
    await ctx.send('Para mais informações sobre o BLM visite: https://www.akhmorning.com/jobs/blm/')


@client.command()
async def smn(ctx):
    await ctx.send('https://www.youtube.com/watch?v=qHfgStj5RmE')
    await ctx.send('Opener: https://www.akhmorning.com/assets/webp/guide/5.x/openers/smn/3rd-gcd-dwt-opener.webp')
    await ctx.send('BiS 2.50GCD https://etro.gg/gearset/5cfccfce-456b-45e8-9b5f-a71b7d7544a3'
                   '\n BiS 2.48GCD https://etro.gg/gearset/545b4941-747b-4588-9fe6-37e76778ff8d'
                   '\n BiS 2.47GCD https://etro.gg/gearset/2777f081-1ac6-43f7-a18f-3e1cc58cbc9b')
    await ctx.send('Para mais informações sobre o SMN visite: https://www.akhmorning.com/jobs/smn/')


@client.command()
async def rdm(ctx):
    await ctx.send('https://docs.google.com/document/d/1JqEFEsWcvZr2gYwAmtW4344qZJ8dMTlxyTiWwMSL2NM/edit')
    await ctx.send('https://www.youtube.com/watch?v=zBN4S7O2L8E')
    await ctx.send('Opener: https://www.akhmorning.com/assets/webp/guide/5.x/openers/rdm/3-8-opener.webp')
    await ctx.send('BiS 2.50GCD https://etro.gg/gearset/ee3466d0-bceb-4da0-823b-9914e37f1604'
                   '\n BiS 2.49GCD https://etro.gg/gearset/ee3466d0-bceb-4da0-823b-9914e37f1604'
                   '\n BiS 2.48GCD https://etro.gg/gearset/72f82fb5-9e09-4cf7-a2c8-ff0c6a16109f')
    await ctx.send('Para mais informações sobre o RDM visite: https://www.akhmorning.com/jobs/rdm/')

client.run('token')
