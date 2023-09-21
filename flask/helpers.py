import __main__ as main
import os

def get_path(path):
    if (not hasattr(main, '__file__')):
        full_path = path
    else:   
        os_path = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(
            os_path, path)
    
    print(full_path)   

    return full_path

def df_to_response(df, app): 
    json_data = df.to_json(orient='records')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response