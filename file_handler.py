import os

# READ FILE

def readFile(filename: str)-> str:
    try:
        f = open(filename)
        content: str = f.read()
        f.close()
        return content
    except:
        print('Error occurs while reading the file.')
        print('File does not exist.')
        return ''


# APPEND FILE

# WRITE FILE

def writeFile(filename: str, data: str):
    ## create the file if it does not exist
    try:
        f = open(filename, 'w')
        f.write(data)
        f.close()
    except:
        print('Error occurs while writting the file.')

# CREATE FILE