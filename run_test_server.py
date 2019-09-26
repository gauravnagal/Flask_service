from app import flask_app as app
from requests import post, get
import json


def test_server(is_docker: bool=False):
    if is_docker:
        port = 8001
    else:
        port = 8000 # When Using Flask Test Server
    url = f"http://0.0.0.0:{port}"
    # Checking Heartbeat
    print("Checking Heartbeat from System:")
    print("===============================")
    uri = f"{url}/heartbeat"
    resp = get(uri)
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(f"Returned Status Code: {resp.status_code}\nError With Server")

    print("Checking Sum from System:")
    print("===============================")
    uri = f"{url}/sum/1234"
    data = {"x": 10, "y": 12}
    jdump = data#json.dumps(data)
    print(jdump)
    resp = post(
        uri,
        json=data
    )
    
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(f"Returned Status Code: {resp.status_code}\nError With Server")


    print("Checking Minimum from System:")
    print("===============================")
    uri = f"{url}/minimum/1234"
    data = {'values': [1,5,3,2]}
    jdump = json.dumps(data)
    print(jdump)
    resp = post(
        uri,
        json=data
    )
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(f"Returned Status Code: {resp.status_code}\nError With Server")
    
    
    print("Checking Product from System:")
    print("===============================")
    uri = f"{url}/product/1234"
    data = {'values': [1,5,3,2]}
    jdump = json.dumps(data)
    print(jdump)
    resp = post(
        uri,
        json=data
    )
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(f"Returned Status Code: {resp.status_code}\nError With Server")
    
if __name__ == "__main__":
    test_server()