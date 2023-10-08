import pandas as pd
import random
from helpers import get_path
from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


class BasicDemography:

    def __init__(self):
        csv_path = get_path('data/basic_demography_ltla_level.csv')
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
        self.csv_df.replace(
            {"ethnicity": ethnicity_lables_translation}, inplace=True)

    def get_region_averages(self, region):
        region_df = self.csv_df[self.csv_df['ltla_code'] == region]
        population_total = region_df['observation'].sum()

        # calculate ethnicity propotions
        population_by_ethnicity = region_df[[
            'ethnicity', 'observation']].groupby(
            'ethnicity').sum()
        population_by_ethnicity['observation'] = population_by_ethnicity['observation'] / population_total
        population_by_ethnicity = population_by_ethnicity.round(3)

        # calculate age propotions
        population_by_age = region_df[[
            'age_category', 'observation']].groupby(
            'age_category').sum()
        population_by_age['observation'] = population_by_age['observation'] / \
            population_total
        population_by_age = population_by_age.round(3)

    def get_demographic_average(self, row):
        region_df = self.csv_df[self.csv_df['ltla_code'] == row['ltla_code']]
        population_total = region_df['observation'].sum()

        query = "age_category == '" + row['age_category'] + \
            "' & ethnicity_code == " + str(row['ethnicity_code']) + \
            " & sex == '" + row['sex'] + \
            "' & ltla_code == '" + row['ltla_code'] + "'"

        demographic_df = region_df.query(query)

        percentage = round(
            demographic_df['observation'].values[0] / population_total, 2) * 100

        return percentage

    def sample(self, sample_size, region):

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
                # this could be a lot nicer...
                return random.randrange(75, 90)
            else:
                return -1

        region_df['age'] = region_df['age_category'].apply(age_category_to_age)
        region_df = region_df[(region_df['age'] > 16)]
        sample_df = region_df.sample(n=sample_size, weights='observation')

        sample_df['notes'] = sample_df.apply(
            self.get_demographic_average, axis=1)

        return sample_df

    def list_all_ltlas(self):

        list = self.csv_df.drop_duplicates('ltla_code')
        list = list[['ltla_code', 'ltla_name']]
        list.sort_values('ltla_name', inplace=True)

        return list


basic_demography = BasicDemography()
basic_demography.sample(10, 'E06000001')