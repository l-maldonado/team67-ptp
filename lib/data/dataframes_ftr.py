import pandas as pd
import numpy as np
import feather

filepath = "C:/Users/anemi/OneDrive/Escritorio/Dash/team67-ptp/lib/data/isic_section_name_transaction_processing_amount.ftr"
df_x = feather.read_dataframe(filepath)
# print(df_x.info())
df_x["logarithm"] = np.log(df_x["transaction_processing_amount"])
print(df_x.info())
df_x