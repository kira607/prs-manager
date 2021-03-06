from exchangelib import Credentials, Account
from config import MailClientConfig as _config


class MailClient:
    def __init__(self):
        self.credentials = Credentials(_config.username, _config.password)
        self.account = None
        self.target_folder = 'AWSCodeCommitNotifications'

    def get_inbox(self) -> list:
        self.__login()
        messages = []
        notifications_folder = None
        for folder in self.account.inbox.children:
            if folder.name == self.target_folder:
                notifications_folder = folder
        for item in notifications_folder.all():
            messages.append(
                {
                    'time': str(item.datetime_received),
                    'subject': str(item.subject),
                    'sender': str(item.sender),
                    'body': str(item.body),
                    'body-type': item.body.body_type
                }
            )
        return messages

    def __login(self):
        self.account = Account(
            self.credentials.username,
            credentials=self.credentials,
            autodiscover=True
        )