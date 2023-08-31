from gmail_client import send_message_with_attachment
from telegram_client import get_ctq_link
from web_client import get_content

def main():
    #send_message_with_attachment(get_content(get_ctq_link()))
    get_ctq_link()


if __name__ == '__main__':
    main()