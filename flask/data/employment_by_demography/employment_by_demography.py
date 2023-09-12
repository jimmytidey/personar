import pandas as pd
import sys
import os

# RM200-2021-1-filtered-2023-09-04T14_47_55Z
# gender - two categories
# ethnicity - 20 cateogies
# ltla - 258 out of 331
# Aged 4 years and under
# Aged 5 to 15 years
# Aged 16 to 20 years
# Aged 21 to 24 years
# Aged 25 to 29 years
# Aged 30 years and over

# RM200-2021-1-filtered-2023-09-04T14_53_14Z
# gender - two categories
# ethnicity - 20 cateogies
# ltla - 284 out of 331
# Aged 24 years and under
# Aged 25 to 34 years
# Aged 35 to 49 years
# Aged 50 to 64 years
# Aged 65 years and over


def sample_employment_by_demography(ltla_code, age, ethnicity_code):

    file_name_young = 'RM200-2021-1-filtered-2023-09-04T14_47_55Z.csv'
    file_name_old = 'RM200-2021-1-filtered-2023-09-04T14_53_14Z.csv'

    path = os.path.abspath(os.path.dirname(__file__))
    file_path_young = os.path.join(path, file_name_young)
    file_path_old = os.path.join(path, file_name_old)

    young_df = pd.read_csv(file_path_young)
    old_df = pd.read_csv(file_path_old)

    rename_dict = {'Lower tier local authorities Code': 'ltla_code',
                   'Lower tier local authorities': 'ltla_name',
                   'Age (B) (6 categories)': 'age_category',
                   'Age (C) (5 categories)': 'age_category',
                   'Ethnic group (20 categories)': 'ethnicity',
                   'Ethnic group (20 categories) Code': 'ethnicity_code',
                   'Sex (2 categories)': 'gender',
                   'Observation': 'observation',
                   'Ethnic group (20 categories) Code': 'ethnicity_code',
                   'Economic activity status (7 categories)': 'employment_status',
                   'Economic activity status (7 categories) Code': 'employment_status_code'
                   }
    
    young_df.rename(columns=rename_dict, inplace=True)
    young_df.drop('Age (B) (6 categories) Code', inplace=True, axis=1)

    old_df.rename(columns=rename_dict, inplace=True)
    old_df.drop('Age (C) (5 categories) Code', inplace=True, axis=1)

    def age_to_age_category_young(age):
        if (age <= 4):
            return 'Aged 4 years and under'
        elif (age <= 15):
            return 'Aged 5 to 15 years'
        elif (age <= 20):
            return 'Aged 16 to 20 years'
        elif (age <= 24):
            return 'Aged 21 to 24 years'
        elif (age <= 29):
            return 'Aged 25 to 29 years'
        elif (age > 30):
            return 'Aged 30 years and over'
        else:
            return -1

    def age_to_age_category_old(age):
        if (age <= 24):
            return 'Aged 24 years and under'
        elif (age <= 34):
            return 'Aged 25 to 34 years'
        elif (age <= 49):
            return 'Aged 35 to 49 years'
        elif (age <= 64):
            return 'Aged 50 to 64 years'
        elif (age > 65):
            return 'Aged 65 years and over'
        else:
            return -1

    if (age < 30):
        age_category = age_to_age_category_young(age)
    else:
        age_category = age_to_age_category_old(age)

    query = "age_category== '" + age_category + \
        "'&ethnicity_code== " + str(ethnicity_code) + \
        "&ltla_code== '" + ltla_code + "'"

    print(query)

    if (age < 30):
        distribution_df = young_df.query(query)
    else:
        distribution_df = old_df.query(query)
    
    if(distribution_df['observation'].sum() == 0): 
        employment_status = 'no data'
    else: 
        sample_df = distribution_df.sample(1, weights='observation')
        employment_status = sample_df['employment_status'].values[0]

    print('***')
    print(employment_status)

    return employment_status

