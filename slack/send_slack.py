from slackclient import SlackClient

from slack.slack_info import (
    SLACK_TOKEN,
    CHANNEL,
    USERNAME
)


class SendSlack():

    def send_slack(self, title, text):
        sc = SlackClient(SLACK_TOKEN)

        attachments = [{
            'title': title,
            'text': text,
            'fallback': text
        }]

        sc.api_call(
            "chat.postMessage",
            channel=CHANNEL,
            user=USERNAME,
            attachments=attachments,
            text="you have unread mails in your gmail box"
        )