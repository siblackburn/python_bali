Calculator
==========

# Intro

Write a calculator that operates in prefix notation. Learn more about prefix/Polish notation: https://en.wikipedia.org/wiki/Polish_notation


# Warm-up:

Write a function that validates matching parenthesis in a prefix notation formula.

Valid:

`(+ 1 2)`

Invalid:
`(+ 1 2)(`

In general, we are trying to validate that each open parenthesis, should have a corresponding closed parenthesis. hint: use a stack.



# Main challenge:

Write a calculator that works like the examples below:

```
>> (+ 1 2)
3

>> (* (+ 1 2) 2)
6

>> (sqrt 16)
4
```

# Features:

- Support for common operations: +, -, *, /, modulo, sqrt (square root), pow (raising to power)
- Fully unit tested (run a coverage report: https://coverage.readthedocs.io/en/v4.5.x/)
- Interactive REPL interface (think IPython, Bash, etc)



## Bonus:
- Support for defining variables

```
>> (def my_variable 100)
>> (* my_variable 2)
200
```

