import requests

auth = (
    'API_USERNAME',
    'API_PASSWORD'
    )

fields = {
    'from': '+821021751402',
    'to': '+46700000000',
    'voice_start': '{"play":"https://yourserver.example/files/hello.mp3"}'
    }

response = requests.post(
    "https://api.46elks.com/a1/calls",
    data=fields,
    auth=auth
    )

print(response.text)