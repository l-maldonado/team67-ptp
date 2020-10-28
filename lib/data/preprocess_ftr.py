import pandas as pd
import feather

preprocess_mf3 = __import__("preprocessor").preprocess_mf3
filename = "C:/Users/anemi/OneDrive/Escritorio/dataframes/placetopayDB4.ftr"
# preprocess_mf(filename, "isic_section_name", "transaction_processing_amount")

preprocess_mf3(
    filename,
    "isic_section_name",
    "transaction_processing_amount",
    "transaction_processing_date_",
)
