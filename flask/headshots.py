import os
import re
import pandas as pd
from helpers import get_path



def add_headshots(sample_df):

    def add_ethnicty_image_categories(ethnicity_string):
        if ('black' in ethnicity_string.casefold()):
            ethnicity_image_cat = "black"
        elif ('asian' in ethnicity_string.casefold()):
            ethnicity_image_cat = "asian"
        elif ('chinese' in ethnicity_string.casefold()):
            ethnicity_image_cat = "asian"            
        elif ('indian' in ethnicity_string.casefold()):
            ethnicity_image_cat = "indian"
        elif ('pakistani' in ethnicity_string.casefold()):
            ethnicity_image_cat = "indian"
        elif ('bangladeshi' in ethnicity_string.casefold()):
            ethnicity_image_cat = "indian"                        
        elif ('white' in ethnicity_string.casefold()):
            ethnicity_image_cat = "white"
        else:
            ethnicity_image_cat = "white"
        return ethnicity_image_cat

    sample_df['ethnicity_image_cat'] = sample_df['ethnicity'].apply(
        add_ethnicty_image_categories)

    # create df of images
    path = get_path('headshots/images')
    img_list = os.listdir(path)
    output_list = [re.split('_|\.', i) for i in img_list]

    images_df = pd.DataFrame(output_list)
    images_df.rename(columns={0: 'sex', 1: 'image_age',
                    2: 'image_ethnicity', 3: 'number', 4: 'file_type'}, inplace=True)

    images_df['image_age'] = pd.to_numeric(
        images_df['image_age'], errors='coerce')
    images_df = images_df.dropna(subset=['image_age'])
    images_df['image_age'] = images_df['image_age'].astype(int)

    images_df.sort_values('image_age', inplace=True)
    sample_df.sort_values('age', inplace=True)

    sample_df = pd.merge_asof(sample_df, images_df,
                            left_on='age', right_on='image_age', left_by=['sex', 'ethnicity_image_cat'],
                            right_by=['sex', 'image_ethnicity'], allow_exact_matches=True, direction="nearest")

    sample_df['headshot_file'] = sample_df['sex'].astype(str) + "_" + \
        sample_df['image_age'].astype(str) + "_" + \
        sample_df['ethnicity_image_cat'].astype(str) + "_" + \
        sample_df['number'].astype(str) + "." + \
        sample_df['file_type'].astype(str)
    
    sample_df.drop(columns=['image_age', 'number', 'image_ethnicity',
                'ethnicity_image_cat', 'file_type'], inplace=True)    

    return (sample_df)
