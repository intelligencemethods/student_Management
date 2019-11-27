import requests
url = 'http://127.0.0.1:8000/studentInfo/'
headers = {'Authorization': 'Token 2d01f2935b8f906eab1ce1435f4f51df6d70ec4c'}
r = requests.get(url, headers=headers)