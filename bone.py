import disnake as discord
from disnake.ext import commands
from sets import sets
import sqlite3
import sqlalchemy
#import DiscordUtils
import tabulate 
from tabulate import tabulate as tb
from datetime import datetime, time, date


inte = discord.Intents.all()



bot = commands.Bot(command_prefix = "Р", intents=inte)




conn = sqlite3.connect("database.db")
c = conn.cursor()

#create_engine('sqlite:///{}'.format(f), connect_args={'timeout': 15})

async def de(a, b, c1, c2, c3, ft, fi, ):
    q=discord.Embed(title=str(a), description=str(b),color=discord.Color.from_rgb(c1, c2, c3))
    q.set_footer(text=str(ft), icon_url=str(fi))
    await ctx.send(embed=q)
   

@bot.command(name="эмбед", help='Бот пишет ваш эмбед. эмбед <"заголовок"> <"текст"> <цвет-по-красному-число> <число-по-зелёному-число> <цвет-по-синему-число> <"текст-в-футере" > <иконка-в-футере>. Ковычки писать обязательно писать.') 
async def __hui(ctx, a: str, b: str, c1: int, c2: int, c3: int, ft: str, fi: str):
    
    q=discord.Embed(title=str(a), description=str(b),color=discord.Color.from_rgb(c1, c2, c3))
    q.set_footer(text=str(ft), icon_url=str(fi))
    await ctx.send(embed=q)
    
    
  #  de("Хуй", "Хуй конечно же", 40,55,55,"Ну хуй, пойми", ctx.author.avatar_url)
    
@bot.event
async def on_ready():
    

    

 
    
   
    
   
    for guild in bot.guilds:
        uss=f"S{guild.id}"
        c.execute(f"""CREATE TABLE IF NOT EXISTS {uss}(
        server TEXT,                     
        name TEXT, 
        idi TEXT, 
        money INT, 
        нефть INT, 
        газ INT, 
        олово INT, 
        медь INT, 
        лазурит INT, 
        свинец INT )""")
        c.execute(f"""CREATE TABLE IF NOT EXISTS {uss}_incomes(count INTEGER PRIMARY KEY AUTOINCREMENT, roleId TEXT, roleInc INT)""")
        c.execute(f"""CREATE TABLE IF NOT EXISTS {uss}_shop(s_count INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, cost INT NOT NULL)""")
        
        c.execute(f"""CREATE TABLE IF NOT EXISTS {uss}_resList(res TEXT NOT NULL)""")
        
        for member in guild.members:
             
            if c.execute("SELECT idi FROM {} WHERE idi = {}".format(uss, member.id)).fetchone() is None:
                datas=(str(guild.name), str(member), str(member.id), 0,0,0,0,0, 0,0)
                c.execute("INSERT INTO {}(server, name, idi, money, нефть, газ, олово, медь, лазурит, свинец) VALUES(?, ?,?,?,?,?,?,?,?,? )".format(uss), datas)
    conn.commit()               
                             
    print("Бот запущен") 
    





def whos():
    def predicate(ctx):
        return ctx.author.id==474727352795136020 or ctx.author.id == ctx.guild.owner_id or ctx.author.guild_permissions.administrator
    return commands.check(predicate)




    
    
@bot.command(name="доход-назн" , help="Назначает определенный доход к роли. назн-доход <пинг-роли> <доход>")
@whos()
async def scomes(ctx, role: discord.Role, income: int): 
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:
    
        uss=f"S{ctx.guild.id}"
         
             
        k=(str(role.id), int(income))
    
        c.execute("INSERT INTO {}_incomes(roleId, roleInc) VALUES(?,?)".format(uss), k)
        conn.commit()
        e=discord.Embed(title="**:pencil:¿~ Установлен доход ~¿:pencil:**", description=f"**Установлен доход в размере {income} / день для всех людей на должности <@&{role.id}>.**", color=discord.Color.from_rgb(250,161,204))
        #(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)

@scomes.error
async def scomes_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        embed=discord.Embed(title="***Ошибка!***", description=f"***{ctx.author.mention}, внимательнее пишите комманду! У вас ошибка! НЕ указана роль или доход***", color=discord.Color.from_rgb(240,20,60))
        embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
       
