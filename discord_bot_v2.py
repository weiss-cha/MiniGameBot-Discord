#dependencies: discord.py, dotenv

import os
import discord
import random

TOKEN = 'TOKEN' #BOT TOKEN FROM DISCORD

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == 'hi':
        await message.channel.send('HELLO')

    elif message.content == '!play':
        win = 0
        lose = 0
        draw = 0
        choice = ['石头', '剪刀', '布']
        
        for i in range(5):
            await message.channel.send('''Please choose
    1 for 石头
    2 for 剪刀
    3 for 布
Enter a number of your choice:
            ''')

            msg = await client.wait_for("message")

            if msg.content == '1':
                await message.channel.send('You chose 石头')
            
            elif msg.content == '2':
                await message.channel.send('You chose 剪刀')
            
            elif msg.content == '3':
                await message.channel.send('You chose 布')
            
            computer_choice = random.choice(choice)
            await message.channel.send('Computer chose ' + computer_choice)

            if msg.content == '1' and computer_choice == '石头':
                await message.channel.send('Draw')
                draw = draw + 1

            elif msg.content == '1' and computer_choice == '剪刀':
                await message.channel.send('You win the game')
                win = win + 1

            elif msg.content == '1' and computer_choice == '布':
                await message.channel.send('You lose the game')
                lose = lose + 1

            elif msg.content == '2' and computer_choice == '石头':
                await message.channel.send('You lose the game')
                lose = lose + 1

            elif msg.content == '2' and computer_choice == '剪刀':
                await message.channel.send('Draw')
                draw = draw + 1
 
            elif msg.content == '2' and computer_choice == '布':
                await message.channel.send('You win the game')
                win = win + 1

            elif msg.content == '3' and computer_choice == '石头':
                await message.channel.send('You win the game')
                win = win + 1

            elif msg.content == '3' and computer_choice == '剪刀':
                await message.channel.send('You lose the game')
                lose = lose + 1

            elif msg.content == '3' and computer_choice == '布':
                await message.channel.send('Draw')
                draw = draw + 1

            if i == 4:
                await message.channel.send(f'''Final result:
    You win {win} time(s)
    Computer wins {lose} time(s)
    Draw game {draw} time(s)
End of the game
                ''')

            elif i != 4:
                await message.channel.send('Next round')

    elif message.content == '!gacha':
        card = random.randint(1,100)
        
        if card > 98:
            await message.channel.send('''You got an SSR !
    -------------------
*  |                            |  *
*  |                            |  *
*  |                            |  *
*  |           SSR          |  *
*  |                            |  *
*  |                            |  *
*  |                            |  *
    -------------------
            ''')

        elif 98 >= card > 85:
            await message.channel.send('''You got an SR !
    -------------------
*  |                            |  *
    |                            |  
*  |                            |  *
    |           SR            |  
*  |                            |  *
    |                            |  
*  |                            |  *
    -------------------
            ''')

        elif 85 >= card > 50:
            await message.channel.send('''You got an R !
    -------------------
    |                            |
    |                            |  
    |                            |
    |            R             |  
    |                            |
    |                            |  
    |                            |
    -------------------
            ''')

        else:
            await message.channel.send('''You got an N !
    -------------------
    |                            |
    |                            |  
    |                            |
    |            N             |  
    |                            |
    |                            |  
    |                            |
    -------------------
            ''')

    elif message.content == '!gacha10':
        SSR = 0
        SR = 0
        R = 0
        N = 0

        for i in range(10):
            card = random.randint(1,100)
            
            if card > 98:
                SSR = SSR + 1
                await message.channel.send('''You got an SSR !
    -------------------
*  |                            |  *
*  |                            |  *
*  |                            |  *
*  |           SSR          |  *
*  |                            |  *
*  |                            |  *
*  |                            |  *
    -------------------
                ''')

            elif 98 >= card > 85:
                SR = SR + 1
                await message.channel.send('''You got an SR !
    -------------------
*  |                            |  *
    |                            |  
*  |                            |  *
    |           SR            |  
*  |                            |  *
    |                            |  
*  |                            |  *
    -------------------
                ''')

            elif 85 >= card > 50:
                R = R + 1
                await message.channel.send('''You got an R !
    -------------------
    |                            |
    |                            |  
    |                            |
    |            R             |  
    |                            |
    |                            |  
    |                            |
    -------------------
                ''')

            else:
                N = N + 1
                await message.channel.send('''You got an N !
    -------------------
    |                            |
    |                            |  
    |                            |
    |            N             |  
    |                            |
    |                            |  
    |                            |
    -------------------
                ''')

            if i == 9:
               await message.channel.send(f'''Total:
    SSR:{SSR}
    SR:{SR}
    R:{R}
    N:{N}
                ''')
               
client.run(TOKEN)
