import requests
response = requests.get("https://api.github.com/users/naveenkrnl")
print(response.status_code)
print(response.content)