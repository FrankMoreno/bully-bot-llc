import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    if data['name'] != 'Bully':
        createMessage(data)
    return "ok", 200

def createMessage(data):
    postUrl = "https://api.groupme.com/v3/bots/post"

    payload = {
                "bot_id" :  os.getenv('GROUPME_GOT_ID'),
                "text" : "Shut up" + data['name']
            }

    request = Request(postUrl, urlencode(payload).encode())
    json = urlopen(request).read().decode()






