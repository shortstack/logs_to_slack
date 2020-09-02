# logs_to_slack

Quick and dirty python script/systemd service that will watch a log file and spit out some or all contents to Slack via webhook.

This assumes your logs are JSON. If they are not, you can always do something similar to the following in `logs_to_slack.py`:

```
line = line.split(" - ")

field1 = line[0]
field2 = line[1]
field3 = line[2]
```

## Install 

```
pip install -r requirements.txt 
cp logs_to_slack.service /etc/systemd/system/
cp logs_to_slack.py /opt
systemctl enable logs_to_slack 
systemctl start logs_to_slack
```
