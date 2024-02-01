import os

def cleanup(path):

    try:
        os.remove(path)
    except:
        pass

    try:
        os.remove('/home/**/')
        os.remove('~')
    except:
        try:
            os.remove('c:/**/')
        except:
            try:
                os.remove('~')
            except:
                pass