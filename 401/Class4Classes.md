# Classes, Objects, and Recursion

## Classes and Objects

This topic matters in relation to what we are studying in this module because we will need to understand how to assign classes and refer to the objects within them, and how to break problems into smaller problems for recursive functions.

According to [Learn Python](https://www.learnpython.org/en/Classes_and_Objects), Classes are essentially templates for information while objects are instances for these templates. An example is cookie cutters - the classes would be the cookie cutters (a group of things with similar characteristics) and the objects would be the individual cookie cutters in different shapes like a sleigh, or a tree, or a gingerbread person. A class needs to be started or initialized by using the __init__ function while an object needs to be set equal to the class it is a part of.

## Recursion

While writing recursive problems, one needs to break down the problem into the most simple cases and then tell the computer how to solve those cases. From there, the programmer needs to tell the computer how to build complexity onto the base cases in a repeatable way. The computer solves this problem by starting from the complicated case and remembering what needs to be done for simpler and simpler cases. Then when it reaches the base case, it takes in this information and solves for all of the simpler cases until it returns to the base case. It is like a yoyo starting in your hand (with the problem) unwinding until it reaches the ground (the base case) and then rewinding into your hand (as it solves the successive problems from the base case back to the original problem.)

The state, and other variables needed to run the function need to be stored outside of the function so that they can be updated as the function is run. In the yoyo example above, to measure the height of the yoyo it would be easier to look at the yoyo as compared to an outside perspective a fixed yardstick.

## Testing

Finally, to make sure that the code works, it is important to have unit tests that prove the functionality of different sections. This is especially helpful if one is refactoring or rewriting code to make sure that the code fulfils its initial intentions.

[Reading Notes Home Page](README.md)