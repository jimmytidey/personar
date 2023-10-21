import pandas as pd
from helpers import get_path


class DistanceToWork: 

    def __init__(self):

        file_name = 'data/distance_to_work_by_occupation_ethnicity.csv'

        file_path = get_path(file_name)

        df = pd.read_csv(file_path)
       
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
        
        df.rename(columns=rename_dict, inplace=True)
        self.df = df.drop('Age (B) (6 categories) Code', axis=1)

    def add_distance_to_work(self, sample_df):  
        sample_df['employment'] = sample_df.apply(self.add_employment_data_to_row, axis=1)
        return sample_df

    def add_distance_to_work_to_row(self, row):
        return self.sample_employment_by_demography(row['ltla_code'], row['age'], row['gender'], row['ethnicity_code'], row['employment']) 

    def sample_distance_to_work(self, ltla_code, age, gender, ethnicity_code, employment):

        if employment not in ['Economically active (excluding full-time students): In employment','Economically active and a full-time student: In employment']:
            return 'Does not apply' 

        def age_to_age_category(age):
            if (age <= 15):
                return 'Aged 15 years and under'
            elif (age <= 24):
                return 'Aged 16 to 24 years'
            elif (age <= 34):
                return 'Aged 25 to 34 years'
            elif (age <= 49:
                return 'Aged 35 to 49 years'
            elif (age <= 64):
                return 'Aged 50 to 64 years'
            elif (age > 65):
                return 'Aged 65 years and over'
            else:
                return -1

        age_category = age_to_age_category(age)
      

        query = "age_category== '" + age_category + \
            "'&ethnicity_code== " + str(ethnicity_code) + \
            "&ltla_code== '" + ltla_code + "'" \
            "&gender== '" + gender + "'"

    
            distribution_df = self.df.query(query)

        if(distribution_df['observation'].sum() == 0): 
            distance_to_work = 'no data'
        else: 
            sample_df = distribution_df.sample(1, weights='observation')
            distance_to_work = sample_df['employment_status'].values[0]

     

        return distance_to_work

