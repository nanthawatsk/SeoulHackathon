import requests

url = "http://localhost:5002/process_video"

video_path = "/Users/tententgc/Documents/seoul-incident-reporter/test-input/WhatsApp Video 2567-09-06 at 14.38.59.mp4"


with open(video_path, 'rb') as video_file:
    files = {'video': video_file}
    response = requests.post(url, files=files)


print(response.json())