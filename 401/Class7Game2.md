# Ten Thousand Game 2 - Global and Nonlocal Scope

This topic matters in relation to what we are studying in this module as we will be creating a game that simulates dice rolling in a way that may need to access functions from other areas of the code-base.

According to [Real Python](https://realpython.com/python-scope-legb-rule/#modifying-the-behavior-of-a-python-scope), by default, a **global name** can be accessed from anywhere in the code, a **local name** can be accessed from the function it is a part of, and **nonlocal names** can be accessed but not updated from inside of functions.

From the inside of a function, if you use global to define a variable, the variable will be accessible from outside of the function it is written in. While this is possible, it makes the initialization of variables hard to find and is not considered good practice.

The nonlocal allows the programmer to modify or update nonlocal names, or names that can only be accessed from inside of functions.

[Reading Notes Home Page](README.md)