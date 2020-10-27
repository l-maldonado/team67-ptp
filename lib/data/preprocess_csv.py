import pandas as pd

preprocess_var = __import__("preprocessor").preprocess_var
preprocess_mul = __import__("preprocessor").preprocess_mul

# Getting
# filename = "e:/Users/edwar/Desktop/place_to_pay/team67-ptp/lib/data/placetopayDB4.ftr"
# preprocess_var(filename, "transaction_card_installments")

filename = "C:/Users/anemi/OneDrive/Escritorio/dataframes/placetopayDB4.ftr"
preprocess_mul(filename, "isic_section_name", "transaction_processing_amount")
# def preprocess_mul(bd, var1, var2):
