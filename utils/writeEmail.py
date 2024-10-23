import csv

RESULT_DIR = 'Result'

def writeEmailStepOne(filename, name, email, company):
    NAME, EMAIL, COMPANY = 'Name', 'Email', 'Company'
    fieldnames = [NAME, EMAIL, COMPANY]
    with open(f'{RESULT_DIR}/{filename}', 'a+', newline='') as file:
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writerow({NAME:name, EMAIL:email, COMPANY:company})

