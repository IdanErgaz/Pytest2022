import requests, json, jsonpath
#response should be 200 error code
url= 'https://reqres.in/api/users/2'

#Read input file
file= open("C:\\Users\\user\\api\\updateUser.json", 'r')
json_input=file.read()
requstJson= json.loads(json_input)

#make a PUT request
response= requests.put(url, requstJson)

##assertion of the status code response

assert response.status_code ==200

print(response.content)

#Parse response content
response_json= json.loads(response.text)
print(response_json)
updatedAt= jsonpath.jsonpath(response_json, 'updatedAt')
print('updatedAt:', updatedAt[0])