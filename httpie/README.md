Create a command line application where you can specify request parameters from the command line to perform a HTTP request. Use the builder pattern to construct the URL.

Example usage: `request.py --scheme http --host hostname --port 80 --path /some/api --param param1=val1`

Print out the response from the server in a nice format.

Let’s model it after: https://httpie.org
Write unit tests for your `URI` class.

Bonus: Add support for sending a payload using a `PUT` or a `POST`.


