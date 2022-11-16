import requests
import json
import jsonpath
# apiUrl
url = 'https://reqres.in/api/users?page=2'

#send get request

response= requests.get(url)
print(response)

#display response content
print(response.content)
print('####################################')

#Display response header
print(response.headers)

#parse response to json format
json_response=json.loads(response.text)
print('json response:', json_response)

#Fetch value using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print('number of pages:', pages[0])
assert pages[0] == 2