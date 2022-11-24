import requests, json, jsonpath
import pytest, time
###########################
url= "https://reqres.in/api/users"
def test_createNewUser():
    #read file from json file
    file= open("C:\\Users\\user\\api\\createUser.json", "r")
    json_input= file.read()
    request_json = json.loads(json_input)

    #make a post
    response= requests.post(url, request_json)

    #Validate response code
    assert response.status_code== 201

    #Fetch header from the response
    print(response.headers.get('Content-Length'))

    #Parse the response to json format
    response_json= json.loads(response.text)

    #pick the ID of the new user
    id = jsonpath.jsonpath(response_json, 'id')
    print('id:', id[0])

def test_createOtherUser():
    #read file from json file
    file= open("C:\\Users\\user\\api\\createUser.json", "r")
    json_input= file.read()
    request_json = json.loads(json_input)

    #make a post
    response= requests.post(url, request_json)

    #Validate response code
    assert response.status_code== 201

    #Fetch header from the response
    print(response.headers.get('Content-Length'))

    #Parse the response to json format
    response_json= json.loads(response.text)

    #pick the ID of the new user
    id = jsonpath.jsonpath(response_json, 'id')
    print('id:', id[0])