import pandas as pd
import random
from helpers import get_path

class BasicDemography: 

    def __init__(self):
        csv_path =  get_path('data/basic_demography_ltla_level.csv')
        self.csv_df = pd.read_csv(csv_path)
        rename_dict = {'Lower tier local authorities Code': 'ltla_code',
                    'Lower tier local authorities': 'ltla_name',
                    'Age (9 categories)': 'age_category',
                    'Ethnic group (20 categories)': 'ethnicity',
                    'Sex (2 categories)': 'sex',
                    'Observation': 'observation',
                    'Ethnic group (20 categories) Code': 'ethnicity_code'}

        self.csv_df.rename(columns=rename_dict,
                    inplace=True)    
        
        self.csv_df['sex'] = self.csv_df['sex'].apply(str.lower)
        self.csv_df.drop(['Age (9 categories) Code', 'Sex (2 categories) Code'], inplace=True, axis=1)

    def sample (self, sample_size, region):

        if (region == 'none'):
            region_df = self.csv_df
        else:
            region_df = self.csv_df[self.csv_df['ltla_code'] == region]

        def age_category_to_age(age_category):
            if (age_category == 'Aged 4 years and under'):
                return random.randrange(0, 4)
            elif (age_category == 'Aged 5 to 9 years'):
                return random.randrange(5, 9)
            elif (age_category == 'Aged 10 to 15 years'):
                return random.randrange(10, 15)
            elif (age_category == 'Aged 16 to 24 years'):
                return random.randrange(16, 24)
            elif (age_category == 'Aged 25 to 34 years'):
                return random.randrange(25, 34)
            elif (age_category == 'Aged 35 to 49 years'):
                return random.randrange(35, 49)
            elif (age_category == 'Aged 50 to 64 years'):
                return random.randrange(50, 64)
            elif (age_category == 'Aged 65 to 74 years'):
                return random.randrange(65, 74)
            elif (age_category == 'Aged 75 years and over'):
                return random.randrange(75, 90)
            else:
                return -1

        region_df['age'] = region_df['age_category'].apply(age_category_to_age)     
        region_df = region_df[(region_df['age'] > 16)]
        sample_df = region_df.sample(n=sample_size, weights='observation')

        return sample_df

    def list_all_ltlas(self):
             
        list = self.csv_df.drop_duplicates('ltla_code')
        list = list[['ltla_code','ltla_name']]
        list.sort_values('ltla_name', inplace=True)

        return list


