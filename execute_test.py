from gmail.getmail import GetMailContent
from slack.send_slack import SendSlack


class Execute():
    def send_gmail_to_slack(self):
        get_mail = GetMailContent()
        mails = get_mail.get_mail_list()['messages']
        for mail in mails:
            content = get_mail.get_mail_content(mail['id'])
            parse = get_mail.parse_mail(content)
            text = 'From : ' + parse['from'] + '\n' + 'date : ' + parse['date'] + '\n \n' + parse['body']
            SendSlack().send_slack(parse['subject'], text)


if __name__ == '__main__':
    execute = Execute()
    execute.send_gmail_to_slack()