@bot.command(name="доход-убрать", help="₽убрать-доход <номер_строчки_в_лзп")
@whos()
async def __deleteIncome(ctx, count: int):
    uss=f"S{ctx.guild.id}"
     
     
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:
        c.execute("DELETE FROM {}_incomes WHERE count={}".format(uss, count))
        conn.commit()
        await ctx.send(f"Удалена {count} строка в таблице доходов вашего сервера.")
    else:
        await ctx.send("Вы не админ или не владелец бота" )      
      
   
@bot.command(name="выделить-деньги", help="Передаёт деньги с казны (счет бота Rawec'а) в счёт указанного пользователя." )
@whos()
async def __vidmoney(ctx, member: discord.Member, amount: int):
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:     
        uss=f"S{ctx.guild.id}"
         
         
        c.execute("UPDATE {} SET money=money+{} WHERE idi={}".format(uss,amount, member.id))   
        conn.commit()    
        c.execute("UPDATE {} SET money=money-{} WHERE idi={}".format(uss,amount, bot.user.id))  
        conn.commit()    




@bot.event
async def on_command_error(ctx, err):
    print(err)        
    
@bot.command(name="п")
async def __p(ctx):
	await ctx.send(str(discord.Member.id))
    
        
    
@bot.event
async def on_member_join(member):
	a=str(member.guild.name)
	 
	 
	
	
	#mi2=discord.ClientUser.id
	
	#mi=m.replace("<","")
	#mi1=mi.replace("@","")
	#mi2=mi1.replace(">","")
	
	print(uss, member.id) 
	c.execute("SELECT idi FROM {} WHERE idi = {}".format(uss, member.id))
	if c.fetchone() is None:
		datas=(str(member.guild.id), str(member.name), str(member.id) , 0,0,0,0,0)                
		c.execute("INSERT INTO users(server, name, idi, money, oil, cu, ol, gas) VALUES(?, ?,?,?,?,?,?,?)", datas)
		conn.commit()
	else:
		pass
           
        
        
                     
@bot.command(name="придумать-вещь")
@whos()
async def __pv(ctx, resname: str):
    uss=f"S{ctx.guild.id}"
     
     
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:        
        c.execute("ALTER TABLE {} ADD {} INT".format(uss, resname))
        conn.commit()
        c.execute("UPDATE {} SET {}=0 ".format(uss, resname))
        conn.commit()
        await ctx.send(f"Добавлен предмет «{resname}». Чтобы добавить его в магазин напишите магазин-доб")
    else:
        pass        


@bot.command(name="магаз-доб", help="n")
@whos()
async def __magazdob(ctx, i: str, q: int):
    uss=f"S{ctx.guild.id}"
     
      
    #print("олд")      
   # print("биба")
   
    c.execute("SELECT * FROM {} WHERE idi={}".format(uss, ctx.author.id)).fetchone()
    print(c.description)
    namesTuple=[tup[0] for tup in c.description]
    print(namesTuple)
    if i in namesTuple:  
        print("боба") 
        iQ=(str(i), int(q))
        c.execute("INSERT INTO {}_shop (item, cost) VALUES(?,?)".format(uss), iQ)
        conn.commit()
        await ctx.send(f"Был добавлен {i} за цену {q} в обычный магазин вашего сервера")
    else:                
        await ctx.send("Такого предмета нет")
            






@bot.command(name="табл")
async def __tab(ctx):
    uss=f"S{ctx.guild.id}"
     
       
    c.execute("SELECT * FROM {}".format(uss))
    await ctx.send(c.fetchall())  

            
@bot.command(name="бал", help="Баланс пользователя.") 
async def __bal(ctx, member: discord.Member=None):
    
    print("a")
    uss=f"S{ctx.guild.id}"
     
     
    if member is None:
        member=ctx.author
    c.execute("SELECT money FROM {} WHERE idi={}".format(uss, member.id))
    b=c.fetchone()[0]
   # await ctx.send(b)
    e = discord.Embed(title=f'**:credit_card: ¿~ Карта {member.name} ~¿ :credit_card:**',description=f"**:busts_in_silhouette:| Личные:**\n **{b}** ",color=0x42f566)
    #print(" e=") 
   # print("jjjj")
    await ctx.send(embed=e)
    
    

            
            
            
