import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
class Finance_Tracker:
    CSV_file = "budget_tracker.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    
    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_file, index=False)
            
    @classmethod
    def append_to_csv(cls, date, amount, category, description):
        addItem = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description
        }
        
        with open(file=cls.CSV_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=cls.COLUMNS)
            writer.writerow(addItem)
        print("Entry Added Successfully")  
        
    @classmethod
    def retrieve_data(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_file)
        df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        print(filtered_df) 
        
        if not filtered_df:
            print("No Data Exists")     
        else:
            print(f"The Transaction from {start_date.strftime("%d-%m-%Y")} to {end_date.strftime("%d-%m-%Y")}")    
        
def main():
    Finance_Tracker.intialize_csv()
    date = get_date("Enter the date of the transaction dd-mm-yy ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    Finance_Tracker.append_to_csv(date=date, amount=amount, category=category, description= description)          
            
            
# main()

    
Finance_Tracker.retrieve_data("01-01-2025", "30-03-2025")    
# Finance_Tracker.append_to_csv("27-02-2025", 500.00, "Incoming", "PocketMoney")                