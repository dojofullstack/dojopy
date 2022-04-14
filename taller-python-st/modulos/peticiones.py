# from chatbot import * 
# import chatbot
# from chatbot import chatbot
# from terceros.new_module import news
# import requests
import requests
import json
# print(chatbot())
# print(news())

# https://ipapi.co/json/

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }

data = requests.post('https://ipapi.co/json', headers=headers)
print(data.status_code)
# print(data.text)
data = data.content
data = json.loads(data)
print(data)
print('--'*10)
print(data.get('country'))
print(data.get('currency'))