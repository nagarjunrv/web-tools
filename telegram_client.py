import requests
import configparser

class TelegramClient:
    def __init__(self, config_file='configs/telegram_client_config.ini') -> None:
        config = configparser.ConfigParser().read(config_file)
        self.url_prefix = F"https://api.telegram.org/bot{config['DEFAULT']['token']}/getUpdates"

    def getUpdates(self):
        try:
            response = requests.get(F'{self.url_prefix}/getUpdates')
            print(response.text)
        except Exception as e:
            print(F'getUpdates Failed!\n{e}')
            return None
        return ''