import logging
import pandas as pd
import os
import pickle
import numpy as np
import pandas as pd
import joblib


data_sample = pd.DataFrame({"loan_amnt": pd.Series([0.0], dtype="float32"), "term": pd.Series([0], dtype="int8"), "int_rate": pd.Series([0.0], dtype="float32"), "grade": pd.Series(["example_value"], dtype="object"), "emp_title": pd.Series(["example_value"], dtype="object"), "emp_length": pd.Series([0], dtype="int8"), "home_ownership": pd.Series(["example_value"], dtype="object"), "annual_inc": pd.Series([0.0], dtype="float32"), "verification_status": pd.Series(["example_value"], dtype="object"), "purpose": pd.Series(["example_value"], dtype="object"), "dti": pd.Series([0.0], dtype="float32")})
model = joblib.load('model.pkl')
result = model.predict_proba(data_sample)
print(result)