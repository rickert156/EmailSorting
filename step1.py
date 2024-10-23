import csv, time
from utils.createDir import createDir
from utils.searchFile import selectBase
from utils.addEmail import addListEmail, readSetEmail, returnEmail
from utils.exceptList import returnSetExceptEmail, returnSetExceptDomain
from utils.validEmail import ClearExceptionEmail

EXCEPT_DIR = 'Exception'
EXCEPT_EMAIL = f'{EXCEPT_DIR}/email.txt'
EXCEPT_DOMAIN = f'{EXCEPT_DIR}/domain.txt'

EXCEPT_SET_EMAIL = set()

MAIN_EXCEPT_EMAIL = set()
MAIN_EXCEPT_DOMAIN = set()

SET_EMAIL = set()

def notExceptSet():
    global MAIN_EXCEPT_EMAIL
    global MAIN_EXCEPT_DOMAIN
    global SET_EMAIL

    lenEmail = len(SET_EMAIL)
    lenExceptEmail = len(MAIN_EXCEPT_EMAIL)
    lenExceptDomain = len(MAIN_EXCEPT_DOMAIN)
    print(f'\nAll Emails: {lenEmail}\nAll Except Email: {lenExceptEmail}\nAll Except Domain: {lenExceptDomain}\n')

    clearExceptionEmail = ClearExceptionEmail(SET_EMAIL, MAIN_EXCEPT_EMAIL)
    countClearEmail = len(clearExceptionEmail)
    diff_email = lenEmail - countClearEmail
    print(f'All Email(clear): {countClearEmail}\tDelete {diff_email} email')


def InitExcept():
    global MAIN_EXCEPT_EMAIL
    global MAIN_EXCEPT_DOMAIN

    MAIN_EXCEPT_EMAIL = returnSetExceptEmail()
    MAIN_EXCEPT_DOMAIN = returnSetExceptDomain()


def readBase():
    global SET_EMAIL
    try:
        TARGET_BASE = selectBase()

        with open(TARGET_BASE, 'r') as file:
            number_email = 0
            for row in csv.DictReader(file):
                number_email+=1
                email = row['Email']
                print(f'[{number_email}] {email}')
                addListEmail(email)
            
            time.sleep(1)
            readSetEmail()

    except TypeError as err:
        print(f'Error: {err}')
    
    try:
        filename = TARGET_BASE.split('/')[1]
        print(filename)
        time.sleep(1)
        SET_EMAIL = returnEmail()
    except Exception as err:print(f'Error: {err}')

if __name__ == '__main__':
    createDir()
    readBase()
    InitExcept()
    notExceptSet()
