import json
import csv
from Builder.uri_builder import Uri

test2 = Uri.new().with_scheme("http").with_host("demo.codingnomads.co").with_port(8080).with_path("/tasks_api/users").to_url()
# print(test2.to_string())

output = Uri.get_request(test2)
# print(output)

with open('CodingNomadstestwrite.txt', 'w', encoding='utf-8') as data_file:
    data_file.write(str(output))







