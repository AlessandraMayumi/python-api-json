import json
import requests

base_url = 'https://api.covid19api.com'

countries_req = requests.get(base_url + '/countries')
countries_str = countries_req.text
countries_json = json.loads(countries_str)

response_list = []
for country in countries_json:
    country_req = requests.get(base_url + '/country/' + country['Slug'])
    country_str = country_req.text
    if country_req.status_code == 200 and len(country_str) > 10:
        try:
            country_json = json.loads(country_str)
            response_list += country_json
        except:
            pass
response_str = json.dumps(response_list)

filename = 'covid19api.json'
f = open(filename, 'w')
f.write(response_str)
f.close()
