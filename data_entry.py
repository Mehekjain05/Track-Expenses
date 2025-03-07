from datetime import datetime
CATEGORIES = {
    'I' : "Incoming",
    'O' : "Outgoing"
}

def get_date(prompt, allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    
    try:
        valid_date = datetime.strptime(date_str,"%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Please enter a valid format in dd-mm-yyyy")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amt = int(input("Enter the amount "))
        if amt <= 0:
            print("Amount should be positive and Nonzero")
        return amt    
    except ValueError as e:
        print("Please enter a valid amount.." + e)
        return get_amount()
                

def get_category():
    try:
        category = input("Entry I => Credited or O => Debited ").upper()
        for category in CATEGORIES:
            return CATEGORIES[category]
    except ValueError as e:
        print("Enter category from the options" + e)
        return get_category()    

def get_description():
    try:
        description = input("Enter the description ")
        return description
    except Exception as e:
        print("Enter a valid Description" + e)
        return get_description()