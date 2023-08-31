import requests

def get_ctq_link():
    try:
        response = requests.get(F'https://api.telegram.org/bot{token}/getUpdates')
        print(response.text)
    except Exception as e:
        print(F'getUpdates Failed!\n{e}')
    #return 'https://www.mentalfloss.com/article/31932/chasing-cicada-exploring-darkest-corridors-internet'