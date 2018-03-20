import os
import json

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    #if data['name'] != 'Bully':
    createMessage(data)
    return "ok", 200

@app.route('/', methods=['GET'])
def simpleCheck():
    r = requests.post("https://bully-bot-llc.herokuapp.com", data = {"var 1":"value", "var 2":"value"}, verify=True)
    return "Web Server is up."

def createMessage(data):
    postUrl = 'https://api.groupme.com/v3/bots/post'

    payload = {
                'text' : "Shut up", #+ data['name']
                'bot_id' :  os.getenv('GROUPME_BOT_ID'),
            }

    r = requests.post(postUrl, data = payload, verify=True)






