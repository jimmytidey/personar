from flask import Flask,json, send_file,request,make_response, send_from_directory
from flask_cors import CORS, cross_origin
import pandas as pd
import random
import os
from data.core_demography_by_ltla.core_demography_by_ltla import sample_core_demography_by_ltla, list_all_ltlas
from data.employment_by_demography.employment_by_demography import sample_employment_by_demography
from headshots.get_headshot_urls import get_headshot_urls

app = Flask(__name__)
CORS(app,resources={r"/sample/": {"origins": "*"}})

def DfToResponse(df): 
    json_data = df.to_json(orient='records')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/data/sample/', methods=['GET'])
def sample():
    region = request.args.get('region')
    sample_df = sample_core_demography_by_ltla(10, region)

    def add_employment_data(row):
        return sample_employment_by_demography(row['ltla_code'], row['age'], row['ethnicity_code'])

    sample_df['employment'] = sample_df.apply(add_employment_data, axis=1)
    sample_df = get_headshot_urls(sample_df)

    response = DfToResponse(sample_df)
    return response

@app.route('/data/list_ltlas/', methods=['GET'])
def list_ltlas():
    result_df = list_all_ltlas()
    response = DfToResponse(result_df)
    return response

@app.route('/headshots/<path:path>')
def serve_headshots(path):
    return send_from_directory('headshots', path)

@app.route('/',  methods=['GET'])
def serve_app():
    return send_from_directory('app', 'index.html')

@app.route('/assets/<path:path>',  methods=['GET'])
def serve_app_assets(path):
    return send_from_directory('app/assets', path)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)








  

