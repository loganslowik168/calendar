#Logan Slowik
import json
from event import event
#create list of events. initialize empty.
events = []
#restore events to last state
with open("out.json","r") as inFile:
    events = [json.load(inFile)]

def AddNewEvent(day,month,year,ST,ET):
    temp=event(day,month,year,ST,ET)
    events.append(temp)

AddNewEvent(1,2,3,"01:23","04:22")
AddNewEvent(1,2,3,"05:23","23:59")
#write data back to file
'''
jsonObj = json.dumps(event,indent=4)
with open("out.json","w") as outFile:
    outFile.write(jsonObj)
'''
for event in events:
    print(event)
print(len(events))