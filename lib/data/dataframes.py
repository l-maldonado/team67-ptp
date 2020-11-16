"""
File to import csv file in data dir and convert into dataframe
"""
import pandas as pd
# from app import cache

filename1 = "data/transaction_merchant.csv"
filename2 = "data/similarities.csv"
filename3 = "data/cluster_test.csv"


df_x = pd.read_csv(filename1)
df_x.rename(
    columns={"transaction_payer_id": "user",
             "merchant_id": "item"}, inplace=True
)
df_x

ds_x = pd.read_csv(filename2)
ds_x

df_c = pd.read_csv(filename3)
df_c
