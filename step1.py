import csv, time
from utils.createDir import createDir
from utils.searchFile import selectBase
from utils.addEmail import addListEmail, readSetEmail, returnEmail
from utils.exceptList import returnSetExceptEmail, returnSetExceptDomain
from utils.validEmail import ClearExceptionEmail, ClearExceptionDomain
from utils.writeEmail import writeEmailStepOne 


EXCEPT_DIR = 'Exception'
EXCEPT_EMAIL = f'{EXCEPT_DIR}/email.txt'
EXCEPT_DOMAIN = f'{EXCEPT_DIR}/domain.txt'

EXCEPT_SET_EMAIL = set()

MAIN_EXCEPT_EMAIL = set()
MAIN_EXCEPT_DOMAIN = set()

SET_EMAIL = set()

TARGET_BASE = False

def processingBase():
    global TARGET_BASE
    global SET_EMAIL

    filename = TARGET_BASE.split('/')[1]
    
    with open(TARGET_BASE, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            name = row['Name']
            email = row['Email']
            company = row['Company']
            if email in SET_EMAIL:
                number_email+=1
                print(f'[{number_email}] {email} {name} {company}')
                writeEmailStepOne(filename, name, email, company)
            


def notExceptSet():
    global MAIN_EXCEPT_EMAIL
    global MAIN_EXCEPT_DOMAIN
    global SET_EMAIL

    lenEmail = len(SET_EMAIL)
    lenExceptEmail = len(MAIN_EXCEPT_EMAIL)
    lenExceptDomain = len(MAIN_EXCEPT_DOMAIN)
    print(f'\nAll Emails: {lenEmail}\nEmails Exceptions(count): {lenExceptEmail}\nDomain Exceptions(count): {lenExceptDomain}\n')

    clearExceptionEmail = ClearExceptionEmail(SET_EMAIL, MAIN_EXCEPT_EMAIL)
    clearExceptionDomain = ClearExceptionDomain(SET_EMAIL, MAIN_EXCEPT_DOMAIN)
    
    countClearEmail = len(SET_EMAIL)
    diff_email = lenEmail - countClearEmail
    print(f'All Email(clear email): Total {countClearEmail} emails\tDelete {diff_email} emails')
    time.sleep(2)  
    processingBase()

def InitExcept():
    global MAIN_EXCEPT_EMAIL
    global MAIN_EXCEPT_DOMAIN

    MAIN_EXCEPT_EMAIL = returnSetExceptEmail()
    MAIN_EXCEPT_DOMAIN = returnSetExceptDomain()


def readBase():
    global SET_EMAIL
    global TARGET_BASE
    global PROCESSING_EMAIL
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