@bot.command(name="инв", help="Показывает инвентарь себя / указанного человека") 
async def __inv(ctx, member: discord.Member=None):
    uss=f"S{ctx.guild.id}"
     
     
    if member is None:
        member=ctx.author
    c.execute('SELECT * FROM {} WHERE idi={}'.format(uss, member.id))
    for row in c.fetchall():
        colName=[tup[0] for tup in c.description]
        colValue=[val for val in row]
        tank=list(zip(colValue, colName))
        a=tank[4:]
       # print(tank)
        heads=["Кол-во", "Ресурс"]
        e=discord.Embed(title=f"**Инвентарь {member.name}**", description=f"{tb(a, headers=heads, tablefmt='simple', numalign='center')}")
       # #(text=f"{member.name} × Rawec", icon_url=member.avatar_url)
        await ctx.send(embed=e)
        
@bot.command(name="магаз") 
async def __magaz(ctx, member: discord.Member=None):
    if member is None:
        member=ctx.author
    uss=f"S{ctx.guild.id}"
     
     
    c.execute("SELECT * FROM {}_shop".format(uss))
    colName=[tup[1] for tup in c.fetchall()]
    print(colName)
    c.execute("SELECT cost FROM {}_shop".format(uss))    
    colValue=[tup[0] for tup in c.fetchall()] 
    print(colValue)   
    tank=list(zip(colValue, colName))
    print(tank)
    heads=["Цена", "Предмет"]
    e=discord.Embed(title=f"**Магазин вашего сервера**", description=f"{tb(tank, headers=heads, tablefmt='simple', numalign='center')}")
    #(text=f"{member.name} × Rawec", icon_url=member.avatar_url)
    await ctx.send(embed=e)
    
    
    
    
       


          
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Следующее использования этой комманды будет доступно через 24ч")         
      
 
        
 
                                
@bot.command(name="зп", help="Выдает доход человеку за роль. НИ В КОЕМ СЛУЧАЕ НЕ УКАЗЫВАТЬ ПОЛЬЗОВАТЕЛЯ ПОСЛЕ КОММАНДЫ зп", cooldown_after_parsing=True)
@commands.cooldown(1, 86400, commands.BucketType.user )
async def __zp(ctx, member: discord.Member=None):
    

    uss=f"S{ctx.guild.id}"
     
     
    role=discord.Role
    if member is None:
        for role in ctx.author.roles:
            c.execute("SELECT roleId FROM {}_incomes WHERE roleId={}".format(uss, role.id, ))
            for row in c.fetchall():
                    if row is not None:
                        a=str(row[0])
                        for a in  c.execute("SELECT roleId FROM {}_incomes WHERE roleId={}".format(uss, role.id, )).fetchone():
                            c.execute("SELECT roleInc FROM {}_incomes WHERE roleId={}".format(uss, a ))
                            l=int(c.fetchone()[0]) 
                            c.execute("UPDATE {} SET money=money+{} WHERE idi={}".format(uss, l, ctx.author.id)) 
        e=discord.Embed(title="**:incoming_envelope:¿~ Доход получен! ~¿:incoming_envelope:**", description=f"**{ctx.author.mention}, вы получили  доход ПО ВСЕМ должностям, которые вы занимаете. В случае ошибок обращаться к администрации сервера.**", color=discord.Color.from_rgb(250,161,204))
        #(text=f"{ctx.author.name} × Rawec", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e) 
    else:
        e=discord.Embed(title="Доход НЕ получен!", description=f"***{ctx.author.mention}, НЕЛЬЗЯ указать человека в комманде!***", color=discord.Color.from_rgb(250,161,204))
    
        #(text=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e) 
    conn.commit()  

       
    
        
                                                 
                        
                                    
                
                
                
