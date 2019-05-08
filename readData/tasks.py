import json
import urllib.request
from .models import Temperature, Humidity
from celery import task

@task
def readDataScheduler():
    url = urllib.request.Request('https://api.thingspeak.com/channels/722545/feeds.json?results=2')
    response = urllib.request.urlopen(url)

    json_object = json.loads(response.read())

    for entry in json_object["feeds"]:
        id = entry["entry_id"]
        temp_value = entry["field1"]
        humidity_value = entry["field2"]
        date_time = entry["created_at"].split('T')
        date = date_time[0]
        time = date_time[1].split('Z')[0]

        temp = Temperature(id, temp_value, date)
        temp.save()
        print(id)    
        print(humidity_value)
        humidity = Humidity(id, humidity_value, date)
        humidity.save()
   


