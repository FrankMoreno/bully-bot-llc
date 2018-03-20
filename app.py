import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)

GROUPME_BOT_ID = os.getenv('GROUPME_GOT_ID')

@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    data.dumps()

    return "ok", 200

def createMessage():
    {
        "attachments": [],
        "avatar_url": "",
        "created_at": 1302623328,
        "group_id": "1234567890",
        "id": "1234567890",
        "name": "John",
        "sender_id": "12345",
        "sender_type": "user",
        "source_guid": "GUID",
        "system": False,
        "text": "Hello world ☃☃",
        "user_id": "1234567890"
}






