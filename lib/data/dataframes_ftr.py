import pandas as pd
import numpy as np
import feather

filepath = "data/transaction_payer_id_merchant_id.feather"

df_x = feather.read_dataframe(filepath)
df_x.rename(
    columns={"transaction_payer_id": "user", "merchant_id": "item"}, inplace=True
)
df_x

filepath1 = "data/similarities.feather"
ds_x = feather.read_dataframe(filepath1)
ds_x