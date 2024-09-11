import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
import requests
from telegram_bot import server_push_notifications
from call import message_call
class AccidentAnalyzer:
    def __init__(self):
        load_dotenv() 
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_accident(self, image_path): 
        base64_image = self.encode_image(image_path)
         
        response = self.client.chat.completions.create(
            model="gpt-4o",  
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": '''
                         Response should be in the following format and take short each topic but having a key important
                         **1.Incident Overview :** 
                            - A brief description of the accident and what seems to have happened.
                        **2.Location of the Accident:** 
                            - Describe the place where the accident occurred (street, intersection, highway, building, etc.).
                            -Include details like traffic conditions, weather, lighting, or any hazards present.
                        **3.Vehicles/Objects Involved :** 
                            -identify the vehicles, objects, or structures involved in the accident (e.g., cars, trucks, motorcycles, bicycles, etc.).
                            -Mention any visible damage to the vehicles or objects.
                        **4.People Involved:** 
                            -Number of people involved, including drivers, passengers, and pedestrians.
                            -Visible injuries, expressions, and the actions they are taking (e.g., helping each other, calling for help, etc.).  
                        **5.Damage Assessment:** 
                            - Extent of damage to vehicles, property, or infrastructure.
                            - Any potential secondary hazards (e.g., fuel leakage, debris, fire risk).
                        **6. summary Case:**  
                            - show and analysis what happended in the image
                            
                         '''},
                        {
                            "type": "image_url",
                            "image_url": {
                                 "url": f"data:image/jpeg;base64,{base64_image}",
                            }
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        
        message_content = response.choices[0].message.content
        server_push_notifications(message_content)
        
        # speech_file_path = "speech_report.mp3"
        # sound_response= self.client.audio.speech.create(
        # model="tts-1",
        # voice="alloy",
        # input=f"{message_content}"
        # )

        # sound_response.stream_to_file(speech_file_path)
        message_call()
        return message_content


