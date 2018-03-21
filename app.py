import os
import json
import time

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def simpleCheck():
    return "Web Server is up."
    
@app.route('/', methods=['POST'])
def webserver():
    data = request.get_json()
    if (data['text'][0:7]).lower() == "google:":
        searchTerm = createSearchTerm(data['text'][7:])
        createMessage(searchTerm)
    return "ok", 200

def createMessage(searchTerm):
    postUrl = 'https://api.groupme.com/v3/bots/post'

    payload = {
                'text' : searchTerm,
                'bot_id' :  os.getenv('GROUPME_BOT_ID'),
            }

    time.sleep(1)
    r = requests.post(postUrl, data = payload, verify=True)

def createSearchTerm(data):
    terms = data.split()
    search = ""
    for term in terms:
        search = search + term + "+"
    search = "https://www.google.com/search?q="+search
    return search











