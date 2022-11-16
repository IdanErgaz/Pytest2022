import requests, json, jsonpath, pytest
# pip install requests
#pip install -U requests
#pip install -U jsonpath

def test_getUsers():
    url = "https://reqres.in/api/users?page=2"
    #send get request
    response= requests.get(url)
    #print response content
    print('################## Response Content #################################')
    print()
    print(response.content)
    print()
    print('################## Response Text #################################')
    print()
    print(response.text)
    print()
    print('################## Response Header #################################')
    print(response.headers)
    assert response.status_code == 200
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    json_response= json.loads(response.text)
    print(json_response)
    total_pages=jsonpath.jsonpath(json_response, 'total_pages')
    print(total_pages[0])
    assert total_pages[0] ==2
    firstName= jsonpath.jsonpath(json_response, 'data[0].first_name')
    print(firstName)
    assert firstName[0] == 'Michael'
    print(jsonpath.jsonpath(json_response, 'data[3].first_name'))
    #print all first names
    for i in range(0,3):
        firstN= (jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name'))
        print(firstN[0])

def test_deleteUser():
    url="https://reqres.in/api/users/2"
    response= requests.delete(url)
    if response.status_code == 204:
        print('status code for deletion is OK...')
        assert True
    else:
        print('The error status code is wrong!')
        assert False

def test_post():
    #create a new user
    api_createUser= 'https://reqres.in/api/users'
    fileInput= open("C:\\Users\\user\\api\\createUser.json")
    json_input= fileInput.read()
    requests_json= json.loads(json_input)
    print(requests_json)
    #make a post request
    response= requests.post(api_createUser, requests_json)
    print(response.text, response.status_code)
    assert response.status_code == 201
    #fetch header from the response
    print('********************')
    print(response.headers)
    print(response.headers.get('Content-Length'))

#parse response to json format
    responseJson=json.loads(response.text)
    print(responseJson)
    id= (jsonpath.jsonpath(responseJson, 'id'))[0]
    print('id: ', id)

def test_updateUser():
    api_updateUser="https://reqres.in/api/users/2"
    source=open("C:\\Users\\user\\api\\updateUser.json", "r")
    file=source.read()
    #parse source int json format
    sourceJson= json.loads(file)
    putResponse=requests.put(api_updateUser, sourceJson)
    print(putResponse.text)
    assert putResponse.status_code==200
    responseJson= json.loads(putResponse.text)
    job= jsonpath.jsonpath(responseJson, 'job')
    print(job[0])
    assert job[0] =='TL'