import os
import json
import time

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    if (data['name'] != 'Bully' and data['name'] != 'GroupMe'):
        createMessage(data)
    return "ok", 200

@app.route('/', methods=['GET'])
def simpleCheck():
    return "Web Server is up."

def createMessage(data):
    postUrl = 'https://api.groupme.com/v3/bots/post'

    payload = {
                'text' : "Shut up " + data['name'],
                'bot_id' :  os.getenv('GROUPME_BOT_ID'),
            }
            
    time.sleep(1)
    r = requests.post(postUrl, data = payload, verify=True)







