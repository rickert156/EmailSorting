import os

EXCEPT_DIR = 'Exception'
EXCEPT_EMAIL = f'{EXCEPT_DIR}/email.txt'
EXCEPT_DOMAIN = f'{EXCEPT_DIR}/domain.txt'

SET_EXCEPT_EMAIL = set()
SET_EXCEPT_DOMAIN = set()

def returnSetExceptEmail():
    global SET_EXCEPT_EMAIL
    with open(EXCEPT_EMAIL, 'r') as file:
        for email in file.readlines():
            email = email.strip()
            SET_EXCEPT_EMAIL.add(email)

    return SET_EXCEPT_EMAIL

def returnSetExceptDomain():
    global SET_EXCEPT_DOMAIN
    with open(EXCEPT_DOMAIN, 'r') as file:
        for email in file.readlines():
            email = email.strip()
            SET_EXCEPT_DOMAIN.add(email)

    return SET_EXCEPT_DOMAIN
