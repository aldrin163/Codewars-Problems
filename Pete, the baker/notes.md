# New Concepts encountered or old Concepts worth Revising

## Infinity in Python

In python, infinity can be represented using:
    float('inf')
Note that this will not work for an intiger and will result in run-time error if float is replaced with int.

~~~ a = float('-inf') # works
    b = float('inf') # works
    c = int('-inf') # compile error, ValueError: invalid literal for int() with base 10: 'inf'
    d = int('inf') # compile error, ValueError: invalid literal for int() with base 10: 'inf'
~~~

## .get method for objects/dictionaries

For dictionaries, the .get method allows two arguments with the first one being the item to search and the second one being the output to be returned in case the item does not exist in the dictionary
For reference: <https://www.geeksforgeeks.org/get-method-dictionaries-python/>

## min function

The min function gives the smallest of all the arguments passed
