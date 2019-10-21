import json

with open("CodingNomadstest.txt", "r") as access_json:
    read_content = json.load(access_json)

#data contains several dictionaries
for dicts in read_content:
    print(dicts)

#the dictionary data has all the content we want
cn_data = read_content['data']
print(f'initial data: {cn_data}')

# #within the data dictionary, there's a list, which contains a dictionaries. Can access them by first cycling through dictionaries, then cycling throught he keys in each
dict_list_first_name = []
for dicts in cn_data:
    for k, v in dicts.items():
        if k=="first_name":
            dict_list_first_name.append(v)
print(f'list of dicts {dict_list_first_name}')


dict_list_email = []
for dicts in cn_data:
    for k, v in dicts.items():
        if k=="email":
            dict_list_email.append(v)
print(f'list of dicts {dict_list_email}')
