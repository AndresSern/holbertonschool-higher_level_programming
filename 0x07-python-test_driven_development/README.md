# 0x07. Python - Test-driven development

## GENERAL:

 <ol>
	<li>Why Python programming is awesome</li>
	<li>What’s an interactive test</li>
	<li>Why tests are important</li>
	<li>How to write Docstrings to create tests</li>
	<li>How to write documentation for each module and function</li>
	<li>What are the basic option flags to create tests</li>
	<li>How to find edge cases</li>
</ol>

## RESOURCES:

 <ol>
	<li>Based on the requirements of each task, <strong>you should always write the documentation (module(s) + function(s)) and tests first</strong>, before you actually code anything</li>
	<li>The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases</li>
	<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case. <strong>But not in the implementation of them!</strong></li>
	<li><strong>Don’t trust the user</strong>, always think about all possible edge cases</li>
</ol>

## INTRODUCTION TO FILES:

0.	[**0-add_integer.py**:](#0-add_integerpy)  function that adds 2 integers.
1.	[**2-matrix_divided.py*:](#2-matrix_dividedpy)  function that divides all elements of a matrix.Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
2.	[**3-say_my_name.py**:](#3-say_my_namepy)  function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
3.	[**4-print_square.py**:](#4-print_squarepy)  function that prints a square with the character <code>#</code>.
4.	[**5-text_indentation.py**:](#5-text_indentationpy)  function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code>
5.	[**tests/6-max_integer_test.py**:](#tests/6-max_integer_testpy) Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.

## FILES:

### 0-add_integer.py

*<p>Function that adds 2 integers.</p>*

<ul>
	<li>Prototype: <code>def add_integer(a, b=98):</code></li>
	<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
	<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
	<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$ 
</code></pre>

### 2-matrix_divided.py

*<p>Function that divides all elements of a matrix.</p><p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>*

<ul>
	<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
	<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
	<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
	<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
	<li><code>div</code> can’t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
	<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
	<li>Returns a new matrix</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

### 3-say_my_name.py

*<p>Function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p><p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>*

<ul>
	<li>Prototype: <code>def say_my_name(first_name, last_name=""):</code></li>
	<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

### 4-print_square.py

*<p>Function that prints a square with the character <code>#</code>.</p>*

<ul>
	<li>Prototype: <code>def print_square(size):</code></li>
	<li><code>size</code> is the size length of the square</li>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
	<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be &gt;= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

### 5-text_indentation.py

*<p>Function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>*

<ul>
	<li>Prototype: <code>def text_indentation(text):</code></li>
	<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
	<li>There should be no space at the beginning or at the end of each printed line</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

### tests/6-max_integer_test.py

*<p>Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.</p><p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>*

<ul>
	<li>test file should be inside a folder <code>tests</code></li>
	<li>You have to use the <a href="/rltoken/qMqF1bBJXSAIjg8tugitHQ" title="unittest module" target="_blank">unittest module</a> </li>
	<li>test file should be python files (extension: <code>.py</code>)</li>
	<li>test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
	<li>All tests you make must be passable by the function below</li>
	<li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
</code></pre>
