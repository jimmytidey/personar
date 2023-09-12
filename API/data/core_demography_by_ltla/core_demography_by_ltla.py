import pandas as pd
import random
import os

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


# https://www.ons.gov.uk/datasets/RM200/editions/2021/versions/1/filter-outputs/3a155485-7746-4c70-9348-0c8de43d09e6#get-data
# gender - two categories 
# age - nine categories
# ethnicity - 20 cateogies 

def sample_core_demography_by_ltla(sample_size, region):

    if (is_interactive()):
        print('interactive')
        file_path = 'RM032-2021-1-filtered-2023-09-02T13_43_40Z.csv'
    else:
        print('not interactive')
        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(
            path, 'RM032-2021-1-filtered-2023-09-02T13_43_40Z.csv')

    csv_df = pd.read_csv(file_path)

    rename_dict = {'Lower tier local authorities Code': 'ltla_code',
                   'Lower tier local authorities': 'ltla_name',
                   'Age (9 categories)': 'age_category',
                   'Ethnic group (20 categories)': 'ethnicity',
                   'Sex (2 categories)': 'sex',
                   'Observation': 'observation',
                   'Ethnic group (20 categories) Code': 'ethnicity_code'}

    csv_df.rename(columns=rename_dict,
                  inplace=True)

    if (region == 'none'):
        region_df = csv_df
    else:
        region_df = csv_df[csv_df['ltla_code'] == region]

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

    sample_df['sex'] = sample_df['sex'].apply(str.lower)
    
    sample_df.drop(['Age (9 categories) Code', 'Sex (2 categories) Code'], inplace=True, axis=1)
    
    print(sample_df)

    return sample_df

def list_all_ltlas():

    path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(path, 'RM032-2021-1-filtered-2023-09-02T13_43_40Z.csv')
    df = pd.read_csv(file_path)

    list = df.drop_duplicates('Lower tier local authorities Code')

    list = list[['Lower tier local authorities Code',
                 'Lower tier local authorities']]
    
    list.rename(columns={'Lower tier local authorities Code': 'ltla_code',
                 'Lower tier local authorities': 'ltla_name'},inplace=True)

    list.sort_values('ltla_name', inplace=True)

    return list


