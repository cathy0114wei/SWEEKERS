# pip install requests
import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "<YourSlack'sWebHookURLhere>"
    message = ("This is my message")
    title = (f"This is the Title:zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        "channel" : "#job-updates",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
