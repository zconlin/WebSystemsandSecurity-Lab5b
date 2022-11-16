# Server Hardening Documentation

__Name__: Zac Conlin

This project documents the outputs of some custom IP address jails, and a python script that will send a text message to an admin every time a ban occurs.

## Fail2Ban Log

![Fail2Ban Log](./documentation/screenshot%20the%20test-jail%20ban%20activity.png)

## Custom Jails

### `jail.local`

![Jail.local](./documentation/screenshot%20of%20jail.png)

### `filter.d/jail.conf`

![relevant lines](./documentation/screenshot%20of%20filter.png)

...

## `fail2ban-regex`

![output showing matches](./documentation/screenshot%20logs%20that%20show%20the%20banned%20IP.png)

![Custom Jail(s) ban activity](./documentation/screenshot%20logs%20that%20show%20the%20banned%20IP.png)

## Python script

```Python
# Download the helper library from https://www.twilio.com/docs/python/install
from decouple import config
from twilio.rest import Client
import sys

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
```

This script will send a text message through Twilio the the administrator every time an IP is banned or unbanned. This could be useful because it will notify them that unseemly behavior was going on with the server so they can be aware and alert about potential problems.
