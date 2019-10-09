# -*- coding: utf-8 -*-
import requests
import random
import os
import settings

ACCESS_TOKEN = settings.AT
imgFileNum = sum(len(files) for _, _, files in os.walk('img'))
print(str(imgFileNum))

messageList = ["おはよう! 今日も1日頑張ろうね☀️",
"おはよう! 身体に気をつけて1日ファイト🐱",
"おはよう😆 今日も寒いけど頑張ろう！",
"おはよう！昨晩はよく眠れた？？今日も1日頑張ろう😊",
"おはよう！昨日はお疲れ様。今日は無理しないでね😌"]

# messageList = ["Hello"]


url = "https://notify-api.line.me/api/notify"
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}  # 発行したトークン
message = random.choice(messageList)

payload = {"message":  message}
# バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。
files = {"imageFile": open("img/" + str(random.randrange(imgFileNum)+1) + ".jpg", "rb")}

if random.randrange(5) == 1 :
    r = requests.post(url, headers=headers, params=payload, files=files)
