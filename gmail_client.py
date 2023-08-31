"""
Taken from
https://github.com/googleworkspace/python-samples/blob/main/gmail/quickstart/quickstart.py
"""

from __future__ import print_function

import os.path
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import mimetypes

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def gmail_send_message(creds, attachment):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id
    """

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message['To'] = 'bharadwaj.akella_Fe3XMh@kindle.com'
        message['From'] = 'nagarjunrv@gmail.com'
        message['Subject'] = 'CTQ Compounds daily reader'

        type_subtype, _ = mimetypes.guess_type(attachment)
        maintype, subtype = type_subtype.split('/')

        with open(attachment, 'rb') as fp:
            attachment_data = fp.read()
        message.add_attachment(attachment_data, maintype, subtype, filename=os.path.basename(attachment))

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def get_oauth_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def send_message_with_attachment(attachment):
    creds = get_oauth_creds()
    gmail_send_message(creds, attachment)

