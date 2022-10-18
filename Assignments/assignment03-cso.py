import requests
import json
import os

dirname = os.path.dirname(__file__)
write_path = os.path.join(dirname, 'cso.json')

url_beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end = "/JSON-stat/2.0/en"

def get_response(dataset):   
    url = url_beginning + dataset + url_end
    response = requests.get(url)
    return response.json()           

def write_data_as_file(dataset):
    with open(write_path, "wt") as fp:
        resp = get_response(dataset)    # store response
        json.dump(resp, fp)             # write response as JSON formatted data into a .json file

if __name__ == "__main__":
    write_data_as_file("FIQ02")