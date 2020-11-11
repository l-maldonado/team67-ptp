import pandas as pd
import numpy as np
import feather

filepath = "team67-ptp/data/transaction_payer_id.ftr"
"""filepath3 = "team67-ptp/data/payers_2.csv"
df_test = pd.read_csv(filepath3, usecols=["transaction_payer_id"])
print(df_test.head())
"""

df_x = feather.read_dataframe(filepath)
df_x.rename(
    columns={"transaction_payer_id": "user", "merchant_id": "item"}, inplace=True
)
df_x
