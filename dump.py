import requests 
import sys

url = sys.argv[-1]


var = {
    'twitter': 'https://twitter.com/ProfAvery',
    'github': 'https://github.com/ProfAvery',
    'cpsc4493': 'https://sites.google.com/view/cpsc449'
    }
test = requests.post(url, json=var)

if test.status_code != 200:
    print('something went wrong')
else:
    resp = requests.get(url)

    temp = resp.json()
    values = temp.values()

    for x in values:
        for i in x:
            foo = requests.get(url+ str(i))
            print(foo.json())