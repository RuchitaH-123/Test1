import numpy as np
import pandas as pd
from openpyxl import load_workbook

nam = input("Enter name")
dict1  ={
    "name":[nam,"har","suh"],
    "marks":[52,56,36],
}

df = pd.DataFrame(dict1)
# print(df)
dt= df.to_csv('Book1.csv',index=False)


