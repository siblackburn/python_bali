import unittest

from Builder.uri_builder import Uri

class TestUri(unittest.TestCase):

    def test_url_set(self):
        test1 = Uri.new().with_scheme("http").with_host("google.com").with_port(8080).with_params("hi", "world").with_fragment("row", "4").to_url()
        output = test1.to_string()

        self.assertEqual("http://google.com:8080/?hi=world#row=4", output, "oops")


unittest.main(argv=[''], verbosity=2, exit=False)