import json

people_string = '''
{

    "people":[
        {
         "name":"John Smith",
         "phone":"0911-111-111",
         "email":["a@gmail.com", "b@yahoo.com"],
         "has_license":false
        }
         ,
        {
         "name":"Jane Dave",
         "phone":"0911-222-222",
         "email": null,
         "has_license":true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)

print(type(data))
print(data.get("people")[0].get("name"))

for person in data["people"]:
    print(person["name"])
    del person["phone"]

new_string = json.dumps(data, indent = 2)

print(new_string)

new_data = json.loads(new_string)

print(new_data)

with open("states.json") as f:
    info = json.load(f)

for state in info["states"]:
    print(state)
#######################################
from urllib.request import urlopen

#with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
with urlopen("https://openexchangerates.org/api/currencies.json") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent =2))




