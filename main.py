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

    filename = TARGET_BASE.split('/')[-1]
    processed_emails = set()  # Уникальные email из текущей сессии
    count_check = 0
    number_email = 0

    with open(TARGET_BASE, 'r') as file:
        reader = csv.DictReader(file)
        total_rows = sum(1 for _ in file)  # Подсчёт строк
        file.seek(0)  # Возврат указателя в начало для чтения данных

        print('\nProcessing...\n')
        for row in reader:
            count_check += 1
            email = row.get('Email')

            # Проверяем наличие email и его уникальность
            if email and '@' in email and email not in processed_emails and email in SET_EMAIL:
                number_email += 1
                processed_emails.add(email)
                print(f'[ {count_check} / {total_rows} ] processing...\t[ {number_email} ]')

                # Запись результата
                writeEmailStepOne(
                    filename=filename,
                    name=row.get('Name'),
                    email=email,
                    company=row.get('Company'),
                    domain=row.get('Domain'),
                    category=row.get('Category'),
                    source=row.get('Source')
                )

    print(f'Ready!\nOpen Result/{filename}')

def notExceptSet():
    global MAIN_EXCEPT_EMAIL
    global MAIN_EXCEPT_DOMAIN
    global SET_EMAIL

    lenEmail = len(SET_EMAIL)
    lenExceptEmail = len(MAIN_EXCEPT_EMAIL)
    lenExceptDomain = len(MAIN_EXCEPT_DOMAIN)
    print(f'\nAll Emails: {lenEmail}\nEmails Exceptions(count): \t{lenExceptEmail}\nDomain Exceptions(count): \t{lenExceptDomain}\n')

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
                addListEmail(email)
            
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
