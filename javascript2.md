# Basic Javascript Programming: Functions and Operations

## Operators
Operators are essentially the different ways that variables (or operands) can interact with each other. 

There are three types of operators:
- **Binary Operators** use two operands and the operator. One common example is saying 1+2 where the numbers are the operands and the + sign is the addition operator. Binary operators include:
    - Assignment (x =5)
    - Comparison (Does 3+2 = 5?)
    - Arithmatic (5*4)
    - Logical (and/or/not)
    - Adding Strings ('Happy'+'Birthday')
- **Unary Operators** have only the operand and one operator. An example would be deleting a variable which in Javascript looks like 
    - delete var;
- The **Ternary Operator** is essentially just a way to refer to conditional operators. It is essentially a shorthand block for an if/else statement. There are three parts - the conditional operator, and the two possible values.  

## Functions
Functions use the inputs and operators to perform tasks. Whether to calculate problems or perform tasks, functions take in the inputs manipulate them based on the code, and provide related outputs.

According to MDN Web Docs, A function is usually made up of three parts:
    - The name of the function.
    - A list of parameters to the function, enclosed in parentheses and separated by commas.
    - The JavaScript statements that define the function, enclosed in curly brackets, {...}.

However, functions can also be written as expressions which omits the name of the function. 

**It is important to note that defining or *calling* a function and running or *excecuting* a function are different.**

Functions can be run in many different ways. They can be **nested** aka placed inside of different function sor they can be **recursive** aka placed inside of themselves. **Control Flow** dictates the order in which the computer reads the script file. Usually this is from top to bottom unless there is something like a loop or conditional that redirects the computer. 

Functions are written in the following format:

    - function (parameters) {
    -     Code
    - }

Notice how the parameters are in round brackets and the code is in curly brackets. The function will run until another part of the code calls for the function to **return**.


[Reading Notes Home Page](README.md)