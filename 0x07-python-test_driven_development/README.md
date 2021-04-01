# 0x07. Python - Test-driven development

## GENERAL :open_book::open_book::open_book::

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
	<li><a href="/rltoken/alaT1C9CeCbkRKh-yjMRww" title="doctest — Test interactive Python examples" target="_blank">doctest — Test interactive Python examples</a> (<em>until “26.2.3.7. Warnings” included</em>)</li>
	<li><a href="/rltoken/cpEYbv_Z55QrSVRiuG5tUw" title="doctest – Testing through documentation" target="_blank">doctest – Testing through documentation</a> </li>
	<li><a href="/rltoken/CELicn3K8hODQsWZak_h0g" title="Unit Tests in Python" target="_blank">Unit Tests in Python</a></li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-add_integer.py, tests/0-add_integer.txt**:](#0-add_integerpy-tests0-add_integertxt) Function that adds 2 integers.
1.	[**2-matrix_divided.py, tests/2-matrix_divided.txt**:](#2-matrix_dividedpy-tests2-matrix_dividedtxt) Function that divides all elements of a matrix.Note you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
2.	[**3-say_my_name.py, tests/3-say_my_name.txt**:](#3-say_my_namepy-tests3-say_my_nametxt) Function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code>Note you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
3.	[**4-print_square.py, tests/4-print_square.txt**:](#4-print_squarepy-tests4-print_squaretxt) Function that prints a square with the character <code>#</code>.
4.	[**5-text_indentation.py, tests/5-text_indentation.txt**:](#5-text_indentationpy-tests5-text_indentationtxt) Function that prints a text with 2 new lines after each of these characters <code>.</code>, <code>?</code> and <code></code>
5.	[**tests/6-max_integer_test.py**:](#tests6-max_integer_testpy) Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.In this task, you will write unittests for the function <code>def max_integer(list=[])</code>.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-add_integer.py, tests/0-add_integer.txt

**<p>Function that adds 2 integers.</p>**

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

### 2-matrix_divided.py, tests/2-matrix_divided.txt

**<p>Function that divides all elements of a matrix.</p><p>Note you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>**

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

### 3-say_my_name.py, tests/3-say_my_name.txt

**<p>Function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p><p>Note you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>**

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

### 4-print_square.py, tests/4-print_square.txt

**<p>Function that prints a square with the character <code>#</code>.</p>**

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

### 5-text_indentation.py, tests/5-text_indentation.txt

**<p>Function that prints a text with 2 new lines after each of these characters <code>.</code>, <code>?</code> and <code></code></p>**

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

**<p>Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.</p><p>In this task, you will write unittests for the function <code>def max_integer(list=[])</code>.</p>**

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

