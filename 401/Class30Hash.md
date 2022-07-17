# Hash Tables

In this module we will be studying Hash Tables. In Python, these are mostly built in as dictionaries.

There is a Hash, or a string that determines the index of an array, and an array of nodes with key/value pairs. It is really interesting to learn that the hash keys and number of nodes in the hash array can essentially be created by the programmer. 

Things can be looked up in O(1) time even though if a collision happens, the new keys and values are stored in a linked list. This is still more efficient than using an array because with a hash table the computer can have a starting point that should hopefully eliminate at least some items in the full array and narrow things down to only the linked list things. Even though you would have to cycle through N items in the linked list, if the overall has table is implemented properly, data would be stored more or less evenly among the available spaces in the array which would minimize the needing to cycle through a list and bring the average lookup time to being linear. 

[Reading Notes Home Page](README.md)