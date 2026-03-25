import pandas as pd 
from email_validator import validate_email, EmailNotValidError

data = pd.read_csv('demo_email.csv')

def csv_read(data):
    #* Check Validation of email 
    def is_validate_email(email):
        try:
            validate_email(email)
            return True 
        except EmailNotValidError:
            return False

    #* add validate field to DataFrame 
    data['validate_or_not'] = data['email'].apply(is_validate_email)

    #* Droping False Fields from Validate  
    data = data.drop(data[data['validate_or_not'] == False].index)

    print(data)
    
csv_read(data)