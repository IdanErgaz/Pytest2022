import requests, json, jsonpath

#Read json input from a file
#Parse into json format
#Hit post method
#Parse response into json format
#Validate response

############################################
url= 'https://reqres.in/api/users'

#Read input json file
file= open('C:\\Users\\user\\api\\createUser.json', 'r')
json_input= file.read()
request_json=json.loads(json_input)
print(request_json)
###############################################
#Make Post request with the json input body
response= requests.post(url, request_json )
print(response.content)
####################
#assert response response status code is 201
assert response.status_code ==201
######################

#Fetch header from the response
print('Header:', response.headers)
print(response.headers.get('Content-Length'))


#Parse response to JSON FORMAT
response_json= json.loads(response.text)
print(response_json)

##Pick ID from json path
id= jsonpath.jsonpath(response_json, 'id')
print('id:', id[0])