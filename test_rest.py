import requests


url = 'http://127.0.0.1:8000/'
req = requests.post(url=url,data={
    'pk':1,
    'status':'completed'
})
print(req)