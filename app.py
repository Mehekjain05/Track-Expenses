import pandas as pd
import csv
from datetime import datetime

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
            
            
            
    
    
    
# Finance_Tracker.append_to_csv("27-02-2025", 500.00, "Incoming", "PocketMoney")                