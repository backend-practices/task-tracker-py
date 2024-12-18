import datetime
import json
from file_handler import writeFile, readFile

now: float = datetime.datetime.now().timestamp()
filename: str = './db/tasks.json'

def addAction(description:str):
    try:
        contentStr = readFile(filename)
        
        contentJson = json.load(contentStr)
        
        print(contentJson)
        
        # data: object = [
        #     {
        #         "id": 1,
        #         "description": description,
        #         "status": "todo",
        #         "createdAt": now,
        #         "updatedAt": now
        #     }
        # ]
        # writeFile(filename, json.dumps(data))
    except:
        print('Error')