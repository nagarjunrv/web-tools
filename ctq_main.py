from gmail_client import GClient
from telegram_client import TelegramClient
from web_client import get_contents_pdf
from email.message import EmailMessage
import mimetypes


gclient = GClient()
tclient = TelegramClient()


def get_ctq_link():
    pass


def send_article_to_kindle():
    message = EmailMessage()
    message['To'] = 'bharadwaj.akella_Fe3XMh@kindle.com'
    message['From'] = 'nagarjunrv@gmail.com'
    message['Subject'] = 'CTQ Compounds daily reader'

    attachment = get_contents_pdf(get_ctq_link())

    type_subtype, _ = mimetypes.guess_type(attachment)
    maintype, subtype = type_subtype.split('/')

    with open(attachment, 'rb') as fp:
        attachment_data = fp.read()
    message.add_attachment(attachment_data, maintype, subtype, filename=os.path.basename(attachment))
    gclient.gmail_send(message)


def main():
    #send_message_with_attachment(get_content(get_ctq_link()))
    get_ctq_link()


if __name__ == '__main__':
    main()