import requests
from pprint import pprint
from Builder.uri_builder import Uri

class Data_builder():
    def __init__(self, id: int, first_name: str, last_name: str, email: str):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email


    @staticmethod
    def new():
        return Bodybuilder()

    def data_input(self):
        return f'{ "id": {self.__id}, "first_name": {self.__first_name}, "last_name": {self.__last_name}, "email": {self.__email} }'

    @staticmethod
    def put_request(self):
        base_url = Uri.to_string(self)
        body = Data_builder.data_input(self)
        response = requests.put(base_url, json=body)
        return response

class Bodybuilder():
    def __init__(self, id=None, first_name=None, last_name=None, email=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_id(self, id):
        return Bodybuilder(id=id, first_name=self.first_name, last_name=self.last_name, email=self.email)

    def add_firstname(self, first_name):
        return Bodybuilder(id=self.id, first_name=first_name, last_name=self.last_name, email=self.email)

    def add_lastname(self, last_name):
        return Bodybuilder(id=self.id, first_name=self.first_name, last_name=last_name, email=self.email)

    def add_email(self, email):
        return Bodybuilder(id=self.id, first_name=self.first_name, last_name=self.last_name, email=email)

test_put = Uri.new().with_scheme("http").with_host("demo.codingnomads.co").with_port(8080).with_path("/tasks_api/users").to_url()
print(test_put.to_string())


test_data = Data_builder.new().add_id(69).add_firstname("Simons test").add_lastname("Thats right it's blackburn").add_email("siblackburn@Gmail.com")
Data_builder.put_request(test_data)
