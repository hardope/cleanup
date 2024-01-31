import os

def cleanup(path):

    try:
        os.remove(path)
    except:
        pass
