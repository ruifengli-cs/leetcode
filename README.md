# Note
1. Python map() function

map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax :
map(fun, iter)
eg. LeetCode 66. Plus One
Input: [1,2,3]
Output: [1,2,4]
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
        
2. zip() in Python

The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
Syntax :
zip(*iterators)

Parameters :
Python iterables or containers ( list, string etc )
Return Value :
Returns a single iterator object, having mapped values from all the
containers.

3. Python String find()

The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
Syntax :
str.find(sub,start,end)

sub : It’s the substring which needs to be searched in the given string.
start : Starting position where sub is needs to be checked within the string.
end : Ending position where suffix is needs to be checked within the string.

word = 'geeks for geeks'
result = word.find('geeks') 
print ("Substring 'geeks' found at index:", result )
result = word.find('for') 
print ("Substring 'for ' found at index:", result )  
output:
Substring 'geeks' found at index: 0
Substring 'for ' found at index: 6

4. Python Dictionary | setdefault() method
In Python Dictionary, setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
Syntax: dict.setdefault(key[, default_value])

Parameters: It takes two parameters:
key – Key to be searched in the dictionary.
default_value (optional) – Key with a value default_value is inserted to the dictionary if key is not in the dictionary. If not provided, the default_value will be None.

Returns:
Value of the key if it is in the dictionary.
None if key is not in the dictionary and default_value is not specified.
default_value if key is not in the dictionary and default_value is specified.

5. python lambda
In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax:
Syntax: lambda arguments : expression
This function can have any number of arguments but only one expression, which is evaluated and returned.
lambda a : a ** n 

6. collections.Counter()

Once initialized, counters are accessed just like dictionaries. Also, it does not raise the KeyValue error (if key is not present) instead the value’s count is shown as 0.

from collections import Counter 
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red'] 
col_count = Counter(z) 
print(col_count) 
Counter({'blue': 3, 'red': 2, 'yellow': 1})

7. String | count()
count() function in an inbuilt function in python programming language that returns the number of occurrences of a substring in the given string.
Syntax:
string.count(substring, start=…, end=…)

string = "geeks for geeks" 
print(string.count("geeks")) 
output: 2

8. max()
max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.

