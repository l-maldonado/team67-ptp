import pandas as pd

##### TRANSACTIONS CARD INSTALLMENTS #####
df_x = pd.read_csv(
    "C:/Users/anemi/OneDrive/Escritorio/dataframes/transaction_payer_id_merchant_id.csv"
)
df_x.rename(
    columns={"transaction_payer_id": "user", "merchant_id": "item"}, inplace=True
)
df_x

ds_x = pd.read_csv(
    "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/data/similarities.csv"
)

ds_x