# 0x03. Python - Data Structures: Lists, Tuples

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>What are lists and how to use them</li>
	<li>What are the differences and similarities between strings and lists</li>
	<li>What are the most common methods of lists and how to use them</li>
	<li>How to use lists as stacks and queues</li>
	<li>What are list comprehensions and how to use them</li>
	<li>What are tuples and how to use them</li>
	<li>When to use tuples versus lists</li>
	<li>What is a sequence</li>
	<li>What is tuple packing</li>
	<li>What is sequence unpacking</li>
	<li>What is the <code>del</code> statement and how to use it</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/zIxzk5ChUX6KzhJIxJjf9Q" title="3.1.3. Lists" target="_blank">3.1.3. Lists</a> </li>
	<li><a href="/rltoken/ugotLwGPHgU1raKqco8TFg" title="Data structures" target="_blank">Data structures</a> (<em>until <code>5.3. Tuples and Sequences</code> included</em>)</li>
	<li><a href="/rltoken/smot10KJXMP-a84UxJ7WrQ" title="Learn to Program 6 : Lists" target="_blank">Learn to Program 6 : Lists</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-print_list_integer.py**:](#0-print_list_integerpy) Function that prints all integers of a list.
1.	[**1-element_at.py**:](#1-element_atpy) Function that retrieves an element from a list like in C.
2.	[**2-replace_in_list.py**:](#2-replace_in_listpy) Function that replaces an element of a list at a specific position (like in C).
3.	[**3-print_reversed_list_integer.py**:](#3-print_reversed_list_integerpy) Function that prints all integers of a list, in reverse order.
4.	[**4-new_in_list.py**:](#4-new_in_listpy) Function that replaces an element in a list at a specific position without modifying the original list (like in C).
5.	[**5-no_c.py**:](#5-no_cpy) Function that removes all characters <code>c</code> and <code>C</code> from a string.
6.	[**6-print_matrix_integer.py**:](#6-print_matrix_integerpy) Function that prints a matrix of integers.
7.	[**7-add_tuple.py**:](#7-add_tuplepy) Function that adds 2 tuples.
8.	[**8-multiple_returns.py**:](#8-multiple_returnspy) Function that returns a tuple with the length of a string and its first character.
9.	[**9-max_integer.py**:](#9-max_integerpy) Function that finds the biggest integer of a list. 
10.	[**10-divisible_by_2.py**:](#10-divisible_by_2py) Function that finds all multiples of 2 in a list.
11.	[**11-delete_at.py**:](#11-delete_atpy) Function that deletes the item at a specific position in a list.
12.	[**12-switch.py**:](#12-switchpy) Complete the source code in order to switch value of <code>a</code> and <code>b</code>
13.	[**13-is_palindrome.c, lists.h**:](#13-is_palindromec-listsh) <strong>Technical interview preparation</strong> Function in C that checks if a singly linked list is a palindrome.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-print_list_integer.py

**<p>Function that prints all integers of a list.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 1-element_at.py

**<p>Function that retrieves an element from a list like in C.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 2-replace_in_list.py

**<p>Function that replaces an element of a list at a specific position (like in C).</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 3-print_reversed_list_integer.py

**<p>Function that prints all integers of a list, in reverse order.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 4-new_in_list.py

**<p>Function that replaces an element in a list at a specific position without modifying the original list (like in C).</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 5-no_c.py

**<p>Function that removes all characters <code>c</code> and <code>C</code> from a string.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Holberton Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 6-print_matrix_integer.py

**<p>Function that prints a matrix of integers.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 7-add_tuple.py

**<p>Function that adds 2 tuples.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 8-multiple_returns.py

**<p>Function that returns a tuple with the length of a string and its first character.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 32 - First character: A
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 9-max_integer.py

**<p>Function that finds the biggest integer of a list. </p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 10-divisible_by_2.py

**<p>Function that finds all multiples of 2 in a list.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i &lt; len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 11-delete_at.py

**<p>Function that deletes the item at a specific position in a list.</p>**

<pre><code>guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
</code></pre>

### 12-switch.py

**<p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>**

<pre><code>guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
</code></pre>

### 13-is_palindrome.c, lists.h

**<p><strong>Technical interview preparation</strong> </p><p>Function in C that checks if a singly linked list is a palindrome.</p>**

<pre><code>carrie@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
carrie@ubuntu:0x03$
</code></pre>

