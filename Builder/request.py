import requests

base_url = "https://google.com"
response = requests.get(base_url)

print(f"Response Content: {response.content}")