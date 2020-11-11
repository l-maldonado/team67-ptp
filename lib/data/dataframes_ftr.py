import pandas as pd
import numpy as np
import feather

filepath = "team67-ptp/data/transaction_payer_id.ftr"
filepath2 = "team67-ptp/data/placetopayDB4.ftr"
df_sim = feather.read_dataframe(filepath)
df2 = df_sim.transaction_payer_id
df3 = feather.read_dataframe(filepath2)
print(df2.iloc[0])
print()
print(df3.transaction_payer_id.iloc[0])
print()
"""filepath3 = "team67-ptp/data/payers_2.csv"
df_test = pd.read_csv(filepath3, usecols=["transaction_payer_id"])
print(df_test.head())
"""