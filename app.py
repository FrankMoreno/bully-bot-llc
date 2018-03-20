import os
import json

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    if data['name'] != 'Bully':
        createMessage(data)
    return "ok", 200

@app.route('/', methods=['GET'])
def simpleCheck():
    r = requests.post('https://bully-bot-llc.herokuapp.com/', data = {'name':'Frank Moreno'})
    return "You're ugly"

def createMessage(data):
    postUrl = 'https://api.groupme.com/v3/bots/post'

    payload = {
                'text' : "Shut up", #+ data['name']
                'bot_id' :  os.getenv('GROUPME_GOT_ID'),
            }

    print("Working maybe")
    request = requests.post(postUrl, payload)





