import json
import requests

NYT_API_KEY = 'Y4FXGPerVU07dTdIkFGZ65C72K2KAJHh'

query = 'election'
url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={NYT_API_KEY}'

response = requests.get(url)



print(json.dumps(response.json(), indent=1))