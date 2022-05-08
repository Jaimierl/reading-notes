# Memory Storage

## The JavaScript Call Stack

1. A call is a function invocation. One of those short words where the definition is even harder.
2. Calls happen one at a time.
3. LIFO means Last In First Out
4. The following is an example of a stack and the functions needed to call the stack: 
  function One(){
    console.log('1')
  }

  function Two (){
    console.log('2')
  }

  Two()
5. A function calling itself without an endpoint causes a Stack Overflow.

## JavaScript Error Messages

1. A reference error is when you try to use a variable you have not yet declared.
2. A syntax error essentially means you are using an embedded JS function/method wrong. Like when you try to use a string method on an array or forgetting a comma.
3. A range error is when you mess up the length of something. Like if you ask to loop through an array with three elements 5 times.
4. A type error is when you mix the types of things. Like using a number with a string without putting things together properly.
5. A breakpoint is where your code breaks. You can do this by including a debugger statement.
6. In the code, a debugger is a program that can help you find your programs problems while it is running.

[Reading Notes Home Page](README.md)