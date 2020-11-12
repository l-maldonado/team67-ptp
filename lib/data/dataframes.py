import pandas as pd

filename1 = "data/payer_merchant.csv"
filename2 = "data/similarities.csv"

df_x = pd.read_csv("data/transaction_payer_id_merchant_id.csv")
df_x.rename(
    columns={"transaction_payer_id": "user",
             "merchant_id": "item"}, inplace=True
)
df_x

ds_x = pd.read_csv("data/similarities.csv")
ds_x
