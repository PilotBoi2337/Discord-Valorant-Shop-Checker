import requests

import riot_auth
import asyncio
import sys
import discord
import random
import asyncio
import nest_asyncio
import csv
nest_asyncio.apply()


    

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('$check'):
            channel = message.channel
            file = open("test.csv", "r")
            data = list(csv.reader(file, delimiter=","))
            for x in range(len(data)):
                
                if data[x][0] == str(message.author.id):
                    CREDS = data[x][1], data[x][2]

                    auth = riot_auth.RiotAuth()
                    asyncio.run(auth.authorize(*CREDS))


                    authtoken = (auth.access_token)
                    entitled = (auth.entitlements_token)
                    userid = (auth.user_id)
                    asyncio.run(auth.reauthorize())
                    url = (f"https://pd.na.a.pvp.net/store/v2/storefront/{userid}")


                    payload = ""
                    headers = {
                        "X-Riot-Entitlements-JWT": (entitled),
                        "Authorization": (f"Bearer {authtoken}")
                    }


                    response = requests.request("GET", url, data=payload, headers=headers)





                    # print(response.text)
                    # weapons = response.text
                    item1 = 757
                    item2 = item1 + 2
                    item3 = item2 + 2
                    item4 = item3 + 2

                    priceitem1 = item1 + 23
                    priceitem2 = priceitem1 + 26
                    priceitem3 = priceitem2 + 26
                    priceitem4 = priceitem3 + 26
                    li = list(response.text.split('"'))
                    first = (li[item1])
                    second = (li[item2])
                    third = (li[item3])
                    fourth = (li[item4])







                    url = "https://valorant-api.com/v1/weapons/skins"

                    payload = ""
                    response = requests.request("GET", url, data=payload)

                    uuidsort = list(response.text.split('"'))
                   
                    for val in uuidsort:
                        if val == first:
                            loc2 = uuidsort.index(val)
                            embedVar = discord.Embed(title=(uuidsort[loc2+4]), description="", color=0xFFFFFF)
                            embedVar.add_field(name="Price", value=(li[priceitem1].replace(':', ' ').replace('}', ' ').replace(',', ' ')), inline=False)
                            embedVar.set_thumbnail(url=(uuidsort[loc2+10]))
                            await message.channel.send(embed=embedVar)
                        elif val == second:
                            loc2 = uuidsort.index(val)
                            embedVar = discord.Embed(title=(uuidsort[loc2+4]), description="", color=0xFFFFFF)
                            embedVar.add_field(name="Price", value=(li[priceitem2].replace(':', ' ').replace('}', ' ').replace(',', ' ')), inline=False)
                            embedVar.set_thumbnail(url=(uuidsort[loc2+10]))
                            await message.channel.send(embed=embedVar)
                        elif val == third:
                            loc2 = uuidsort.index(val)
                            embedVar = discord.Embed(title=(uuidsort[loc2+4]), description="", color=0xFFFFFF)
                            embedVar.add_field(name="Price", value=(li[priceitem3].replace(':', ' ').replace('}', ' ').replace(',', ' ')), inline=False)
                            embedVar.set_thumbnail(url=(uuidsort[loc2+10]))
                            await message.channel.send(embed=embedVar)
                        elif val == fourth:
                            loc2 = uuidsort.index(val)
                            embedVar = discord.Embed(title=(uuidsort[loc2+4]), description="", color=0xFFFFFF)
                            embedVar.add_field(name="Price", value=(li[priceitem4].replace(':', ' ').replace('}', ' ').replace(',', ' ')), inline=False)
                            embedVar.set_thumbnail(url=(uuidsort[loc2+10]))
                            await message.channel.send(embed=embedVar)
                else: 
                    continue
        
            
        
      
        if message.content.startswith('$setup'):
            await message.author.send('Please enter your username and password in username:password format')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            cred = await self.wait_for('message')

            if (":") in (cred.content):
                did = []
                await message.author.send('Working on it...')
                split = cred.content.split(":")
                print(split)
                data = [1,2,3]
                with open('test.csv', 'a', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow([message.author.id, split[0], split[1]])
                    
                    await message.author.send('Success! Use $check to check your shop!')
                    f.close
                
            else:
                await message.author.send("Please input your password with correct formatting")
           

intents = discord.Intents.default()

intents.messages = True
client = MyClient(intents=intents)
client.run('NzU3NzI2OTU1MDk2MjQ0MzQ1.GD9pmS.DDM_Q_qs44icWOd-62Q0YAS78yJNoFouO4srZU')





