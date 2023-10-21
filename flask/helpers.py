import __main__ as main
import os
import pandas as pd

def get_path(path):
    if (not hasattr(main, '__file__')):
        full_path = path
    else:   
        os_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(
            os_path, path)

    return full_path

def df_to_response(df, app): 
    json_data = df.to_json(orient='records')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def csv_to_clean_df(csv_path): 
    file_name = csv_path

    file_path = get_path(file_name)

    df = pd.read_csv(file_path)
    
    rename_dict = {'Lower tier local authorities Code': 'ltla_code',
                'Lower tier local authorities': 'ltla_name',
                'Age (B) (6 categories)': 'age_category',
                'Age (C) (5 categories)': 'age_category',
                'Age (9 categories)': 'age_category',
                'Age (9 categories)': 'age_category',
                'Age (6 categories)': 'age_category',
                'Age (5 categories)': 'age_category',
                'Ethnic group (20 categories)': 'ethnicity',
                'Ethnic group (20 categories) Code': 'ethnicity_code',
                'Sex (2 categories)': 'gender',
                'Observation': 'observation',
                'Ethnic group (6 categories)': 'ethnicity_simplified',
                'Ethnic group (6 categories) Code': 'ethnicity_simplified_code',
                'Economic activity status (7 categories)': 'employment_status',
                'Economic activity status (7 categories) Code': 'employment_status_code',
                'Economic activity status (4 categories)': 'employment_status_simplified',
                'Economic activity status (4 categories) Code': 'employment_status_simplified_code',
                'Occupation (current) (10 categories)': 'occupation',
                'Disability (3 categories) Code': 'disability_status_code', 
                'Disability (3 categories)': 'disability_status',
                'Economic activity status (4 categories) Code': 'employment_status_simplified_code'                
                }
    
    df.rename(columns=rename_dict, inplace=True)

    if 'gender' in df.columns:
        df['gender'] = df['gender'].apply(str.lower)

    return df


def ethnicity_translation():  
    ethnicity_lables_translation = {
        'Does not apply': 'Does not apply',
        'Asian, Asian British or Asian Welsh: Bangladeshi': 'Bangladeshi',
        'Asian, Asian British or Asian Welsh: Chinese': 'Chinese',
        'Asian, Asian British or Asian Welsh: Indian': 'Indian',
        'Asian, Asian British or Asian Welsh: Pakistani': 'Pakistani',
        'Asian, Asian British or Asian Welsh: Other Asian': 'Asian (not Bangladeshi, Chinese, Indian, Pakistani)',
        'Black, Black British, Black Welsh, Caribbean or African: African': 'Black African',
        'Black, Black British, Black Welsh, Caribbean or African: Caribbean': 'Black Caribbean',
        'Black, Black British, Black Welsh, Caribbean or African: Other Black': 'Black (not African or Caribbean)',
        'Mixed or Multiple ethnic groups: White and Asian': 'Mixed White and Asian',
        'Mixed or Multiple ethnic groups: White and Black African': 'Mixed White and Black African',
        'Mixed or Multiple ethnic groups: White and Black Caribbean': 'Mixed White and Black Caribbean',
        'Mixed or Multiple ethnic groups: Other Mixed or Multiple ethnic groups': 'Mixed or Multiple ethnic groups',
        'White: English, Welsh, Scottish, Northern Irish or British': 'White British',
        'White: Irish': 'White Irish',
        'White: Gypsy or Irish Traveller': 'White: Gypsy or Irish Traveller',
        'White: Roma': 'White: Roma',
        'White: Other White': 'White: Other White',
        'Other ethnic group: Arab': 'Arab',
        'Other ethnic group: Any other ethnic group': 'Other ethnic group',
    }

def ethnicity_code_simplified(ethnicity):  
    ethnicity_six_categories = {
        'Does not apply': 'Does not apply',
        'Bangladeshi': 1,
        'Chinese': 1,
        'Indian': 1,
        'Pakistani': 1,
        'Asian (not Bangladeshi, Chinese, Indian, Pakistani)': 1,
        'Black African': 2,
        'Black Caribbean': 2,
        'Black (not African or Caribbean)': 2,
        'Mixed White and Asian': 3,
        'Mixed White and Black African': 3,
        'Mixed White and Black Caribbean': 3,
        'Mixed or Multiple ethnic groups': 3,
        'White British': 4,
        'White Irish': 4,
        'White: Gypsy or Irish Traveller': 5,
        'White: Roma': 5,
        'White: Other White': 5,
        'Arab': 5,
        'Other ethnic group': 5,       
    }   
    
    return ethnicity_six_categories[ethnicity] 

def simplified_employment_code(ethnicity):  
    ethnicity_six_categories = {
        'Does not apply': 'Does not apply',
        'Bangladeshi': 1,
        'Chinese': 1,
        'Indian': 1,
        'Pakistani': 1,
        'Asian (not Bangladeshi, Chinese, Indian, Pakistani)': 1,
        'Black African': 2,
        'Black Caribbean': 2,
        'Black (not African or Caribbean)': 2,
        'Mixed White and Asian': 3,
        'Mixed White and Black African': 3,
        'Mixed White and Black Caribbean': 3,
        'Mixed or Multiple ethnic groups': 3,
        'White British': 4,
        'White Irish': 4,
        'White: Gypsy or Irish Traveller': 5,
        'White: Roma': 5,
        'White: Other White': 5,
        'Arab': 5,
        'Other ethnic group': 5,       
    }   
    
    return ethnicity_six_categories[ethnicity] 