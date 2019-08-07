import requests
import json

data = requests.get('https://interns.bcgdvsydney.com/api/v1/key', verify=False).json()
print(data)
payload = {"name":"Niravit Theng", "email":"niravit.theng@gmail.com"}
response = requests.post('https://interns.bcgdvsydney.com/api/v1/submit?apiKey='+data['key']
, data=json.dumps(payload))
print(response.status_code)