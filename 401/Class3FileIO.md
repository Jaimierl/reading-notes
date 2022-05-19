# FileIO and Exceptions 

## Files

This topic matters in relation to what we are studying in this module as we learn to navigate to files in terminal including opening the files, reading the data from them, and closing the files. 

It is very important to remember to close files when they are open. It is like when you open the fridge to retrieve something, it needs to be closed when you are finished. The open command needs the file name (file = open('file_name.txt')) while the close command just needs to come after the manipulation of the open file (file.close()). One can also use a with statement:
- with open('file_name.txt', mode) as reader
- -   file manipulation directions would be indented here

The with statement will automatically close the file when the indented file manipulation portion has been run. The **mode** is optional, although that is the location wherein you could specify if the file is open for reading or writing, or for either using byte data. 

Python can be used to read files or even iterate through lines of files in which more information can be found [here](https://realpython.com/read-write-files-python/). It can also be used to append information into files or work with multiple files. The most common file types Python reads data from are JSON and CSV files. 

## Exceptions vs. Syntax Errors

Syntax errors are when things are written improperly while exceptions are when properly written code does not work. You can **raise** or program in an error to show where something is going wrong in the running of your code. Assertions are another proactive way to handle errors because they state that an initial condition must be met so the code will run in the first place. 

According to the [Real Python Guide to Exceptions](https://realpython.com/python-exceptions/), there are four elements that may be included in block handling exceptions: 
- In the **try** clause, all statements are executed until an exception is encountered.
- **Except** is used to catch and handle the exception(s) that are encountered in the try clause.
- **Else** lets you code sections that should run only when no exceptions are encountered in the try clause.
- **Finally** enables you to execute sections of code that should always run, with or without any previously encountered exceptions. 

[Reading Notes Home Page](README.md)