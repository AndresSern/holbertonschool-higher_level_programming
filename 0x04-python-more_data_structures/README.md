# 0x04. Python - More Data Structures: Set, Dictionary

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>What are set and how to use them</li>
	<li>What are the most common methods of set and how to use them</li>
	<li>When to use sets versus lists</li>
	<li>How to iterate into a set</li>
	<li>What are dictionary and how to use them</li>
	<li>When to use dictionaries versus lists or sets</li>
	<li>What is a key in a dictionary</li>
	<li>How to iterate into a dictionary</li>
	<li>What is a lambda function</li>
	<li>What is map, reduce and filter functions</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/dnFegYagqFoW7WraIP-9RA" title="Data structures" target="_blank">Data structures</a> </li>
	<li><a href="/rltoken/xXAlsMIs9-sCL4fljYeNfg" title="Lambda, filter, reduce and map" target="_blank">Lambda, filter, reduce and map</a> </li>
	<li><a href="/rltoken/AT-UtsGuhgIzQSwSdKvckw" title="Learn to Program 12 Lambda Map Filter Reduce" target="_blank">Learn to Program 12 Lambda Map Filter Reduce</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-square_matrix_simple.py**:](#0-square_matrix_simplepy) Function that computes the square value of all integers of a matrix.
1.	[**1-search_replace.py**:](#1-search_replacepy) Function that replaces all occurrences of an element by another in a new list.
2.	[**2-uniq_add.py**:](#2-uniq_addpy) Function that adds all unique integers in a list (only once for each integer).
3.	[**3-common_elements.py**:](#3-common_elementspy) Function that returns a set of common elements in two sets.
4.	[**4-only_diff_elements.py**:](#4-only_diff_elementspy) Function that returns a set of all elements present in only one set.
5.	[**5-number_keys.py**:](#5-number_keyspy) Function that returns the number of keys in a dictionary.
6.	[**6-print_sorted_dictionary.py**:](#6-print_sorted_dictionarypy) Function that prints a dictionary by ordered keys.
7.	[**7-update_dictionary.py**:](#7-update_dictionarypy) Function that replaces or adds key/value in a dictionary.
8.	[**8-simple_delete.py**:](#8-simple_deletepy) Function that deletes a key in a dictionary.
9.	[**9-multiply_by_2.py**:](#9-multiply_by_2py) Function that returns a new dictionary with all values multiplied by 2
10.	[**10-best_score.py**:](#10-best_scorepy) Function that returns a key with the biggest integer value.
11.	[**11-multiply_list_map.py**:](#11-multiply_list_mappy) Function that returns a list with all values multiplied by a number without using any loops.
12.	[**12-roman_to_int.py**:](#12-roman_to_intpy) <strong>Technical interview preparation</strong> Create a function <code>def roman_to_int(roman_string)</code> that converts a <a href="/rltoken/g7UKrGGWwbRJRkdB3tFThg" title="Roman numeral" target="_blank">Roman numeral</a> to an integer.
13.	[**101-square_matrix_map.py**:](#101-square_matrix_mappy) Function that computes the square value of all integers of a matrix using <code>map</code>
14.	[**102-complex_delete.py**:](#102-complex_deletepy) Function that deletes keys with a specific value in a dictionary.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-square_matrix_simple.py

**<p>Function that computes the square value of all integers of a matrix.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 0-main.py
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
</code></pre>

### 1-search_replace.py

**<p>Function that replaces all occurrences of an element by another in a new list.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 1-main.py
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
</code></pre>

### 2-uniq_add.py

**<p>Function that adds all unique integers in a list (only once for each integer).</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 
</code></pre>

### 3-common_elements.py

**<p>Function that returns a set of common elements in two sets.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 
</code></pre>

### 4-only_diff_elements.py

**<p>Function that returns a set of all elements present in only one set.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 
</code></pre>

### 5-number_keys.py

**<p>Function that returns the number of keys in a dictionary.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
</code></pre>

### 6-print_sorted_dictionary.py

**<p>Function that prints a dictionary by ordered keys.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 6-main.py
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
</code></pre>

### 7-update_dictionary.py

**<p>Function that replaces or adds key/value in a dictionary.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 7-main.py
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
</code></pre>

### 8-simple_delete.py

**<p>Function that deletes a key in a dictionary.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 8-main.py
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
</code></pre>

### 9-multiply_by_2.py

**<p>Function that returns a new dictionary with all values multiplied by 2</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 9-main.py
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
</code></pre>

### 10-best_score.py

**<p>Function that returns a key with the biggest integer value.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 10-main.py
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
</code></pre>

### 11-multiply_list_map.py

**<p>Function that returns a list with all values multiplied by a number without using any loops.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 11-main.py
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
</code></pre>

### 12-roman_to_int.py

**<p><strong>Technical interview preparation</strong> </p><p>Create a function <code>def roman_to_int(roman_string)</code> that converts a <a href="/rltoken/g7UKrGGWwbRJRkdB3tFThg" title="Roman numeral" target="_blank">Roman numeral</a> to an integer.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
</code></pre>

### 101-square_matrix_map.py

**<p>Function that computes the square value of all integers of a matrix using <code>map</code></p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 101-main.py
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
</code></pre>

### 102-complex_delete.py

**<p>Function that deletes keys with a specific value in a dictionary.</p>**

<pre><code>guillaume@ubuntu:~/0x04$ cat 102-main.py
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
</code></pre>

