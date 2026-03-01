import requests

def test_bearer_token(endpoint, credentials):

    response = requests.post(endpoint, json=credentials)

    assert response.status_code == 201  # Created
    print(response.json())

    token = response.json().get("token")
    assert token is not None
    
    
    
  
  
  
   


        