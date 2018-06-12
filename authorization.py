import json
import webbrowser
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow


class Credential():

    def readonly_credential(self):
        return Credential.pass_credential(self, 'readonly')

    def modify_credential(self):
        return Credential.pass_credential(self, 'modify')

    def send_credential(self):
        return Credential.pass_credential(self, 'send')

    def full_credential(self):
        return Credential.pass_credential(self, 'full')

    def pass_credential(self, scope_type):
        SCOPES = 'https://www.googleapis.com/auth/gmail.' + scope_type
        if (scope_type == 'full'):
            SCOPES = 'https://mail.google.com/'
        storage = Storage('credentials.json')
        credential = storage.get()
        if credential is None or credential.invalid:
            auth_info = json.load(open('client_secret.json'))
            info = auth_info['installed']
            flow = OAuth2WebServerFlow(client_id=info['client_id'],
                                       client_secret=info['client_secret'],
                                       scope=SCOPES,
                                       redirect_uri=info['redirect_uris'][0])
            auth_url = flow.step1_get_authorize_url()
            webbrowser.open(auth_url)
            code = input("input code : ")
            credential = flow.step2_exchange(code)
            storage = storage.put(credential)
        http = credential.authorize(Http())

        gmail_service = build('gmail', 'v1', http=http)
        return gmail_service

    if __name__ == '__main__' :
        pass_credential(1,"full")