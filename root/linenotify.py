import requests
ACCESS_TOKEN = "SpZO5Ll4waJmi0qYGdRrDWMs9fYLZeMULUqyldOWcJG"

url = "https://notify-api.line.me/api/notify"
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN} # 発行したトークン
message =  'ここにメッセージを入れます'
payload = {"message" :  message}
files = {"imageFile": open("1.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

r = requests.post(url ,headers = headers ,params=payload, files=files)
