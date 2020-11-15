"""
File to import csv file in data dir and convert into dataframe
"""
import pandas as pd
# from app import cache

filename1 = "data/transaction_merchant.csv"
filename2 = "data/similarities_2.csv"
filename3 = "data/merchants.csv"


#@cache.memoize(timeout=120)
def get_db(filename=filename1):
    df_x = pd.read_csv(filename1)
    df_x.rename(
        columns={"transaction_payer_id": "user",
                "merchant_id": "item"}, inplace=True
    )
    return df_x

ds_x = pd.read_csv(filename2)
ds_x
