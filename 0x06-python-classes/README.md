# 0x06. Python - Classes and Objects

## GENERAL:

 <ol>
	<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
	<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
	<li>All your files should end with a new line</li>
	<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
	<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
	<li>Your code should use the <code>PEP 8</code> style (version 1.7)</li>
	<li>All your files must be executable</li>
	<li>The length of your files will be tested using <code>wc</code></li>
	<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
	<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
	<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
	<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/izl1kO1isRJo6h_Ce2pmhw" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, <code>classmethod</code> and <code>staticmethod</code> yet</em>)</li>
	<li><a href="/rltoken/K5t1QFchQYs7rkt62uMo7A" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please *</em>be careful*<em>: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The <code>__init__</code> Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”</em>)</li>
	<li><a href="/rltoken/LZg7XYGGZj49Gu2276afpA" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> </li>
	<li><a href="/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ" title="Learn to Program 9 : Object Oriented Programming" target="_blank">Learn to Program 9 : Object Oriented Programming</a> </li>
	<li><a href="/rltoken/CFTUXsxbTVu4xb698_2bmQ" title="Python Classes and Objects" target="_blank">Python Classes and Objects</a> </li>
	<li><a href="/rltoken/DK1vkIQ0xT1fmMrmBcSGiA" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> </li>
</ol>

## INTRODUCTION TO FILES:

0.	[**0-square.py**:](#0-squarepy) n empty class <code>Square</code> that defines a square:
1.	[**1-square.py**:](#1-squarepy)  class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)<strong>Why?</strong><em>Why <code>size</code> is private attribute?</em>The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.
2.	[**2-square.py**:](#2-squarepy)  class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)
3.	[**3-square.py**:](#3-squarepy)  class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)
4.	[**4-square.py**:](#4-squarepy)  class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)<strong>Why?</strong><em>Why a getter and setter?</em>Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
5.	[**5-square.py**:](#5-squarepy)  class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)
6.	[**6-square.py**:](#6-squarepy)  class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)
## FILES:

### 0-square.py

*<p>Write an empty class <code>Square</code> that defines a square:</p>*

<ul>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
&lt;class '0-square.Square'&gt;
{}
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 1-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)</p><p><strong>Why?</strong></p><p><em>Why <code>size</code> is private attribute?</em></p><p>The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.</p>*

<ul>
	<li>Private instance attribute: <code>size</code></li>
	<li>Instantiation with <code>size</code> (no type/value verification)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
&lt;class '1-square.Square'&gt;
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 2-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)</p>*

<ul>
	<li>Private instance attribute: <code>size</code></li>
	<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
&lt;class '2-square.Square'&gt;
{'_Square__size': 3}
&lt;class '2-square.Square'&gt;
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be &gt;= 0
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 3-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)</p>*

<ul>
	<li>Private instance attribute: <code>size</code></li>
	<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
	<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 4-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)</p><p><strong>Why?</strong></p><p><em>Why a getter and setter?</em></p><p>Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.</p>*

<ul>
	<li>Private instance attribute: <code>size</code>:

<ul>
	<li>property <code>def size(self):</code> to retrieve it</li>
	<li>property setter <code>def size(self, value):</code> to set it:

<ul>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
	<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
	<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 5-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>*

<ul>
	<li>Private instance attribute: <code>size</code>:

<ul>
	<li>property <code>def size(self):</code> to retrieve it</li>
	<li>property setter <code>def size(self, value):</code> to set it:

<ul>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
	<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
	<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
	<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
	<li>if <code>size</code> is equal to 0, print an empty line</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
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
--

--
guillaume@ubuntu:~/0x06$ 
</code></pre>

### 6-square.py

*<p>class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)</p>*

<ul>
	<li>Private instance attribute: <code>size</code>:

<ul>
	<li>property <code>def size(self):</code> to retrieve it</li>
	<li>property setter <code>def size(self, value):</code> to set it:

<ul>
	<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
	<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
	<li>Private instance attribute: <code>position</code>:

<ul>
	<li>property <code>def position(self):</code> to retrieve it</li>
	<li>property setter <code>def position(self, value):</code> to set it:

<ul>
	<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code><br></li>
</ul></li>
</ul></li>
	<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
	<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
	<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
	<li>if <code>size</code> is equal to 0, print an empty line</li>
	<li><code>position</code> should be use by using space - <strong>Don’t fill lines by spaces</strong> when <code>position[1] &gt; 0</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 
</code></pre>
