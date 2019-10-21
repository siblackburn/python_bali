class URL:
    @staticmethod
    def new():
        return URLBuilder

    def __init__(self, scheme: str, host: str, path: str):

    def to_string(self):
        return f'{self.scheme}//{self.host}//{self.path}'

class URLBuilder:
    def __init__(self, scheme: str=None, host: str=None, path: str=None):
        self.scheme = scheme
        self.host = host
        self.path = path

    def with_scheme(self, scheme):
        return URLBuilder(scheme=scheme, host=self.host, path=self.path)

    def with_host(self, scheme):
        return URLBuilder(scheme=scheme, host=self.host, path=self.path)

    def with_path(self, scheme):
        return URLBuilder(scheme=scheme, host=self.host, path=self.path)

    def with_to_url(self, scheme):
        return URLBuilder(scheme=scheme, host=self.host, path=self.path)

builder = URL.new()
builder = builder.with_scheme("http")
u = builder.to_url()
print(u.to_string())


#build url cuilder
# add support for query parameters
# add support for URL fragments