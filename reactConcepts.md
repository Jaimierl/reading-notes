# React and Concepts

## Thinking in React

1. The Single Responsibility Principle is the idea that a component should only do one thing.
2. Building a static version of your application means building a version with all of the data set up but with no user interactivity built in.
3. When you have a static application you need to add state to make the site interactive.
4. An element of data is not state if the data is passed in from a parent via props, if it remains unchanged over time, or if it can be computed based on any other existing state.
5. Essentially the state needs to be higher in the "tree" of components than any of the components that need the information from the state. A component can be added to the tree with the express purpose of holding the state.

## Higher-Order Functions

1. According to [EloquentJavascript](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK), a Higher-Order Function is a function that operates on other functions either by taking them as arguments or by returning them.
2. In line two of the greaterThan function [here](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK) the function compares two numbers and returns true or false if the an input is greater than the number in question (in the formula it is asking whether 11 is greater than 10).
3. With regards to higher-order functions, map works by transforming an array but putting all of its elements through a function and reduce combines all of the elements in an array into a single value.

[Reading Notes Home Page](README.md)