Day 1: Baseline Quiz
====

## Intro

Some of the questions below are short-answer questions, others require some coding. Some of the short-answer questions may require you to write some code to explain yourself.

Please take your time with this quiz, there is no rush. While we generally strongly encourage you to use Google to answers questions on a very regular basis, please do your best to complete this quiz without any external assistance from Google or from the CodingNomads online platform.

When you have finished, or gotten as far as you can, please email your quiz to yurigorokhov@gmail.com and ryan@codingnomads.co. After everyone has completed the quiz and emailed their results to Yuri and Ryan we will discuss the quiz as a class.

## Git & GitHub

- What is Git? Git is a version control system that allows us to keep track of changes to our code and revert back to previous versions if needed
- What is GitHub? Github is the most popular online Git repository
- Please list all the Git commands you can think of, and explain what each of the commands does.
git init [project x] - initialises a git in the folder you're currently in. Allows you to begin tracking changes to things within that folder
git add [file x] - adds file to your git. This is needed to include files in the project, even if they are in the same folder
git commit -m "my new comments here" - commits the changes to a new version
git push - pushes the commit to your repository
git remote - checks where your git is pointing to. If it says origin it's pointing to your git
git remote -v - checks the github url your project is being saved to


- What is the general git workflow for a developer on a day-to-day basis?
1) Ensure Git is running
2) Work on project
3) Commit changes
4) Push changes

- Is it important to push your work to GitHub every day?
If you've made changes you need to keep.....yes!!! Otherwise the changes will only be saved on your local system, which therefore might be lost.
Also - if you're working in a team, you will need to keep your team up to date with your developments

## Python Basics

- Name 5 python keywords.
1) if
2) def
3) int
4) Class
5) else

- Describe the difference between a `statement` and an `expression`. Provide an example of each.
A statement is a line of code that performs an action, whereas an expression is code that evaluates to a value, and can be combined with multiple lines of code

- Name the primitive python datatypes (as many as you can think of), and provide a declaration of each.
1) Integer
2) Float
3) String
4) Boolean
5) Class

- Convert a floating point to an integer
int(floating_point)

- Name some complex python data structures. Specify why and when you would use these.
#I looked this up....sorry!!
1) Lists - what it says on the tin! contains a mutable list of data of any type
2) Tuples - an immutable list. Used when you don't want the data to change
3) Sets - an unordered collection of data, with no duplicates. Could use this when you need each data point to be a unique value
4) Dictionaries - a list of key: value pairs, where each key is unique and has a value assigned to it. Used when you want to associate a key with a value (or vice versa)

- Write a `for` loop and a `while` loop
    - When would you prefer one over the other?

for i in range(10):
    print(i)

While i <=100:
    print(i)

While loops are used for times we need to keep running the segment of code until a condition is met. For example, if we're asking the user to input a certain datatype, but they don't enter the information correctly
Whereas for loops are used to iterate through items in a list/dictionary/set etc

## Functions
- What is a function? Define a simple function. (One that adds two numbers for example)
A function is a set of code that performs a task and returns and outcome

def add_numbers(a, b):
    c = a + b
    return c

- When a variable is declared inside a function, what scope does it have?
The scope is within the function (and within the level of indentation it sits at)

- Describe variable shadowing and how it applies to functions (use code to explain yourself if appropriate)
- What are first class functions? Provide a code example of first class functions being used.
- What does the return keyword do
The return keyword allows us to return something out of the function to be used elsewhere.
e.g. in the example above - we can then call c to print, assign to a variable etc.
- [Optional] - What is pass by reference vs pass by value? When would you use one over the other?

## OOP
- What is object oriented programing. Why use it?
Languages where everything is an object (for example Python!!!).

- What is the difference between a function and a method?
- Write and use a simple class that contains: a constructor, an instance variable, an instance method.

Class my_class()

def __init__(self, variable_X, variable_y):
    self.variable_x = variable_x
    self.variable_y = variable_y
    addition = variable_x + variable_y

def __str__(self, variable_x, variable_y):
    print(f'The sum of {self.variable_x} and {self.variable_y} is {addition})


- Describe inheritance. Why use it?
Inheritance is where variables are passed to other methods. This can be used so:
a) We don't have to repeat the same code
b) So making changes is easier (we only make changes to one input rather than more)

- What does is to mean to "override" a function?
# Looked this up!!
Overriding is the ability to change the implementation of a method made by it's ancestors.
The child class can get passed a method from the parent class and then perform some additional functionality/change the functionality

