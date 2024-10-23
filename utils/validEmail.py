import csv

def ClearExceptionEmail(email, exceptionEmail):
    email.difference_update(exceptionEmail)
    
    return email

