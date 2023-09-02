"""
Taken from
https://github.com/googleworkspace/python-samples/blob/main/gmail/quickstart/quickstart.py
"""

from __future__ import print_function

import os.path
import base64
import configparser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GClient:
    def __init__(self, config_file = 'configs/google_client_config.ini') -> None:
        config = configparser.ConfigParser()
        config.read(config_file)
        self.SCOPES = config['DEFAULT']['scopes']
        self.creds_file = config['DEFAULT']['creds_file']
        self.token_file = config['DEFAULT']['token_file']


    def gmail_send(self, message):
        try:
            creds = self.get_oauth_creds()
            service = build('gmail', 'v1', credentials=creds)
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


    def get_oauth_creds(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.creds_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        return creds
