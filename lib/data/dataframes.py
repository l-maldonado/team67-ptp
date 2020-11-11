import pandas as pd

##### TRANSACTIONS CARD INSTALLMENTS #####
"""
df_ci = pd.read_csv(
    "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/transaction_card_installments.csv"
)

df_ci

df_t = pd.read_csv(
    "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/db/transaction_description.csv"
)
df_t = (
    df_t.groupby("transaction_description")
    .size()
    .reset_index()
    .sort_values(by=[0], ascending=False)
)
df_t = df_t.reset_index(drop=True)
df_t = df_t.rename(columns={0: "amount"})
df_t = df_t.iloc[0:21]
"""

df_x = pd.read_csv(
    "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/data/transaction_payer_id_merchant_id.csv"
)
df_x.rename(
    columns={"transaction_payer_id": "user", "merchant_id": "item"}, inplace=True
)
df_x

ds_x = pd.read_csv(
    "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/data/similarities.csv"
)

ds_x