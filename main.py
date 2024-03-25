#Logan Slowik
import json
event = {
    "day":0,
    "month":0,
    "year":0,
    "startTime":0,
    "endTime":0
}

jsonObj = json.dumps(event,indent=4)
with open("out.json","w") as outFile:
    outFile.write(jsonObj)
