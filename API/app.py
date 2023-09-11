from flask import Flask,json, send_file,request,make_response
from flask_cors import CORS, cross_origin
import pandas as pd
import random
import os
from data.core_demography_by_ltla.core_demography_by_ltla import sample_core_demography_by_ltla, list_all_ltlas
from data.employment_by_demography.employment_by_demography import sample_employment_by_demography
from data.headshots.get_headshot_urls import get_headshot_urls
 


app = Flask(__name__)
CORS(app,resources={r"/sample/": {"origins": "*"}})

@app.route('/sample/', methods=['GET'])

def sample():
    sample_df = sample_core_demography_by_ltla(10)
    print(sample_df)
    def add_employment_data(row):
        return sample_employment_by_demography(row['ltla_code'], row['age'], row['ethnicity_code'])

    sample_df['employment'] = sample_df.apply(add_employment_data, axis=1)
    sample_df = get_headshot_urls(sample_df)

    json_data = sample_df.to_json(orient='records')
    print(json_data)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/list_ltlas/', methods=['GET'])
def list_ltlas():
    result = list_all_ltlas()
 
    json_data = result.to_json(orient='records')
    print(json_data)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)





  

