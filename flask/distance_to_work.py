import pandas as pd
from helpers import get_path


class Employment: 

    def __init__(self):

        file_name_young = 'data/employment_status_by_basic_demography_young.csv'
        file_name_old = 'data/employment_status_by_basic_demography_old.csv'

        file_path_young = get_path(file_name_young)
        file_path_old = get_path(file_name_old)

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
        self.young_df = young_df.drop('Age (B) (6 categories) Code', axis=1)

        old_df.rename(columns=rename_dict, inplace=True)
        self.old_df = old_df.drop('Age (C) (5 categories) Code', axis=1)


    def add_employment(self, sample_df):  
        sample_df['employment'] = sample_df.apply(self.add_employment_data_to_row, axis=1)
        return sample_df

    def add_employment_data_to_row(self, row):
        return self.sample_employment_by_demography(row['ltla_code'], row['age'], row['ethnicity_code']) 

    def sample_employment_by_demography(self, ltla_code, age, ethnicity_code):


        def age_to_age_category(age):
            if (age <= 4):
                return 'Aged 15 years and under'
            elif (age <= 15):
                return 'Aged 16 to 24 years'
            elif (age <= 20):
                return 'Aged 25 to 34 years'
            elif (age <= 24):
                return 'Aged 35 to 49 years'
            elif (age <= 29):
                return 'Aged 50 to 64 years'
            elif (age > 30):
                return 'Aged 65 years and over'
            else:
                return -1

        age_category = age_to_age_category(age)
      

        query = "age_category== '" + age_category + \
            "'&ethnicity_code== " + str(ethnicity_code) + \
            "&ltla_code== '" + ltla_code + "'"

        if (age < 30):
            distribution_df = self.young_df.query(query)
        else:
            distribution_df = self.old_df.query(query)
        
        if(distribution_df['observation'].sum() == 0): 
            employment_status = 'no data'
        else: 
            sample_df = distribution_df.sample(1, weights='observation')
            employment_status = sample_df['employment_status'].values[0]

        print('***')
        print(employment_status)

        return employment_status

