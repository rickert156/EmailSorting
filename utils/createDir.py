import os

def createDir():
    RESULT_DIR = 'Result'

    if not os.path.exists(RESULT_DIR):os.makedirs(RESULT_DIR)
