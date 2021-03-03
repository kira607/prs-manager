import json
from typing import Optional
from bs4 import BeautifulSoup
from mail_client import MailClient

CREDENTIALS_PATH = "credentials/luxoft.json"



def parse_message(msg: dict) -> Optional[dict]:
    try:
        text = None
        content_type = msg['body-type']

        if content_type == "HTML":
            soup = BeautifulSoup(msg["body"], 'lxml')
            text = soup.body.text
        elif content_type == "Text":
            text = msg['body']

        if text is None:
            raise RuntimeError(f"Unknown message content type: {content_type}")

        text = text[text.find("{"):-1]
        text = text.strip()

        # drop non ascii characters
        text = text.encode('ascii', 'ignore')
        text = text.decode('utf-8')
        
        d = json.loads(text, strict=False)
        try:
            d["Message"] = json.loads(d["Message"].replace('\r\n', ' '))
        except: 
            pass
        return d
    except Exception as e:
        print(f"Could not parse message. Error: {e}")
        return None


def parse_notification(notif: dict) -> dict:
    pass


def load_credentials(path: str = CREDENTIALS_PATH) -> dict:
    with open(CREDENTIALS_PATH, "r") as file:
        raw = file.read()
    credentials = json.loads(raw)
    return credentials


if __name__ == "__main__":
    client = MailClient()
    client.set_credentials(load_credentials())
    inbox = client.get_inbox()
    print(f"found {len(inbox)} messages")
    for message in inbox:
        msg_dict = parse_message(message)