# Git

### What is Git and How does it Work?

Git is essentially a program for being able to work on a bit of a program while the main program is operational.

The **main** is the basic version of the site or code or program that is being worked on.
The **branches** are the places where someone wants to work on something.
The **repository** is the places where all versions or changes can be stored and accessed lated.

Benefits include:
- Changes can be made and worked with without impacting the working elements on the main site.
- Multiple coders can work on different branches for fixes, changes, and updates without affecting each other or the main code.
- Previous versions of the main and of branchces in progress are accessible in case you want to bring back old elements or restore a version from before you made a mistake.
- Versions can be kept in the cloud in virtual servers called *repositories* so if something happens to a computer a backup of a previous version can keep you from losing everything you had worked on.
- Different elements of the main system can be worked on in pieces or out of order.

When branches are tested and proven to be working, they can be incorporated in the main.


### Git Vocab
- A **commit** is saving an updated version of your project.
- A **snapshot** is a reference to the file a commit is stored into. This creates an organized library of changes.
- **Local operations** are the set of recently saved commits that are stored in your computer without the main system.
- Git will **track changes** or keep track of updates and different versions. It will also note if files are damaged or if information is lost between versions.
- **Loss of data** is prevented by having saved previous versions so information can be recovered.
- **States** are the phases a file can be in. A file can be in one of three states which are:
  - **Committed** or stored in a local database
  - **Modified** or changed without having been committed
  - **Staged** which is ready and waiting to be commited

### Git Repositories
Github is a very popular version of a repository for git where files can be stored updated and worked on.

However, files can be downloaded to a local repository (ie. on your computer), or full repositories can be downloaded which is called cloning.

There is some repository related vocab regarding the stages of files being downloaded and file status:

The **head** is the most recent version to be worked on (or committed) which comes from the **index** which is the file storage and staging area where files are first added from the **working directory**. 

*Files* are **tracked** or **untracked** depending on whether they are committed into the last file snapshot while *changes within files* can be make the file considered **modified**. A modfied file is considered to be **staged** when it is completed until it is committed to a new file. Once versions of the files are all complete, the finished files can be **pushed** or re-uploaded into teh main repository.

[Reading Notes Home Page](README.md)
