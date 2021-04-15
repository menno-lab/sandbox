import requests

nextUrl = ""
headers = {"Accept": "application/json"}

while True:
    response = requests.get('http://fasttrack.herokuapp.com/' + nextUrl, headers=headers).json()
    if "next" in response.keys():
        nextUrl = response["next"]
    else:
        nextUrl = response
    print(response)
