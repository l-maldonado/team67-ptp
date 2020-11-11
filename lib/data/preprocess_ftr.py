import pandas as pd
import feather
import os

preprocess_mf = __import__("preprocessor").preprocess_mf
preprocess_sf = __import__("preprocessor").preprocess_sf
preprocess_mf3 = __import__("preprocessor").preprocess_mf3
preprocess_var = __import__("preprocessor").preprocess_var
preprocess_mul = __import__("preprocessor").preprocess_mul

# Usage
#  Call the function depending how many variales you want to transform

filename = "team67-ptp/data/placetopayDB4.ftr"
# preprocess_mf(filename, "transaction_payer_id", "merchant_id")
preprocess_mul(filename, "transaction_payer_id", "merchant_id")
