# 0x05. Python - Exceptions

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome </li>
	<li>What’s the difference between errors and exceptions</li>
	<li>What are exceptions and how to use them</li>
	<li>When do we need to use exceptions</li>
	<li>How to correctly handle an exception</li>
	<li>What’s the purpose of catching exceptions</li>
	<li>How to raise a builtin exception</li>
	<li>When do we need to implement a clean-up action after an exception</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/IvW-V19TlPbmMnVTHNllUg" title="Errors and Exceptions" target="_blank">Errors and Exceptions</a> </li>
	<li><a href="/rltoken/uHg99jd88sVrhuGUDfwT8g" title="Learn to Program 11 Static &amp; Exception Handling" target="_blank">Learn to Program 11 Static &amp; Exception Handling</a> (<em>starting at minute 7</em>)</li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-safe_print_list.py**:](#0-safe_print_listpy) Function that prints <code>x</code> elements of a list.
1.	[**1-safe_print_integer.py**:](#1-safe_print_integerpy) Function that prints an integer with <code>"{d}".format()</code>.
2.	[**2-safe_print_list_integers.py**:](#2-safe_print_list_integerspy) Function that prints the first <code>x</code> elements of a list and only integers.
3.	[**3-safe_print_division.py**:](#3-safe_print_divisionpy) Function that divides 2 integers and prints the result.
4.	[**4-list_division.py**:](#4-list_divisionpy) Function that divides element by element 2 lists.
5.	[**5-raise_exception.py**:](#5-raise_exceptionpy) Function that raises a type exception.
6.	[**6-raise_exception_msg.py**:](#6-raise_exception_msgpy) Function that raises a name exception with a message.
7.	[**100-safe_print_integer_err.py**:](#100-safe_print_integer_errpy) Function that prints an integer.
8.	[**102-magic_calculation.py**:](#102-magic_calculationpy) Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-safe_print_list.py

**<p>Function that prints <code>x</code> elements of a list.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 1-safe_print_integer.py

**<p>Function that prints an integer with <code>"{d}".format()</code>.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
Holberton is not an integer
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 2-safe_print_list_integers.py

**<p>Function that prints the first <code>x</code> elements of a list and only integers.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in &lt;module&gt;
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 3-safe_print_division.py

**<p>Function that divides 2 integers and prints the result.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 4-list_division.py

**<p>Function that divides element by element 2 lists.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 5-raise_exception.py

**<p>Function that raises a type exception.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 6-raise_exception_msg.py

**<p>Function that raises a name exception with a message.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 100-safe_print_integer_err.py

**<p>Function that prints an integer.</p>**

<pre><code>guillaume@ubuntu:~/0x05$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/0x05$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
Holberton is not an integer
guillaume@ubuntu:~/0x05$ ./100-main.py 2&gt; /dev/null
89
-89
Holberton is not an integer
guillaume@ubuntu:~/0x05$ 
</code></pre>

### 102-magic_calculation.py

**<p>Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode</p>**

<pre><code>  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        &gt;&gt;   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (&gt;)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     &gt;&gt;   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        &gt;&gt;   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     &gt;&gt;   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        &gt;&gt;  102 POP_BLOCK

 13     &gt;&gt;  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
</code></pre>

