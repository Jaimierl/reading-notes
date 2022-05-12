# The Command Line

For this assignment, we read through several tutorials on ryanstutorials.net

In this tutorial we learned about the command line which is a text based interface to interacting with the computer as opposed to the graphics user interface (GUI) with windows, images, amd taskbars that many people usually use. In the command line the computer gives prompts and the user gives the computer commands. 

The **command line interface** where you can input or type in commands while the **shell** is the application that runs the commands or interfaces between different programs. 

Then the author goes into commands using the command line:
- pwd will show the current directory, or folder the user is in
- ls will show files in that location while ls -l will also show file information. 

## Navigation

While navigating through the command line it is also important to note that files have paths which are like their addresses in the system. Files can have absolute paths which is their location from the root directory or being outside of all folders (these paths start with a "/"), or a relative path which is the path from your current location in the file directory. Some navigational tools presented are:
- ~ or cd for returning to the root directory
- . for calling the present directory
- .. for moving up or out of a folder by one directory
When typing out a directory you can also use tab to autocomplete a phrase if the letters typed so far are unique.  

## Files

Essentially every endpoint or location in linux is considered to be a file, whether that file is an actual file or a path/directory. File names in the terminal are case sensitive. If the file name includes spaces, then to reference the file name you would need to "use quotes" or a backslash in front of the space("/ "). Also some files may be hidden. To access hidden files you would need to use ls -a to show all files ni a directory including hidden files. 

## Help

Essentially the help manual or the ability to see what commands do is stored in the manual menu. This can be accessed by running man<command to find> (notice the command is in <brackets>). You can also look up terms to search by using man -k <thing to search>. 

## File Manipulation 

When moving, deleting, and other actions remember that there is no undo button for the command line. That being said, here sre some command line manipulation tools:

- mkdir will create a directory or folder
- touch will make an empty file in the current directory 
- cp <> will copy a file
- mv <old location> <new location> will move a file or can be used to rename a file id you do mv <old file name> <new file name>
- rm remove the file
- rmdir will remove a non-empty directory

For more commands, see the [**full list here**](https://ryanstutorials.net/linuxtutorial/cheatsheet.php)

[Reading Notes Home Page](README.md)