# Python `with` keyword

class FileWriter:

    def __init__(self, filename):
        self._filename = filename
        self._f = None

    def write(self, message):
        self._f.write(message)

    def __enter__(self):
        print('creating')
        self._f = open(self._filename, 'w')
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print('cleaning up')
        if self._f:
            self._f.close()


with FileWriter('myfile.txt') as f:
    f.write('message')

