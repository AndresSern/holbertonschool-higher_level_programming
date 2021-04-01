# 0x08. Python - More Classes and Objects

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome </li>
	<li>What is OOP</li>
	<li>“first-class everything”</li>
	<li>What is a class</li>
	<li>What is an object and an instance</li>
	<li>What is the difference between a class and an object or instance</li>
	<li>What is an attribute</li>
	<li>What are and how to use public, protected and private attributes</li>
	<li>What is <code>self</code></li>
	<li>What is a method</li>
	<li>What is the special <code>__init__</code> method and how to use it</li>
	<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
	<li>What is a property</li>
	<li>What is the difference between an attribute and a property in Python</li>
	<li>What is the Pythonic way to write getters and setters in Python</li>
	<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
	<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
	<li>What is a class attribute</li>
	<li>What is the difference between a object attribute and a class attribute</li>
	<li>What is a class method</li>
	<li>What is a static method</li>
	<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
	<li>How to bind attributes to object and classes</li>
	<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
	<li>How does Python find the attributes of an object or class</li>
	<li>How to use the <code>getattr</code> function</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/VlISluyXK-teEwwPCu2tlg" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph “Inheritance” (excluded)</em>)</li>
	<li><a href="/rltoken/m_oP4NCbKTp9tKptvxWP_g" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The <code>__init__</code> Method,”  “Data Abstraction, Data Encapsulation, and Information Hiding,” “<code>__str__</code>- and <code>__repr__</code>-Methods,” “Public- Protected- and Private Attributes,” &amp; “Destructor”</em>)</li>
	<li><a href="/rltoken/yRdxqVWRyGiu38i6oB4m4g" title="Class and Instance Attributes" target="_blank">Class and Instance Attributes</a> </li>
	<li><a href="/rltoken/ce7aZMwzugNBFgfYxNxwCw" title="classmethods and staticmethods" target="_blank">classmethods and staticmethods</a> </li>
	<li><a href="/rltoken/PVFV8ka_Ii6h2rXBqAliMQ" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> (<em>Mainly the last part “Public instead of Private Attributes”</em>)</li>
	<li><a href="/rltoken/eYiDVsmlNHRZTrirAZ7Qtg" title="str vs repr" target="_blank">str vs repr</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-rectangle.py**:](#0-rectanglepy) An empty class <code>Rectangle</code> that defines a rectangle
1.	[**1-rectangle.py**:](#1-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>0-rectangle.py</code>)
2.	[**2-rectangle.py**:](#2-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>1-rectangle.py</code>)
3.	[**3-rectangle.py**:](#3-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>2-rectangle.py</code>)<strong>Object address can be different</strong>
4.	[**4-rectangle.py**:](#4-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>3-rectangle.py</code>)
5.	[**5-rectangle.py**:](#5-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>4-rectangle.py</code>)
6.	[**6-rectangle.py**:](#6-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>5-rectangle.py</code>)
7.	[**7-rectangle.py**:](#7-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>6-rectangle.py</code>)
8.	[**8-rectangle.py**:](#8-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>7-rectangle.py</code>)
9.	[**9-rectangle.py**:](#9-rectanglepy) Class <code>Rectangle</code> that defines a rectangle by (based on <code>8-rectangle.py</code>)

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-rectangle.py

**<p>An empty class <code>Rectangle</code> that defines a rectangle</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
&lt;class '0-rectangle.Rectangle'&gt;
{}
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 1-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>0-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 2-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>1-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 3-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>2-rectangle.py</code>)</p><p><strong>Object address can be different</strong></p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
--
##########
##########
##########
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 4-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>3-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 5-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>4-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 6-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>5-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 7-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>6-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&amp;"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 8-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>7-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

### 9-rectangle.py

**<p>Class <code>Rectangle</code> that defines a rectangle by (based on <code>8-rectangle.py</code>)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

