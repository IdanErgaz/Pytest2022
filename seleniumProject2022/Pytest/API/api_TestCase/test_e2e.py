import json, jsonpath, requests, pytest
def test_e2e():
    # add new student
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f= open("C:\\Users\\user\\api\\e2e_test\\addUser.json", "r")
    json_input= f.read()
    json_request=json.loads(json_input)
    response= requests.post(url, json_request)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), "id")
    print(id[0])

    #add technical skill
    urlTechnicalSkils= "https://thetestingworldapi.com/api/technicalskills"
    f= open("C:\\Users\\user\\api\\e2e_test\\addTechSkill.json", "r")
    jsonInput= f.read()
    request_json= json.loads(jsonInput)
    request_json['id']= int(id[0])
    request_json['st_id']=id[0]
    response= requests.post(urlTechnicalSkils, request_json)
    print(response.text)

    #add address
    api_address= "https://thetestingworldapi.com/api/addresses"
    f= open("C:\\Users\\user\\api\\e2e_test\\add_adress.json", "r")
    json_input= f.read()
    request_json= json.loads(json_input)
    request_json['id'] = id[0]
    request_json['st_id'] = id[0]
    response= requests.post(api_address, request_json)
    print('withAdress', response.content)

    #fetch complete details
    finalDetails_api= "https://thetestingworldapi.com/api/FinalStudentDetails/+id[0]"
    response= requests.get(finalDetails_api)
    print(response.text)

