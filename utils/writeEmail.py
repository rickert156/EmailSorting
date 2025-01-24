import csv, os

RESULT_DIR = 'Result'

def writeEmailStepOne(filename:str, name:str, email:str, company:str, domain:str, category:str, source:str):
    list_email = []

    result_path = f'{RESULT_DIR}/{filename}'
    
    if not os.path.exists(result_path):
        with open(result_path, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Company', 'Domain', 'Category', 'Source'])
    
    with open(result_path, 'r') as file:
        for row in csv.DictReader(file):
            select_email = row['Email']
            list_email+=[select_email]

    #if email not in list_email:
    with open(result_path, 'a+', newline='') as file:
        write = csv.writer(file)
        write.writerow([name, email, company, domain, category, source])

