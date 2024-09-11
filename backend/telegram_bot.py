import os
import time
import requests
import telepot

def server_push_notifications(message_content):
    try:
        kakao_map_link = "https://map.kakao.com/link/map/incident_point,37.402056,127.108212"
        message_content_with_link = f"{message_content}\n\nLocation: [Kakao Map]({kakao_map_link})"

        url = f"https://api.telegram.org/bot7355623583:AAGKeiusZvOrtMTlr1X7MiMDNt3w3Jl7XO0/sendMessage"
        response = requests.post(
            url=url,
            params={'chat_id': -4524627260, 'text': f"{message_content_with_link}", 'parse_mode': 'Markdown'}
        )

        image_path = 'accident_frame/accident_img.jpg'
        if os.path.exists(image_path):
            bot = telepot.Bot('7355623583:AAGKeiusZvOrtMTlr1X7MiMDNt3w3Jl7XO0')
            bot.sendPhoto(-4524627260, photo=open(image_path, 'rb'))
        else:
            print(f"Error: File {image_path} not found!")

        print(url, response.json())
        time.sleep(10)

    except KeyboardInterrupt:
        return 
