import pandas as pd
import numpy as np
import feather

filepath = "E:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/isic_section_name_transaction_processing_amount.ftr"
df_x = feather.read_dataframe(filepath)

# print(df_x.info())

df_x["logarithm"] = np.log(df_x["transaction_processing_amount"])
df_x
print(df_x.info())

["logarithm"] = np.log(df_x["transaction_processing_amount"])
df_x
print(df_x.info())

np.random.seed(135568109)
ndata = len(df_x)
idx_80 = np.random.choice(range(ndata), int(0.8 * ndata), replace=False)
idx_20  = np.asarray(list(set(range(ndata)) - set(idx_train)))
data_80    = df_x.iloc[idx_80] 
data_20      = df_x.iloc[idx_20] 
data_20
