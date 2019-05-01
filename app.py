import os
import json
import time

from flask import Flask, request
import requests

app = Flask(__name__)

#GroupMe will POST to url every time message is received in chat
@app.route('/', methods=['GET']) 
def simpleCheck():
    return "Web Server is up."

@app.route('/transaction', methods=['POST'])
def makeTransaction():
    data = request.get_data()
    return data

#GroupMe will POST to url every time message is received in chat
@app.route('/', methods=['POST']) 
def webserver():
    data = request.get_json()
    if (data['text'][0:7]).lower() == "@google":        #GroupMe will POST to url every time message is received in chat
        searchTerm = createSearchTerm(data['text'][7:]) #Create URL from remaining message
        sendMessage(searchTerm)                         #Send message back to GroupMe
    return "ok", 200

#Function to create request body and POST to groupme
def sendMessage(searchTerm):
    postUrl = 'https://api.groupme.com/v3/bots/post'    #Defined URL for sending messages

    payload = {
                'text' : searchTerm,
                'bot_id' :  os.getenv('GROUPME_BOT_ID'),    #Bot ID to prove identity
            }

    time.sleep(1)   #Minor delay to ensure proper order of messsages
    r = requests.post(postUrl, data = payload, verify=True) #Post message to url using requests library

def createSearchTerm(data):
    terms = data.split()    #Split message body on each space
    search = ""
    for term in terms:
        search = search + term + "+"    #Add '+' for proper URL formatting
    search = "https://www.google.com/search?q="+search
    return search       #Return complete search URL











