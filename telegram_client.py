from telethon import TelegramClient
import configparser
import json

class TeleClient:
    def __init__(self, config_file='configs/telegram_client_config.ini') -> None:
        config = configparser.ConfigParser()
        config.read(config_file)
        self.init_client(config)
        

    def init_client(self, config):
        creds = None
        with open(config['DEFAULT']['creds_file'], "r") as  file:
            creds = json.load(file)
        self.client = TelegramClient(config['DEFAULT']['session_path'], creds['app_id'], creds['api_hash'])
        #self.client.session.save_entities = False


    async def async_get_me(self):
        me = await self.client.get_me()
        print(me.stringify())


    def get_me(self):
        with self.client:
            self.client.loop.run_until_complete(self.async_get_me())