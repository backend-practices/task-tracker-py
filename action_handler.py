import datetime
from file_handler import saveFile, readFile
from task import Task

now: float = datetime.datetime.now().timestamp()
filename: str = './db/tasks.json'

def addAction(descriptions: str):
    try:
        tasks: list = readFile(filename)    
        for description in descriptions:
            lastElementId = tasks[-1]['id'] if tasks else 0
            newTask = Task(
                id=lastElementId + 1,
                description=description,
                status='todo',
                createdAt=now,
                updatedAt=now)
            tasks.append(newTask.to_dict())
        saveFile(filename, tasks)
    except Exception as e:
        print('Error', e)
        
def updateAction(id: int, description: str):
    try:
        tasks: list = readFile(filename)
        for task in tasks:
            if task['id'] == id:
                task['description'] = description    
                task['updatedAt'] = now   
        print(tasks)
    except Exception as e:
        print('Error', e)
        
def updateStatus(ids: list, status: str):
    try:
        tasks: list = readFile(filename)
        for id in ids:
            for task in tasks:
                if task['id'] == int(id):
                    task['status'] = status    
                    task['updatedAt'] = now   
        print(tasks)
    except Exception as e:
        print('Error', e)
        
def deleteAction(ids: list):
    try:
        tasks: list = readFile(filename)    
        for id in ids:
            for task in tasks:
                if int(id) == task['id']: tasks.remove(task)
        saveFile(filename, tasks)
    except Exception as e:
        print('Error', e)
        
def listAction():
    try:
        tasks: list = readFile(filename)    
        print(tasks)
    except Exception as e:
        print('Error', e)
        
def listByStatus(status: str):
    try:
        tasks: list = readFile(filename)  
        result: list = list(filter(lambda task: task['status']==status, tasks))
        print(result)
    except Exception as e:
        print('Error', e)