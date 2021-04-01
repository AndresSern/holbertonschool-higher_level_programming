# 0x00. Python - Hello, World

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>Who created Python</li>
	<li>Who is Guido van Rossum</li>
	<li>Where does the name ‘Python’ come from</li>
	<li>What is the Zen of Python</li>
	<li>How to use the Python interpreter</li>
	<li>How to print text and variables using <code>print</code></li>
	<li>How to use strings</li>
	<li>What are indexing and slicing in Python</li>
	<li>What is the official Holberton Python coding style and how to check your code with <code>PEP 8</code></li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/fX5geNeDFcCtootbB_MqCQ" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>only the first three chapters below</em>)

<ol>
	<li><a href="/rltoken/JnsZOCXrWDkZn6iMo1uuFg" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
	<li><a href="/rltoken/AejXr_G-d8CSITEtpvwpRg" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
	<li><a href="/rltoken/lUBuPMNcox9EqJ1Q3oVesQ" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until “3.1.2. Strings” included</em>)</li>
</ol></li>
	<li><a href="/rltoken/z6mk3Yep2tJVSF6KsBAYrg" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
	<li><a href="/rltoken/gYgGXOth8N16KjUpXgO1uQ" title="Learn to Program" target="_blank">Learn to Program</a> </li>
	<li><a href="/rltoken/BMIjFOY7HvWHSjHfNrkzPg" title="PEP 8 -- Style Guide for Python Code" target="_blank">PEP 8 – Style Guide for Python Code</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-run**:](#0-run) Shell script that runs a Python script.The Python file name will be saved in the environment variable <code>$PYFILE</code>
1.	[**1-run_inline**:](#1-run_inline) Shell script that runs Python code.The Python code will be saved in the environment variable <code>$PYCODE</code>
2.	[**2-print.py**:](#2-printpy) Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.
3.	[**3-print_number.py**:](#3-print_numberpy) Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="source code" target="_blank">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.
4.	[**4-print_float.py**:](#4-print_floatpy) Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.
5.	[**5-print_string.py**:](#5-print_stringpy) Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="source code" target="_blank">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.
6.	[**6-concat.py**:](#6-concatpy) Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="source code" target="_blank">source code</a> to print <code>Welcome to Holberton School!</code>
7.	[**7-edges.py**:](#7-edgespy) Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="source code" target="_blank">source code</a>
8.	[**8-concat_edges.py**:](#8-concat_edgespy) Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="source code" target="_blank">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.
9.	[**9-easter_egg.py**:](#9-easter_eggpy) Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
10.	[**10-check_cycle.c, lists.h**:](#10-check_cyclec-listsh) <strong>Technical interview preparation</strong> Function in C that checks if a singly linked list has a cycle in it.Requirements
11.	[**100-write.py**:](#100-writepy) Python script that prints exactly <code>and that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.
12.	[**101-compile**:](#101-compile) Script that compiles a Python script file.The Python file name will be stored in the environment variable <code>$PYFILE</code>The output filename has to be <code>$PYFILEc</code> (ex <code>export PYFILE=my_main.py</code> =&gt; output filename <code>my_main.pyc</code>)
13.	[**102-magic_calculation.py**:](#102-magic_calculationpy) Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-run

**<p>Shell script that runs a Python script.</p><p>The Python file name will be saved in the environment variable <code>$PYFILE</code></p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 1-run_inline

**<p>Shell script that runs Python code.</p><p>The Python code will be saved in the environment variable <code>$PYCODE</code></p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Holberton School: 98
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 2-print.py

**<p>Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
</code></pre>

### 3-print_number.py

**<p>Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" title="source code" target="_blank">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 4-print_float.py

**<p>Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 5-print_string.py

**<p>Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" title="source code" target="_blank">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 6-concat.py

**<p>Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/6-concat.py" title="source code" target="_blank">source code</a> to print <code>Welcome to Holberton School!</code></p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 7-edges.py

**<p>Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/7-edges.py" title="source code" target="_blank">source code</a></p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 8-concat_edges.py

**<p>Complete this <a href="https//github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" title="source code" target="_blank">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 9-easter_egg.py

**<p>Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
</code></pre>

### 10-check_cycle.c, lists.h

**<p><strong>Technical interview preparation</strong> </p><p>Function in C that checks if a singly linked list has a cycle in it.</p><p>Requirements</p>**

<pre><code>carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include &lt;stdlib.h&gt;

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
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
</code></pre>

### 100-write.py

**<p>Python script that prints exactly <code>and that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2&gt; q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 101-compile

**<p>Script that compiles a Python script file.</p><p>The Python file name will be stored in the environment variable <code>$PYFILE</code></p><p>The output filename has to be <code>$PYFILEc</code> (ex <code>export PYFILE=my_main.py</code> =&gt; output filename <code>my_main.pyc</code>)</p>**

<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Holberton School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT =&gt; CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

### 102-magic_calculation.py

**<p>Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode</p>**

<pre><code>  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
</code></pre>