@bot.command(name="лзп")
async def __lz(ctx, member: discord.Member=None):
    if member is None:
        member=ctx.author
        uss=f"S{ctx.guild.id}"
         
         
        c.execute("SELECT roleId, roleInc FROM {}_incomes".format(uss))                       
        
        o=[f"<@&{tup[0]}>" for tup in c.fetchall()] 
        
        c.execute("SELECT  roleInc FROM {}_incomes".format(uss))  
        value=[tup[0] for tup in c.fetchall()]
      
        vh=list(zip(value, o))
        heads=["Зп/день", "Роль"]                                
        e=discord.Embed(title=f"**Доходы на вашем сервере**", description=f"{tb(vh, headers=heads, tablefmt='simple', numalign='right')}")
        #(text=f"{member.name} × Rawec", icon_url=member.avatar_url)
        await ctx.send(embed=e)   
        
                                                         
                    
@bot.command(name="платить", help="Передаёт ваши деньги указанному пользователю." )
async def __pay(ctx, member: discord.Member, amount: int):
    uss=f"S{ctx.guild.id}"
     
     
    c.execute("UPDATE {} SET money=money-{} WHERE idi={}".format(uss, amount, ctx.author.id))
    conn.commit()
    c.execute("UPDATE {} SET money=money+{} WHERE idi={}".format(uss, amount, member.id))   
    conn.commit()   
    await ctx.send(f"{member.name}у передано с вашего счета {amount} денег.")  
        
      
@bot.command(name="печать", help="Бот генерирует   деньги и прибавляет их к счету  указанного пользователя.")
@whos()
async def __pechat(ctx, member: discord.Member, Amount: int):
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:
        uss=f"S{ctx.guild.id}"
         
         
        c.execute("UPDATE {} SET money=money+{} WHERE idi={}".format(uss, Amount, member.id))
        conn.commit()  
        await ctx.send(f"{member.name}у добавлено {Amount} денег.")
        #@bot.command(aliases=["льгота", "льготы"])
#async def __daily():   




@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    if ctx.author.guild_permissions.administrator==True or ctx.author.id==474727352795136020:    
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.name} ')
   


@bot.command(name="эвал" )
async def __evaluate(ctx, *, cmd=None):
    if ctx.author.id==474727352795136020:
        try:
            exec(cmd)
           # a = exec(cmd)
           # await ctx.send(f'{a}')
        except:
            print(f'{cmd} is an invalid command')
            await ctx.send(f'Your bot friend could not execute an invalid command --> {cmd}')
    else:
        await ctx.send("Ты не владелец бота")         
 
    
@bot.command(name="лист-акций", help="Показывает список акций всех компаний и их стоимость.")
async def __listAkci(ctx):
    await ctx.send("Назначьте необходимые данные для этой комманды.")

@bot.command(name="магаз-убрать", help="₽убрать-доход <номер_строчки_в_лзп")
@whos()
async def __deleteMagaz(ctx, count: int):
    uss=f"S{ctx.guild.id}"
     
     

    c.execute("DELETE FROM {}_shop WHERE s_count={}".format(uss, count))
    conn.commit()
    await ctx.send(f"Удалена {count} строка в магазине вашего сервера.")
  

@bot.command(name="удалить-вещь", help="удалить-вещь <название> ( 1- удалить предмет только в магазине сераера. 2- удалить предмет только для контрактов. 3- удалить предмет на сервере вообще. По умолчанию стоит 3.")
@whos()
async def __uv(ctx, resname: str, koeff: int=None):
    uss=f"S{ctx.guild.id}"
     
     
    if koeff==3 or koeff is None:        
        c.execute("ALTER TABLE {} DROP COLUMN {}".format(uss, resname))
        conn.commit()
        c.execute("DELETE FROM {}_shop WHERE item={}".format(uss, resname))        
        conn.commit()
        await ctx.send(f"Предмет «{resname}» был удалён с __вашего сервера__.")
   # elif koeff==2:
    		#c.execute("DELETE FROM {}_shop WHERE item={}".format(uss,resname))
    elif koeff==1:
        c.execute("DELETE FROM {}_shop WHERE item={}".format(uss, resname))        
        
            
                      
        conn.commit()
        await ctx.send(f"Предмет «{resname}» был удалён с __магазина__ вашего сервера.")         




#asyc def __x()



bot.run(sets["token"])


