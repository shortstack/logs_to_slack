import os
import sys
import requests
import time
import json

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def logs_to_slack():

    logfile = open('/path/to/logs/omg', 'r')
    loglines = follow(logfile)

    for line in loglines: 

        if "unicorn" in line:           # you can parse for specific entries by keyword, or comment this out to include everything  
    
            line = json.loads(line) 

            field1 = line["field1"]
            field2 = line["field2"]
            field3 = line["field3"]

            webhook_url = "https://hooks.slack.com/goes/here"
            data = {
                "attachments": [
                    {
                        "fallback": line,
                        "icon_emoji": ":unicorn:",
                        "color": "#FF1694",
                        "title": "My Logs",
                        "title_link": "https://angry.unicorns.lol",
                        "fields": [
                            {
                                "title": "Field 1",
                                "value": field1,
                                "short": False
                            },
                            {
                                "title": "Field 1",
                                "value": field2,
                                "short": False
                            },
                            {
                                "title": "Field 1",
                                "value": field3,
                                "short": False
                            }
                        ]
                    }
                ]
            }

            response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

logs_to_slack()
