import json, jsonpath, requests
#url for delete action
url= 'https://reqres.in/api/users/2'

response= requests.delete(url) #we should get 204 response code


print('response status code:', response.status_code)
if response.status_code == 204:
    print('response status code is OK...')
else:
    print('status code is WRONG!!!')
