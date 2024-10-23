import csv

def ClearExceptionEmail(email, exceptionEmail):
    email.difference_update(exceptionEmail)

    return email

def ClearExceptionDomain(emailSet, exceptionDomain):
    ExceptionDomain = set()
    
    for domain in exceptionDomain:
        for email in emailSet:
            if domain in email:
                ExceptionDomain.add(email)
    
    emailSet.difference_update(ExceptionDomain)

    return emailSet

