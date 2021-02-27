import requests

response = requests.get('http://www.argos.co.uk/product/8349024')
print(response.status_code)
