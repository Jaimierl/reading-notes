# Ten Thousand Game 3- List Comprehensions, Debugging, and Decorators

This topic matters in relation to what we are studying in this module:

Either answer provided questions or summarize this module and explain the topic via an analogy to something everyday.  

## List Comprehensions

Lists can have every value spelled out or they can be created with words in python. Lists can be created by using ranges, loops, or by looking for specific information in accessed data-sets. List comprehension can also be used to help parse through data. 

## Debugging

This podcast met with the creator of PySnooper, a program created by Ram Rachum for debugging legacy python projects. Apparently, the way for programmers to see what particular pieces of code were doing was to use print statements. This can quickly get clunky and out of hand for large projects especially when one programmer does not have full exclusive access to the code and when working on code that has been amended by many people in the past.

Essentially, it seems like PySnooper can follow individual functions so the programmer can see what different functions impact in the program. This is like a control find that works for full functions and their related variables instead of just for keywords.

It was also fun to hear about the creation process. Even when creating the projects necessary for class there are often elements that we want to include and end up not getting around to, so it was interesting to see that even professionals sometimes get to their minimum viable product and then call things good enough or to create the proof of concept and then pivot to meet the user demands.

## Decorators

According to [Real Python](https://realpython.com/primer-on-python-decorators/) "a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it." Essentially, in python functions can be treated like objects and they can also be used as the input to other functions. 

The wrapper function takes the object function and can use it in conjunction with other operations. Essentially, it allows one function to reference or use another function. 

You can use the "@" sign with the decorator function name above the function you would like to decorate. You can re-use decorators, use arguments to pass information into decorated functions, and return values from decorated functions.

[Reading Notes Home Page](README.md)