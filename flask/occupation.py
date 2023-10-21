import pandas as pd
from helpers import csv_to_clean_df
from basic_demography import BasicDemography


class Occupation:

    def __init__(self):
        self.df = csv_to_clean_df('data/occupation_by_age_ethnicity.csv')

    def add_occupation(self, sample_df):
        sample_df['occupation'] = sample_df.apply(
            self.sample_occupation_by_demography, axis=1)
        return sample_df

    def sample_occupation_by_demography(self, row):
      
        if row['employment'] not in ['Employed','Student with a job']:
            return 'Does not apply' 

        def age_to_age_category(age):
            if (age <= 15):
                return 'Aged 15 years and under'
            elif (age <= 24):
                return 'Aged 16 to 24 years'
            elif (age <= 34):
                return 'Aged 25 to 34 years'
            elif (age <= 49):
                return 'Aged 35 to 49 years'
            elif (age > 50):
                return 'Aged 50 years and over'
            else:
                return -1
            
        age_category = age_to_age_category(row['age'])     

        query = "age_category=='" + age_category + "'" \
            + " & ethnicity_code==" + str(row['ethnicity_code']) \
            + " & ltla_code=='" + row['ltla_code'] + "'" \
            + " & occupation!='Does not apply'"
        
        print('*****************************')
        print(query)
         
        distribution_df = self.df.query(query)

        if (distribution_df['observation'].sum() == 0):
            occupation = 'no data'
        else:
            sample_df = distribution_df.sample(1, weights='observation')
            occupation = sample_df['occupation'].values[0]

        return occupation