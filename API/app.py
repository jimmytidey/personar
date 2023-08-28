from flask import Flask,json
import pandas as pd
import random

def age_sampler(distribution):
  return random.choices(list(distribution.keys()), weights=distribution.values())[0]

def sample_msoa_age_and_gender(number_of_samples=10, age=all, gender=all):
  # returns [{"MSOA_name": "Stockport 027", "LA_name": : "Stockport", "age": "21", gender: "male" }, ...]
  MSOA_df = pd.read_csv('data/MSOA_age_and_gender/MSOA_age_and_gender.csv')
  MSOA_sample = MSOA_df.sample(n=number_of_samples, weights='All Ages')
  MSOA_sample['age_distribution_dictionary'] = MSOA_sample.iloc[:, 7:98].to_dict('records')
  MSOA_sample.drop(MSOA_sample.columns[7:98], axis=1,inplace=True)
  MSOA_sample['age'] = MSOA_sample['age_distribution_dictionary'].apply(age_sampler)
  MSOA_sample.drop(['age_distribution_dictionary','LA Code (2018 boundaries)','LA name (2018 boundaries)'], axis=1,inplace=True)
  return MSOA_sample

  

def get_MSOA_ethnicity(MSOA_id, no_samples=1):
  MSOA_df = pd.read_csv('data/MSOA_ethnicity/MSOA_ethnicity.csv')
  distribution = MSOA_df.loc[MSOA_df['Middle layer Super Output Areas Code'] == MSOA_id]
  distribution_dict = distribution.set_index('Ethnic group (20 categories)')['Observation'].to_dict()
  sample = random.choices(list(distribution_dict.keys()), weights=distribution_dict.values(), k = no_samples)
  if (no_samples == 1): 
    sample = sample[0]

  return sample
 



app = Flask(__name__)

@app.route('/sample/', methods=['GET', 'POST'])
def sample():
    sample_df = sample_msoa_age_and_gender()
    sample_df['ethniticty'] = sample_df['MSOA Code'].apply(get_MSOA_ethnicity)
    json_data = sample_df.to_json(orient='records')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)





  

