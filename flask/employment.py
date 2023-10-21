import pandas as pd
from helpers import csv_to_clean_df


class Employment: 

    def __init__(self):

        self.young_df = csv_to_clean_df(
            'data/employment_status_by_basic_demography_young.csv')
        self.old_df = csv_to_clean_df(
            'data/employment_status_by_basic_demography_old.csv')

    def add_employment(self, sample_df):  
        sample_df['employment'] = sample_df.apply(self.sample_employment_by_demography, axis=1)
        sample_df['employment_status_simplified_code'] = sample_df['employment'].apply(employment_status_simplified_code)
        
        return sample_df

    def sample_employment_by_demography(self, row):

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
            elif (age >= 65):
                return 'Aged 65 years and over'
            else:
                return -1

        if (row['age'] < 30):
            age_category = age_to_age_category_young(row['age'])
        else:
            age_category = age_to_age_category_old(row['age'])

        query = "age_category== '" + age_category + \
            "'&ethnicity_code== " + str(row['ethnicity_code']) + \
            "&ltla_code== '" + row['ltla_code'] + "'"

        if (row['age'] < 30):
            distribution_df = self.young_df.query(query)
        else:
            distribution_df = self.old_df.query(query)
        
        if(distribution_df['observation'].sum() == 0): 
            employment_status = 'no data'
        else: 
            sample_df = distribution_df.sample(1, weights='observation')
            employment_status = sample_df['employment_status'].values[0]
            employment_status_code = sample_df['employment_status_code'].values[0]
        employment_status = employment_status_translation(employment_status)

        return employment_status


def employment_status_translation(status):
    dict = { 
        'Economically active (excluding full-time students): In employment': 'Employed',
        'Economically active: Unemployed (including full-time students)': 'Student looking for a job',
        'Economically active (excluding full-time students): Unemployed: Seeking work or waiting to start a job already obtained: Available to start working within 2 weeks': 'Seeking work',
        'Economically active and a full-time student: In employment': 'Student with a job',
        'Economically inactive (excluding full-time students)': 'Not seeking work',
        'Economically inactive and a full-time student': 'Student',
        'Does not apply': 'Does not apply',
        'no data': 'no data'
    } 

    return dict[status]

def employment_status_simplified_code(status):
    dict = { 
        'Employed': 1,
        'Student looking for a job': 1,
        'Seeking work': 2,
        'Student with a job': 1,
        'Not seeking work': 3,
        'Student': 1,
        'Does not apply': -8,
        'no data': -8
    } 

    return dict[status]

    