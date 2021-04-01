# 0x02. Python - import & modules

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>How to import functions from another file</li>
	<li>How to use imported functions</li>
	<li>How to create a module</li>
	<li>How to use the built-in function <code>dir()</code></li>
	<li>How to prevent code in your script from being executed when imported</li>
	<li>How to use command line arguments with your Python programs</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/hYag6ME71pOg2xkjqrLDdg" title="Modules" target="_blank">Modules</a> </li>
	<li><a href="/rltoken/CkqNLqqCuYsLbkCIVSKLWA" title="Command line arguments" target="_blank">Command line arguments</a> </li>
	<li><a href="/rltoken/XWzCcj9tvlC2IYjdNDiNAg" title="PEP 8 -- Style Guide for Python Code" target="_blank">PEP 8 – Style Guide for Python Code</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-add.py**:](#0-addpy) Program that imports the function <code>def add(a, b)</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code>
1.	[**1-calculation.py**:](#1-calculationpy) Program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.
2.	[**2-args.py**:](#2-argspy) Program that prints the number of and the list of its arguments.
3.	[**3-infinite_add.py**:](#3-infinite_addpy) Program that prints the result of the addition of all argumentsLast but not least, your program should also handle big numbers. And the good news is if your program works for the above example, it will work for the following exampleRemember how you did (or did not) do it in C? <code>#pythoniscool</code><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T010700Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=778d204afcda02812450165fdf61e1f89881ffecaf3b6e29bec6fcabf44c1cd2" alt="" style="">
4.	[**4-hidden_discovery.py**:](#4-hidden_discoverypy) Program that prints all the names defined by the compiled module <a href="https//github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc" title="hidden_4.pyc" target="_blank">hidden_4.pyc</a> (please download it locally).
5.	[**5-variable_load.py**:](#5-variable_loadpy) Program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.
6.	[**100-my_calculator.py**:](#100-my_calculatorpy) Program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.
7.	[**101-easy_print.py**:](#101-easy_printpy) Program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.
8.	[**102-magic_calculation.py**:](#102-magic_calculationpy) Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode
9.	[**103-fast_alphabet.py**:](#103-fast_alphabetpy) Program that prints the alphabet in uppercase, followed by a new line.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-add.py

**<p>Program that imports the function <code>def add(a, b)</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></p>**

<pre><code>guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 
</code></pre>

### 1-calculation.py

**<p>Program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$
</code></pre>

### 2-args.py

**<p>Program that prints the number of and the list of its arguments.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
guillaume@ubuntu:~/0x02$ 
</code></pre>

### 3-infinite_add.py

**<p>Program that prints the result of the addition of all arguments</p><p>Last but not least, your program should also handle big numbers. And the good news is if your program works for the above example, it will work for the following example</p><p>Remember how you did (or did not) do it in C? <code>#pythoniscool</code></p><p><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T010700Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=778d204afcda02812450165fdf61e1f89881ffecaf3b6e29bec6fcabf44c1cd2" alt="" style=""></p>**

<pre><code>guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 
</code></pre>

### 4-hidden_discovery.py

**<p>Program that prints all the names defined by the compiled module <a href="https//github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc" title="hidden_4.pyc" target="_blank">hidden_4.pyc</a> (please download it locally).</p>**

<pre><code>guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_holberton
print_school
guillaume@ubuntu:~/0x02$ 
</code></pre>

### 5-variable_load.py

**<p>Program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$
</code></pre>

### 100-my_calculator.py

**<p>Program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py &lt;a&gt; &lt;operator&gt; &lt;b&gt;
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
</code></pre>

### 101-easy_print.py

**<p>Program that prints <code>#pythoniscool</code>, followed by a new line, in the standard output.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/0x02$ 
</code></pre>

### 102-magic_calculation.py

**<p>Write the Python function <code>def magic_calculation(a, b)</code> that does exactly the same as the following Python bytecode</p>**

<pre><code>  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (&lt;)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        &gt;&gt;   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        &gt;&gt;   89 POP_BLOCK

  8     &gt;&gt;   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     &gt;&gt;   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
</code></pre>

### 103-fast_alphabet.py

**<p>Program that prints the alphabet in uppercase, followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/0x02$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
guillaume@ubuntu:~/0x02$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
guillaume@ubuntu:~/0x02$
</code></pre>

