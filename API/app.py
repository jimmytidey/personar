from flask import Flask,json, send_file,request,make_response
import pandas as pd
import random
import os
from data.age_and_gender_dist_by_MSOA.sample_age_and_gender_dist_by_MSOA import sample_age_and_gender_dist_by_MSOA


def get_MSOA_ethnicity(MSOA_id, no_samples=1):
  MSOA_df = pd.read_csv('data/MSOA_ethnicity/MSOA_ethnicity.csv')
  distribution = MSOA_df.loc[MSOA_df['Middle layer Super Output Areas Code'] == MSOA_id]
  distribution_dict = distribution.set_index('Ethnic group (20 categories)')['Observation'].to_dict()
  sample = random.choices(list(distribution_dict.keys()), weights=distribution_dict.values(), k = no_samples)
  if (no_samples == 1): 
    sample = sample[0]

  return sample
 

def random_image(age, gender, ethnicity):
    """
    Return a random image from the ones in the static/ directory
    """

    if (ethnicity=='white'):
      ethnicity_prefix_string = "white"
    elif (ethnicity=='black'):
      ethnicity_prefix_string = "black"  
    elif (ethnicity=='asian'):
      ethnicity_prefix_string = "asian"
    elif (ethnicity=='indian'):
      ethnicity_prefix_string = "indian"      
    else:
      ethnicity_prefix_string = "white"        

    prefix_string = gender+ "_" + age + "_"+ ethnicity_prefix_string
    print('prefix_string')
    print(prefix_string)

    img_dir = "./tpdne"
    img_list = os.listdir(img_dir)
    img_path = [filename for filename in os.listdir(img_dir) if filename.startswith(prefix_string)]
    age_search_radius = 1
    while len(img_path) == 0:
      age_search = str(int(age) + age_search_radius)
      prefix_string = gender+ "_" + age_search + "_"+ ethnicity_prefix_string
      older_img_path = [filename for filename in os.listdir(img_dir) if filename.startswith(prefix_string)]

      age_search = str(int(age) - age_search_radius)
      prefix_string = gender+ "_" + age_search + "_"+ ethnicity_prefix_string
      younger_img_path = [filename for filename in os.listdir(img_dir) if filename.startswith(prefix_string)]      
      
      img_path =older_img_path+ younger_img_path

      age_search_radius +=1
      
    img_sample = os.path.join(img_dir, random.choices(img_path)[0])
    print("---") 
    print(img_sample)
    return img_sample


app = Flask(__name__)

@app.route('/sample/', methods=['GET'])
def sample():
    sample_df = sample_age_and_gender_dist_by_MSOA(10)
    sample_df['ethniticty'] = sample_df['MSOA Code'].apply(get_MSOA_ethnicity)
    sample_df.columns = sample_df.columns.str.replace(' ', '')
    sample_df.columns = sample_df.columns.str.replace('(2021boundaries)', '')
   
    json_data = sample_df.to_json(orient='records')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/image/headshot.jpg', methods=['GET'])
def image():
  args = request.args
  print(args.get('age'))
  image = random_image(args.get('age'), args.get('gender'), args.get('ethnicity'))
  response = make_response(send_file(image, mimetype='image/png'))
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

  return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)





  

