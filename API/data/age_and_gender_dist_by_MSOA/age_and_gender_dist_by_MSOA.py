import pandas as pd
import random
import os

def sample_age_and_gender_dist_by_MSOA(sample_size):
    
    # https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/middlesuperoutputareamidyearpopulationestimates

    def age_sampler(distribution):
        return random.choices(list(distribution.keys()), weights=distribution.values())[0]

    file_path = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(file_path, "sape23dt4mid2020msoasyoaestimatesunformatted.xlsx")

    females_df = pd.read_excel(io=data_path, sheet_name='Mid-2020 Females',skiprows=4)
    males_df = pd.read_excel(io=data_path, sheet_name='Mid-2020 Males',skiprows=4)
    females_df['Gender']='female'
    males_df['Gender']='male'
    combined_df = pd.concat([females_df,males_df], ignore_index=True)
    filtered_by_MSOA_df = combined_df.loc[combined_df['LA name (2021 boundaries)'] == 'Newham']
    sample = filtered_by_MSOA_df.sample(n=sample_size, weights='All Ages')
    sample['age_distribution_dictionary'] = sample.iloc[:, 19:98].to_dict('records')
    sample.drop(sample.columns[7:98], axis=1,inplace=True)
    sample['age'] = sample['age_distribution_dictionary'].apply(age_sampler)
    sample.drop(['age_distribution_dictionary','LA Code (2018 boundaries)','LA name (2018 boundaries)'], axis=1,inplace=True)
    return sample



