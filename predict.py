import numpy as np
import pandas as pd
import warnings
import pickle

df_numeric_norm = ['emp_length_0', 'emp_length_1', 'emp_length_2', 'emp_length_3', 'emp_length_4', 'emp_length_5', 'emp_length_6', 'emp_length_7', 'emp_length_8', 'emp_length_9', 'emp_length_10', 'emp_title_account manager', 'emp_title_accountant', 'emp_title_administrative assistant', 'emp_title_administrator', 'emp_title_analyst', 'emp_title_assistant manager', 'emp_title_attorney', 'emp_title_branch manager', 'emp_title_ceo', 'emp_title_clerk', 'emp_title_consultant', 'emp_title_controller', 'emp_title_customer service', 'emp_title_director', 'emp_title_driver', 'emp_title_electrician', 'emp_title_engineer', 'emp_title_executive assistant', 'emp_title_foreman', 'emp_title_general manager', 'emp_title_machine operator', 'emp_title_manager', 'emp_title_mechanic', 'emp_title_nurse', 'emp_title_office manager', 'emp_title_operations manager', 'emp_title_operator', 'emp_title_other', 'emp_title_owner', 'emp_title_paralegal', 'emp_title_police officer', 'emp_title_president', 'emp_title_program manager', 'emp_title_project manager', 'emp_title_sales', 'emp_title_sales manager', 'emp_title_server', 'emp_title_software engineer', 'emp_title_store manager', 'emp_title_supervisor', 'emp_title_teacher', 'emp_title_technician', 'emp_title_truck driver', 'emp_title_vice president', 'verification_status_Source Not Verified', 'verification_status_Source Verified', 'grade_A', 'grade_B', 'grade_C', 'grade_D', 'grade_E', 'grade_F', 'grade_G', 'purpose_car', 'purpose_credit_card', 'purpose_debt_consolidation', 'purpose_educational', 'purpose_home_improvement', 'purpose_house', 'purpose_major_purchase', 'purpose_medical', 'purpose_moving', 'purpose_other', 'purpose_renewable_energy', 'purpose_small_business', 'purpose_vacation', 'purpose_wedding', 'home_ownership_any', 'home_ownership_mortgage', 'home_ownership_none', 'home_ownership_other', 'home_ownership_own', 'home_ownership_rent', 'loan_amnt', 'term', 'annual_inc', 'target', 'dti', 'int_rate']
LR_classifier_model = pickle.load(open('model.pkl', 'rb'))
def dict_to_dummies(dicc, df_numeric_norm):
    dummies_dict = dict.fromkeys(df_numeric_norm, 0)
    for key, value in dicc.items():
        special_key  = key+"_"+str(value)
        if key in df_numeric_norm:
            dummies_dict[key] = value
        elif special_key in df_numeric_norm:
            dummies_dict[special_key] = 1
        else:
            print("Problem with   ",special_key )
    return dummies_dict

def predict(dictt):
    df = pd.DataFrame(columns=df_numeric_norm)
    df = df.append(dict_to_dummies(dictt, df_numeric_norm), ignore_index=True)
    return int(LR_classifier_model.predict(np.array([df.iloc[0].drop("target").to_numpy()])))

def run(term,grade,int_rate,loan_amnt,emp_title,emp_length,home_ownership,verification_status,annual_inc,purpose,dti):

    dicc =  {'loan_amnt': loan_amnt,
         'term': term,
         'int_rate': int_rate,
         'grade': grade,
         'emp_title': emp_title,
         'emp_length': emp_length,
         'home_ownership': home_ownership,
         'annual_inc': annual_inc,
         'verification_status': verification_status,
         'target': 0,
         'purpose': purpose,
         'dti': dti}

    result=predict(dicc)

    return result