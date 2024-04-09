import os
from dotenv.main import load_dotenv

load_dotenv()
api_key = os.getenv('upstox_api_key')
secret_key = os.getenv('upstox_secret_key')
redirect_url='http://127.0.0.1:8000/'
# authorization_code = 'qwjXdc'  # This should be obtained dynamically

def get_auth_code():

    Auth_url=f'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={api_key}&redirect_uri={redirect_url}'
    print(Auth_url)
get_auth_code()

# def token():
    

#     url = 'https://api.upstox.com/v2/login/authorization/token'
#     headers = {
#         'accept': 'application/json',
#         'Content-Type': 'application/x-www-form-urlencoded',
#     }

#     data = {
#         'code': authorization_code,
#         'client_id': api_key,
#         'client_secret': secret_key,
#         'redirect_uri': redirect_url,
#         'grant_type': 'authorization_code',
#     }
#     import requests


#     response = requests.post(url, headers=headers, data=data)

#     return response.json()

    

# access_token=token()
# print("access_token :",access_token)