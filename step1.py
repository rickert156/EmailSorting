import csv
from utils.createDir import createDir
from utils.searchFile import selectBase

TARGET_BASE = selectBase()

def readBase():
    with open(TARGET_BASE, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            number_email+=1
            email = row['Email']
            print(f'[{number_email}] {email}')

readBase()
