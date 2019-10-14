Day 1: Baseline Quiz
====

## Intro

Some of the questions below are short-answer questions, others require some coding. Some of the short-answer questions may require you to write some code to explain yourself.

Please take your time with this quiz, there is no rush. While we generally strongly encourage you to use Google to answers questions on a very regular basis, please do your best to complete this quiz without any external assistance from Google or from the CodingNomads online platform.

When you have finished, or gotten as far as you can, please email your quiz to yurigorokhov@gmail.com and ryan@codingnomads.co. After everyone has completed the quiz and emailed their results to Yuri and Ryan we will discuss the quiz as a class.

## Git & GitHub

- What is Git?
- What is GitHub?
- Please list all the Git commands you can think of, and explain what each of the commands does.
- What is the general git workflow for a developer on a day-to-day basis?
- Is it important to push your work to GitHub every day?

## Python Basics

- Name 5 python keywords.
- Describe the difference between a `statement` and an `expression`. Provide an example of each.
- Name the primitive python datatypes (as many as you can think of), and provide a declaration of each.
- Convert a floating point to an integer
- Name some complex python data structures. Specify why and when you would use these.
- Write a `for` loop and a `while` loop
    - When would you prefer one over the other?

## Functions
- What is a function? Define a simple function. (One that adds two numbers for example)
- When a variable is declared inside a function, what scope does it have?
- Describe variable shadowing and how it applies to functions (use code to explain yourself if appropriate)
- What are first class functions? Provide a code example of first class functions being used.
- What does the return keyword do
- [Optional] - What is pass by reference vs pass by value? When would you use one over the other?

## OOP
- What is object oriented programing. Why use it? 
- What is the difference between a function and a method?
- Write and use a simple class that contains: a constructor, an instance variable, an instance method.
- Describe inheritance. Why use it?
- What does is to mean to "override" a function?
- What is `self`
- What is polymorphism? 

## Error handling
- Unfortunately programs do not always run perfectly. What type of errors might occur in a program?
- How does python handle reporting and handling of these errors?
- [Optional] what are other ways to handle errors?
- Give an example of when you would throw an exception. (write code)
- Give a code example of how you would handle the exception above.
- What is "Pbd"? How do we use it?

## List comprehensions/generators

- Generate the following array with list comprehensions: 
    - `[2, 4, 6, 8, 10, 12, 14, 16, 18]`
    - `[2, 4, 8, 16, 32, 64, 128, 256, 512]`
- What is the difference between:
    - `[x for x in range(10)]`
    - `(x for x in range(1, 10))`

## Databases

- What is a primary key?
- What is a foreign key?
- What is a relational database? 
- What makes a database relational?
- How do we avoid releating and redundant data in relational databases?
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
- A result set of all the employees and their corresponding managers.
- A result set of all the managers and the average salary of the employees that report to them.

## Challenges (do as many as you can)
- Write a function to reverse a string
- Write a function that determines if a number is odd or even
- Write a function to check if a number is prime
- Write a function that generates the first n prime numbers
- Write a function that takes a list as input and returns a list with all duplicates removed. eg: `[1,1,2,2,3]` -> `[1,2,3]`
- Write a generator function that creates the [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number)
- Write a python implementation of the `wc` command. See `man wc` for a description of how it is supposed to work.
