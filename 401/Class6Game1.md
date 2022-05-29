# Ten Thousand Game 1: Assorted Topics in Python

This topic matters in relation to what we are studying in this module as we will be creating a game that rolls dice and keeps tracks of the users points.

The random module allows the program to choose an integer from a range, choose an integer from a list, or shuffle values in a list. 

Risk analysis is related to software development because as developers it is important to anticipate the issues the program is most likely going to run into and to create tests to make sure that the program is protected against those issues. 

When writing tests for programs, it is more important to include high quality tests than simply having a myriad of tests just for the sake of it. 

## Big O - Scaling with Input Variables
O(1) - Takes the same amount of time/space regardless to the size of the input
O(N) - Scales linearly with the amount of input
O(N^2) - Scales quadratically

A few rules to remember:
- Different inputs would become different variables ie. Looping through two arrays would be O(A*B) not O(N)
- The least efficient O of N step is the one that dictates the efficiency of the algorithm.

## Dependency Injection

**Dependency Injection** is when one object supplies an object (or information) to another object. The objects are linked by relying on each other for information. Using dependencies essentially means that the code can be written with one set of default information and have input data changed or specified at a later time. Dependency Injection separates responsibilities by creating and providing the objects a class needs so the class only needs to fulfil its outlined responsibilities. This is mainly used in Java and .Net although it can be found in any programming language. 

[Reading Notes Home Page](README.md)