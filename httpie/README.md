Create a command line application where you can specify request parameters from the command line to perform a HTTP request. Use the builder pattern to construct the URL.

Url: `http://demo.codingnomads.co:8080/tasks_api/users`
Example usage: `request.py --scheme http --host demo.codingnomads.co --port 8080 --path /tasks_api/users`

Use the [argparse](https://docs.python.org/3/library/argparse.html) module for parameter parsing.

Print out the response from the server in a nice format.

Let’s model it after: https://httpie.org
Write unit tests for your `URI` class.


## Steps:

1) Extend your URI class to support a port paramter. (The sample API runs on port `8080`)
2) Add requests support to your URI class. You should be able to call `get` on your URI class. This will use the `requests` library to issue a `GET` HTTP call.
3) Make into a command line tool as described above.
4) Bonus: Add support for sending a payload using a `PUT` or a `POST`.


