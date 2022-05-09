# SQL Review
A work-through of the SQLBolt curriculum.

## Lesson 1 - SELECT Queries

**Select** statements find information from the SQL database. *Query* statements are used to specify the data we are looking for and how to return it for our uses. 

The full SQL table is called an **entity** and each line in the table (or the info about one specific thing) is called an **instance**.

Select * brings back the full table. You can use a comma between queries. Remember to add the from and the name of the database. 

![Lesson 1 Completed](401/SQLReview/SQL1.PNG)

## Lesson 2 - Logic and Filtering

You can specify for your data by returning columns **Where** conditions are met. Included operators are:
=, !=, < <=, >, >=
BETWEEN … AND …	
 NOT BETWEEN … AND …
 IN (…)(numbers and strings in a list)
 NOT IN (…)(numbers and strings in a list)

![Lesson 2 Completed](401/SQLReview/SQL2.PNG)

## Lesson 3 - More Filters

= (case sensitive exact string)
!=/<> (not)
LIKE/NOT LIKE (not case sensitive exact string)
% (characters within colunms)
_ (characters with something following)

All strings in the query you are looking for need to be in quotes in the parenthesis.

![Lesson 3 Completed](401/SQLReview/SQL3.PNG)

## Lesson 4 - Removing Duplicates and Ordering Results

**Select Distinct** will remove duplicate rows in the table. 
You can **order by** as the last line in the query to return the data in a way that makes sense. 
When you Order by you can also **limit** the amount of lines returned or **offset** to start at a certain line based on the order.

![Lesson 4 Completed](401/SQLReview/SQL4.PNG)

## Lesson 5 - Practice

![Lesson 5 Completed](401/SQLReview/SQL5.PNG)

## Lesson 6 - Joining Data from Multiple Tables
When tables share information about one thing that thing has a primary key in the different tables. **Join** combines the data from different tables for the shared entity key. 

You need to add the **on** constraint and match the IDs
 ON mytable.id = another_table.id


![Lesson 6 Completed](401/SQLReview/SQL6.PNG)

## Lesson 13 - 


![Lesson 13 Completed](401/SQLReview/SQL13.PNG)

## Lesson 14 - 


![Lesson 14 Completed](401/SQLReview/SQL14.PNG)

## Lesson 15 - 


![Lesson 15 Completed](401/SQLReview/SQL15.PNG)

## Lesson 16 - 


![Lesson 16 Completed](401/SQLReview/SQL16.PNG)

## Lesson 17 - 


![Lesson 17 Completed](401/SQLReview/SQL17.PNG)

## Lesson 18 - 


![Lesson 18 Completed](401/SQLReview/SQL18.PNG)



[Reading Notes Home Page](README.md)