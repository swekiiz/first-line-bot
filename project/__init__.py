from flask import Flask, request, abort
import requests
import json
from project.Config import *

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        print(json.dumps(payload, indent=2))
        if message in ['Hello', 'hello']:
            ReplyMessage(Reply_token, 'Hi !', channel_access_token)
        return request.json, 200

    elif request.method == 'GET':
        return 'this is method GET!!!', 200

    else:
        abort(400)


@app.route('/')
def hello():
    return 'hello world!', 200


def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    data = {
        "replyToken": Reply_token,
        "messages": [{
            "type": "text",
            "text": TextMessage
        }]
    }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200
