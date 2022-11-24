import pytest, json, jsonpath, requests


###########################################
def test_addNewStudent():
    #Add a new student
    addStudentApi = "https://thetestingworldapi.com/api/Students"
    file = open("C:\\Users\\user\\api\\e2e_session2\\addNewUser.json", "r")
    source_json = file.read()
    request_json = json.loads(source_json)
    response = requests.post(addStudentApi, request_json)
    print(response.status_code)
    print(response.text)
    #add a new skill

    #Add address

    #Fetch compleate details
def test_details():
    apiURL="https://reqres.in/api/users?page=2"
    response= requests.get(apiURL)
    print('statusCode:', response.status_code)
    # response_json=json.loads(response.text)
    response_json= response.json()
    print('===============================')
    print(response_json)
    email= jsonpath.jsonpath(response_json, 'data[2].email')
    print(email[0])
    assert email[0]== 'tobias.funke@reqres.in', "this is the WRONG email address!!!"
    firstUserId12_firstName= jsonpath.jsonpath(response_json, 'data[5].first_name')[0]
    print(firstUserId12_firstName)