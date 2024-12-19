import json

# READ FILE

def readFile(filename: str):
    try: 
        with open(filename) as f: return json.load(f)
    except FileNotFoundError: 
        print('File does not exist.')
        return []
    except json.JSONDecodeError:
        print('Error occurs while reading the file.')
        return []


# APPEND FILE

# WRITE FILE

def saveFile(filename: str, data: str):
    ## create the file if it does not exist
    try:
        content = json.dumps(data)
        f = open(filename, 'w')
        f.write(content)
        f.close()
        print('Task updated.')
    except:
        print('Error occurs while writting the file.')

# CREATE FILE