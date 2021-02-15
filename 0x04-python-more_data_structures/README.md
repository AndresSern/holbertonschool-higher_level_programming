# 0x04. Python - More Data Structures: Set, Dictionary
In this directory you will see more documentacion about Data Structures: Set, and Dictionary

## GENERAL:

1.  Why Python programming is awesome
2.  What are set and how to use them
3.  What are the most common methods of set and how to use them
4.  When to use sets versus lists
5.  How to iterate into a set
6.  What are dictionary and how to use them
7.  When to use dictionaries versus lists or sets
8.  What is a key in a dictionary
9.  How to iterate into a dictionary
10. What is a lambda function
11. What is map, reduce and filter functions 


## Read or watch:

1.    **[Data structures:](https://docs.python.org/3.4/tutorial/datastructures.html)**
2.    **[Lambda, filter, reduce and map:](https://www.python-course.eu/python3_lambda.php)**
3.    **[Learn to Program 12 Lambda Map Filter Reduce:](https://www.youtube.com/watch?v=1GAC6KQUPeg)** 


## Files:

1.  **0-square_matrix_simple.py**
2.  **1-search_replace.py**
3.  **2-uniq_add.py**
4.  **3-common_elements.py**
5.  **4-only_diff_elements.py**
6.  **5-number_keys.py**
7.  **6-print_sorted_dictionary.py**
8.  **7-update_dictionary.py**
9.  **8-simple_delete.py**
10.  **9-multiply_by_2.py**
11.  **10-best_score.py**
12. **11-multiply_list_map.py**
13. **12-roman_to_int.py**
14. **101-square_matrix_map.py**
15. **102-complex_delete.py**

## Tasks

### 0. Squared simple
*   File: **0-square_matrix_simple.py**

*Write a function that computes the square value of all integers of a matrix.*

1.  Prototype: def square_matrix_simple(matrix=[]):
2.  matrix is a 2 dimensional array
3.  Returns a new matrix:
    - Same size as matrix
    - Each value should be the square of the value of the input
4.  Initial matrix should not be modified
5.  You are not allowed to import any module
6.  You are allowed to use regular loops, map, etc.

Example:

```
guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```

### 1. Search and replace  
*   File: **1-search_replace.py**

*Write a function that replaces all occurrences of an element by another in a new list.*

1.  Prototype: def search_replace(my_list, search, replace):
2.  my_list is the initial list
3.  search is the element to replace in the list
4.  replace is the new element
5.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$ 
```

### 2. Unique addition 
*   File: **2-uniq_add.py**

*Write a function that adds all unique integers in a list (only once for each integer).*

1.  Prototype: def uniq_add(my_list=[]):
2.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 
```

###  3. Present in both 
*   File: **3-common_elements.py**

*Write a function that returns a set of common elements in two sets.*

1.  Prototype: def common_elements(set_1, set_2):
2.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 
```

### 4. Only differents  
*   File: **4-only_diff_elements.py**

*Write a function that returns a set of all elements present in only one set.*

1.  Prototype: def only_diff_elements(set_1, set_2):
2.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 
```

###   5. Number of keys

* File: **5-number_keys.py**

*Write a function that returns the number of keys in a dictionary.*

1.  Prototype: def number_keys(a_dictionary):
2.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 


```

### 6. Print sorted dictionary 

*   File: **6-print_sorted_dictionary.py**

*Write a function that prints a dictionary by ordered keys.*

1.  Prototype: def print_sorted_dictionary(a_dictionary):
2.  You can assume that all keys are strings
3.  Keys should be sorted by alphabetic order
4.  Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
5.  Dictionary values can have any type
6.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
```


### 7. Update dictionary 
*   File: **7-update_dictionary.py** 

*Write a function that replaces or adds key/value in a dictionary.*

1.  Prototype: def update_dictionary(a_dictionary, key, value):
2.  key argument will be always a string
3.  value argument will be any type
4.  If a key exists in the dictionary, the value will be replaced
5.  If a key doesn’t exist in the dictionary, it will be created
6.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$
```

### 8. Simple delete by key
*   File: **8-simple_delete.py**

*Write a function that deletes a key in a dictionary.*

1.  Prototype: def simple_delete(a_dictionary, key=""):
2.  key argument will be always a string
3.  If a key doesn’t exist, the dictionary won’t change
4.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 
```

###  9. Multiply by 2 mandatory

*   File: **9-multiply_by_2.py**

*Write a function that returns a new dictionary with all values multiplied by 2*

1.  Prototype: def multiply_by_2(a_dictionary):
2.  You can assume that all values are only integers
3.  Returns a new dictionary
4.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
```

### 10. Best score 
*   File: **10-best_score.py**

*Write a function that returns a key with the biggest integer value.* 

1.  Prototype: def best_score(a_dictionary):
2.  You can assume that all values are only integers
3.  If no score found, return None
4.  You can assume all students have a different score
5.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
```

### 11. Multiply by using map 

*   File: **11-multiply_list_map.py**

*Write a function that returns a list with all values multiplied by a number without using any loops.* 

1.  Prototype: def multiply_list_map(my_list=[], number=0):
2.  Returns a new list:
     - Same length as my_list
     - Each value should be multiplied by number
3.  Initial list should not be modified
4.  You are not allowed to import any module
5.  You have to use map
6.  Your file should be max 3 lines

```
guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
```

### 12. Roman to Integer

*   File: **12-roman_to_int.py**

*Technical interview preparation:* 

1.  You are not allowed to google anything
2.  Whiteboard first

*Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.*

1.  You can assume the number will be between 1 to 3999.
2.  def roman_to_int(roman_string) must return an integer
3.  If the roman_string is not a string or None, return 0

```

```

### 14. Squared by using map 

*   File: **101-square_matrix_map.py**

*Write a function that computes the square value of all integers of a matrix using map* 

1.  Prototype: def square_matrix_map(matrix=[]):
2.  matrix is a 2 dimensional array
3.  Returns a new matrix:
     - Same size as matrix
     - Each value should be the square of the value of the input
4.  Initial matrix should not be modified
5.  You are not allowed to import any module
6.  You have to use map
7.  You are not allowed to use for or while
8.  Your file should be max 3 lines

```
guillaume@ubuntu:~/0x04$ cat 101-main.py
#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```

### 15. Delete by value 
*   File: **102-complex_delete.py**

*Write a function that deletes keys with a specific value in a dictionary.* 

Prototype: def complex_delete(a_dictionary, value):
If the value doesn’t exist, the dictionary won’t change
All keys having the searched value have to be deleted
You are not allowed to import any module


```
guillaume@ubuntu:~/0x04$ cat 102-main.py
#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
guillaume@ubuntu:~/0x04$ 
```
