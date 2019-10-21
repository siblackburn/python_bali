# Step 1: Complete a Builder class for the Uri class
# Step 2: Add support for query paramters
# Step 3: Add support for URI fragment identifiers (https://en.wikipedia.org/wiki/Fragment_identifier)
# Step 4: Ensure nobody can use the URI constructor,
#         they should only be able to use the Builder to create a URI

from typing import Dict
import re

class Uri():
    def __init__(self, scheme: str, host: str, path: str, params: dict, fragment_identifier: dict):
        self.__scheme = scheme
        self.__host = host
        self.__path = path
        self.__params = params
        self.__fragment_identifier = fragment_identifier

    @staticmethod
    def new():
        return URIbuilder()

    def to_string(self):
        parameter_string = '&'.join([f'{k}={v}' for k, v in self.__params.items()])
        if len(parameter_string) > 0:
            parameter_string = '?' + parameter_string

        fragment_string = '&'.join([f'{k}={v}' for k, v in self.__fragment_identifier.items()])
        if len(fragment_string) > 0:
            fragment_string = '#' + fragment_string

        return f'{self.__scheme}://{self.__host}/{self.__path or ""}{parameter_string or ""}{fragment_string or ""}'


class URIbuilder():

    def __init__(self, scheme="https", host=None, path=None, params={}, fragment_identifier={}):
        self.scheme = scheme
        self.host = host
        self.path = path
        self.params = params
        self.fragment_identifier = fragment_identifier

    def with_scheme(self, scheme):
        return URIbuilder(scheme, host=self.host, path=self.path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_host(self, host):
        return URIbuilder(scheme=self.scheme, host=host, path=self.path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_path(self, path):
        return URIbuilder(scheme=self.scheme, host=self.host, path=path, params=self.params, fragment_identifier=self.fragment_identifier)

    def with_params(self, key, value):
        new_params = dict(self.params, **{key: value})
        return URIbuilder(scheme=self.scheme, host=self.host, path=self.path, params=new_params, fragment_identifier=self.fragment_identifier)

    def with_fragment(self, key, value):
        fragment = dict(self.fragment_identifier, **{key: value})
        return URIbuilder(scheme=self.scheme, host=self.host, path=self.path, params=self.params, fragment_identifier=fragment)

    def to_url(self):
        return Uri(self.scheme, self.host, self.path, self.params, self.fragment_identifier)


test = Uri.new().with_scheme("http").with_host("facebook.com").with_params("hi", "world").with_fragment("row", "4").to_url()

print(test.to_string())

private_test = Uri("http", "www,facebook.com", None, None, None)

print(private_test.to_string())

