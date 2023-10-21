import pandas as pd

from helpers import csv_to_clean_df
from basic_demography import BasicDemography
from employment import Employment


class Disability:

    def __init__(self):
        self.df = csv_to_clean_df(
            'data/disability_by_demography_employment_status.csv')

    def add_disability_status(self, sample_df):
        print('main_df')
       
        sample_df['disability_status'] = sample_df.apply(
            self.sample_disability_by_demography_employment, axis=1)
        return sample_df

    def sample_disability_by_demography_employment(self, row):

        def age_to_age_category(age):
            print(age)
            if (age <= 15):
                return 'Aged 15 years and under'
            elif (age <= 24):
                return 'Aged 16 to 24 years'
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

        age_category = age_to_age_category(row['age'])
        print(age_category)

        query = "age_category== '" + age_category + \
            "'& ethnicity_simplified_code== " + str(row['ethnicity_code_simplified']) + \
            "& ltla_code== '" + row['ltla_code'] + "'" \
            "& employment_status_simplified_code== " + str(row['employment_status_simplified_code']) + \
            "& gender== '" + row['gender'] + "'"

        distribution_df = self.df.query(query)

        if (distribution_df['observation'].sum() == 0):
            disability_status = 'no data'
        else:
            sample_df = distribution_df.sample(1, weights='observation')
            disability_status = sample_df['disability_status'].values[0]

        return disability_status