- What is `self`
Self is the variable we define when creating a method that allows us to pass variables. This allows inheritance.

- What is polymorphism?
# Looked this up!!
Polymorphism means that different data types respond to the same function
e.g. __Add__ function would evaluate 1+2 as well as "one" + "two"

## Error handling
- Unfortunately programs do not always run perfectly. What type of errors might occur in a program?
ValueError
TypeError
SyntaxError
Out of range


- How does python handle reporting and handling of these errors?
Not sure what this means....
Python tells us in the terminal/console what type of error we've encountered, what line the code has broken on, and might also provide us with an error code
Very useful!

- [Optional] what are other ways to handle errors?
Through exceptions testing: where we define what should happen when we encounter certain types of errors

- Give an example of when you would throw an exception. (write code)

user_input = input("Enter a number between 1 and 1000:")

while user_input <1 or user_input > 1000:
    print("enter another number")
    user_input = input("Enter a number between 1 and 1000:")
else:
    continue


Notes for self:
Throwing an exception: an error has occurred and you want the user to deal with it (you throw them the exception back)
e.g. you wanted a number between 1 and 10 and they entered 11. You ask them to enter the number against
Catching an exception: an error has occurred and you do something with it. e.g. in exceptions testing you may choose to convert the data type on behalf of the user

- Give a code example of how you would handle the exception above.
- What is "Pbd"? How do we use it?

## List comprehensions/generators

- Generate the following array with list comprehensions: 
    - `[2, 4, 6, 8, 10, 12, 14, 16, 18]`
    - `[2, 4, 8, 16, 32, 64, 128, 256, 512]`

numbers_list = [x * 2 for x in range(10)]
print(numbers_list)



- What is the difference between:
    - `[x for x in range(10)]`
    - `(x for x in range(1, 10))`

 The second line will miss out the first item in range (idx 0)

## Databases

- What is a primary key?
The primary key is the only key that requires a value in a table. Often used to lookup the table (e.g. entry #)

- What is a foreign key?
Any other key that isn't a primary key?!

- What is a relational database?
A database where links between data tables can be made using related columns

- What makes a database relational?
A relational database is organised in columns and rows. Columns are used to relate one table to another

- How do we avoid releating and redundant data in relational databases?
We can ensure certain columns are always complete within certain parameters (e.g. must contain an integer up to 1000).
This means whenever we link to the column, there will be a valid entry to lookup

- Write a simple database schema (make up your own). Write a simple `SELECT`, `INSERT` and `DELETE` query against your schema. Make sure they actually work.

- Given the following schema:

```sql
CREATE TABLE IF NOT EXISTS employees ( 
    employee_id decimal(6,0) NOT NULL PRIMARY KEY, 
    first_name varchar(20) DEFAULT NULL, 
    last_name varchar(25) NOT NULL, 
    salary decimal(8,2) DEFAULT NULL, 
    manager_id decimal(6,0) DEFAULT NULL
);
```

write the following queries:
- A result set of employees that have a salary above $50,000K
SELECT * FROM employees.first_name, employees.last_name WHERE employees.salary > 50000

- A result set of all the employees and their corresponding managers.
SELECT
employees.first_name
employees.last_name
LEFT JOIN employees
on manager_id = employee_id

- A result set of all the managers and the average salary of the employees that report to them.
SELECT AVG(salary) as AVERAGE_SALARY
FROM employees
GROUP BY manager_id

## Challenges (do as many as you can)
- Write a function to reverse a string

my_string = "hello world"

def reverse_fn(x):
    x = x[::-1]
    return x

output = reverse_fn(my_string)
print(output)


- Write a function that determines if a number is odd or even

user_input = int(input("enter a number:"))

def odd_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

output = odd_even(user_input)
print(output)



- Write a function to check if a number is prime

user_input = int(input("enter a number:"))

def prime_n(x):
    for numbers in range(2, x):
        if x % numbers != 0:
            return f'"number is prime"'
        else:
            return f'"number is NOT prime"'

output = prime_n(user_input)
print(output)


- Write a function that generates the first n prime numbers


- Write a function that takes a list as input and returns a list with all duplicates removed. eg: `[1,1,2,2,3]` -> `[1,2,3]`
- Write a generator function that creates the [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number)
- Write a python implementation of the `wc` command. See `man wc` for a description of how it is supposed to work.
