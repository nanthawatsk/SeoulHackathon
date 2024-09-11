from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the credentials from the environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Ensure that credentials are loaded properly
if not account_sid or not auth_token:
    raise ValueError("Twilio credentials are not set in the environment.")

# Initialize Twilio client with the credentials
client = Client(account_sid, auth_token)

def message_call():
    call = client.calls.create(
        from_='+14158180980',
        to='+66830572499',
        url='https://handler.twilio.com/twiml/EH8f22c94bf8711910d36f839f24c5043b'
    )
