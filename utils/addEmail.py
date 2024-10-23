import os

SET_EMAIL = set()

def returnEmail():
    global SET_EMAIL
    return SET_EMAIL

def readSetEmail():
    global SET_EMAIL

    number_email = 0
    for email in SET_EMAIL:
        number_email+=1
        #print(f'[{number_email}] {email}')

def addListEmail(email):
    global SET_EMAIL
    SET_EMAIL.add(email)

