from openpyxl import load_workbook
import numpy as np
import pandas as pd
while(1):
    print("\nMake a choice to proceed...")
    print("Press 1 to Add user.")
    print("Press 2 to Display a user.")
    print("Press 3 to End.")
    # print("Press any key to Continue:-...")

    key = int(input("Press any key to Continue:-..."))
    match key:
        case 1:
            name = input("Enter Your Name:-")
            email = input("Enter your email:-")
            mobile = int(input("enter your mobile number:-"))

            data = {
                    "Name": [name],
                    "Email" : [email],
                    "Mobile" :[mobile]
                    }
            
            df_new = pd.DataFrame(data)
            dt = pd.read_csv('Book2.csv')
            ft_combined = dt._append(df_new)
            ft_combined.to_csv('Book2.csv',index = False)
            
        case 2:
            dt_read = pd.read_csv('Book2.csv')
            print(dt_read)
            
        case 3:
            break