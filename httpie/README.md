Create a command line application where you can specify request parameters from the command line to perform a HTTP request. Use the builder pattern to construct the URL.

Url: `https://reqres.in/api/users?page=2`
Example usage: `request.py --scheme https --host reqres.in --path /api/users/ --params page=2`

Use the [argparse](https://docs.python.org/3/library/argparse.html) module for parameter parsing.

Print out the response from the server in a nice format.

Let’s model it after: https://httpie.org
Write unit tests for your `URI` class.

Bonus: Add support for sending a payload using a `PUT` or a `POST`.


