# Download the helper library from https://www.twilio.com/docs/python/install
from decouple import config
from twilio.rest import Client
import sys


# https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python#send-an-sms-message-in-python-via-the-rest-api
# sudo tail -f /var/log/apache2/access.log

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

SECRET_SID = config('TWILIO_ACCOUNT_SID')
SECRET_AUTH = config('TWILIO_AUTH_TOKEN')
SECRET_FROM = config('from_')
SECRET_TO = config('to')

client = Client(SECRET_SID, SECRET_AUTH)

message = client.messages \
    .create(
         body='The following IP has been ' + sys.argv[1] + 'ned: ' + sys.argv[2],
         from_=SECRET_FROM,
         to=SECRET_TO
     )

print(message.sid)