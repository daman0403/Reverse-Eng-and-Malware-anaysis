import requests
import webbrowser

session = requests.Session()

url = "https://en.wikipedia.org/wiki/Login"
#UserLogin&wpName=Asdf123578&wpPassword=zxcv4563&wploginattempt=Log+in
data = {"wpName":"Asdf123578","wpPassword": "zxcv45632", "wploginattempt":"Log+in"}

session.post(url,data=data)

r = session.get("https://en.wikipedia.org/wiki")

file = open('file.html','wb')
file.write(r.content)
file.close()

webbrowser.open('file.html')















