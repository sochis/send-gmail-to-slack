from gmail.authorization import Credential
import base64


class GetMailContent():

    def get_mail_list(self):
        return self.service.users().messages().list(userId='me', q="is:unread").execute()

    def get_mail_content(self, id):
        return self.service.users().messages().get(userId='me', id=id).execute()

    def parse_mail(self, content):
        mail = {}

        if 'parts' in content['payload'].keys():
            raw_body = content['payload']['parts'][0]['body']['data']
        else:
            raw_body = content['payload']['body']['data']
        mail['body'] = base64.urlsafe_b64decode(raw_body).decode('utf-8')
        mail['snippet'] = content['snippet']

        headers = content['payload']['headers']
        for header in headers:
            if header['name'] == 'From':
                mail['from'] = header['value']
            elif header['name'] == 'To':
                mail['to'] = header['value']
            elif header['name'] == 'Subject':
                mail['subject'] = header['value']
            elif header['name'] == 'Date':
                mail['date'] = header['value']
        return mail

    def __init__(self):
        self.service = Credential().readonly_credential()