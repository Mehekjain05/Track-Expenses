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
            
            
    
    
    
Finance_Tracker.intialize_csv()                