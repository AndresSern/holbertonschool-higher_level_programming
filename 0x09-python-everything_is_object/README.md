# 0x09. Python - Everything is object

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>What is an object</li>
	<li>What is the difference between a class and an object or instance</li>
	<li>What is the difference between immutable object and mutable object</li>
	<li>What is a reference</li>
	<li>What is an assignment</li>
	<li>What is an alias</li>
	<li>How to know if two variables are identical</li>
	<li>How to know if two variables are linked to the same object</li>
	<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
	<li>What is mutable and immutable</li>
	<li>What are the built-in mutable types</li>
	<li>What are the built-in immutable types</li>
	<li>How does Python pass variables to functions</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/n1x09X-KJSllpJkJorBw2A" title="9.10. Objects and values" target="_blank">9.10. Objects and values</a> </li>
	<li><a href="/rltoken/3teQMNNfDeyGvCtZfjsf5g" title="9.11. Aliasing" target="_blank">9.11. Aliasing</a> </li>
	<li><a href="/rltoken/JuPVygeoG27Q_qKxB2lP8g" title="Immutable vs mutable types" target="_blank">Immutable vs mutable types</a> </li>
	<li><a href="/rltoken/UbL96sV3cIxewdQPW_zwRw" title="Mutation" target="_blank">Mutation</a> (<em>Only this chapter</em>)</li>
	<li><a href="/rltoken/-t_1VsmKlgWHszL5y1YiKA" title="9.12. Cloning lists" target="_blank">9.12. Cloning lists</a> </li>
	<li><a href="/rltoken/IdBAdTYNLuS3YpRRQIam6Q" title="Python tuples: immutable but potentially changing" target="_blank">Python tuples: immutable but potentially changing</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-answer.txt**:](#0-answertxt) What function would you use to print the type of an object?Write the name of the function in the file, without <code>()</code>.
1.	[**1-answer.txt**:](#1-answertxt) How do you get the variable identifier (which is the memory address in the CPython implementation)?Write the name of the function in the file, without <code>()</code>.
2.	[**2-answer.txt**:](#2-answertxt) In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.
3.	[**3-answer.txt**:](#3-answertxt) In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.
4.	[**4-answer.txt**:](#4-answertxt) In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.
5.	[**5-answer.txt**:](#5-answertxt) In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.
6.	[**6-answer.txt**:](#6-answertxt) What do these 3 lines print?
7.	[**7-answer.txt**:](#7-answertxt) What do these 3 lines print?
8.	[**8-answer.txt**:](#8-answertxt) What do these 3 lines print?
9.	[**9-answer.txt**:](#9-answertxt) What do these 3 lines print?
10.	[**10-answer.txt**:](#10-answertxt) What do these 3 lines print?
11.	[**11-answer.txt**:](#11-answertxt) What do these 3 lines print?
12.	[**12-answer.txt**:](#12-answertxt) What do these 3 lines print?
13.	[**13-answer.txt**:](#13-answertxt) What do these 3 lines print?
14.	[**14-answer.txt**:](#14-answertxt) What does this script print?
15.	[**15-answer.txt**:](#15-answertxt) What does this script print?
16.	[**16-answer.txt**:](#16-answertxt) What does this script print?
17.	[**17-answer.txt**:](#17-answertxt) What does this script print?
18.	[**18-answer.txt**:](#18-answertxt) What does this script print?
19.	[**20-answer.txt**:](#20-answertxt) Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.
20.	[**21-answer.txt**:](#21-answertxt) Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.
21.	[**22-answer.txt**:](#22-answertxt) Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.
22.	[**23-answer.txt**:](#23-answertxt) Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.
23.	[**24-answer.txt**:](#24-answertxt) What does this script print?
24.	[**25-answer.txt**:](#25-answertxt) What does this script print?
25.	[**26-answer.txt**:](#26-answertxt) What does this script print?
26.	[**27-answer.txt**:](#27-answertxt) Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.
27.	[**28-answer.txt**:](#28-answertxt) Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.
28.	[**100-magic_string.py**:](#100-magic_stringpy) Function <code>magic_string()</code> that returns a string “Holberton” n times the number of the iteration (see code)
29.	[**101-locked_class.py**:](#101-locked_classpy) Class <code>LockedClass</code> with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called <code>first_name</code>.
30.	[**103-line1.txt, 103-line2.txt**:](#103-line1txt-103-line2txt) Assuming we are using a CPython implementation of Python3 with default options/configuration
31.	[**104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt**:](#104-line1txt-104-line2txt-104-line3txt-104-line4txt-104-line5txt) Assuming we are using a CPython implementation of Python3 with default options/configuration
32.	[**105-line1.txt**:](#105-line1txt) Assuming we are using a CPython implementation of Python3 with default options/configurationHint <code>NSMALLPOSINTS</code>, <code>NSMALLNEGINTS</code><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/70f9ea0e969dfcc407a7427aba4786d87a920494.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T012356Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=607ab6716ff4756788e8140ff63f28aff3bec5bce126e399458b0e5adfda4f93" alt="" style="">
33.	[**106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt**:](#106-line1txt-106-line2txt-106-line3txt-106-line4txt-106-line5txt) Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word)

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-answer.txt

**<p>What function would you use to print the type of an object?</p><p>Write the name of the function in the file, without <code>()</code>.</p>**

None

### 1-answer.txt

**<p>How do you get the variable identifier (which is the memory address in the CPython implementation)?</p><p>Write the name of the function in the file, without <code>()</code>.</p>**

None

### 2-answer.txt

**<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 100
</code></pre>

### 3-answer.txt

**<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 89
</code></pre>

### 4-answer.txt

**<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a
</code></pre>

### 5-answer.txt

**<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a + 1
</code></pre>

### 6-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; s1 = "Holberton"
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

### 7-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; s1 = "Holberton"
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

### 8-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; s1 = "Holberton"
&gt;&gt;&gt; s2 = "Holberton"
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

### 9-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; s1 = "Holberton"
&gt;&gt;&gt; s2 = "Holberton"
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

### 10-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

### 11-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

### 12-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

### 13-answer.txt

**<p>What do these 3 lines print?</p>**

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

### 14-answer.txt

**<p>What does this script print?</p>**

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</code></pre>

### 15-answer.txt

**<p>What does this script print?</p>**

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</code></pre>

### 16-answer.txt

**<p>What does this script print?</p>**

<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</code></pre>

### 17-answer.txt

**<p>What does this script print?</p>**

<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</code></pre>

### 18-answer.txt

**<p>What does this script print?</p>**

<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</code></pre>

### 20-answer.txt

**<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>a = ()
</code></pre>

### 21-answer.txt

**<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>a = (1, 2)
</code></pre>

### 22-answer.txt

**<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>a = (1)
</code></pre>

### 23-answer.txt

**<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>a = (1, )
</code></pre>

### 24-answer.txt

**<p>What does this script print?</p>**

<pre><code>a = (1)
b = (1)
a is b
</code></pre>

### 25-answer.txt

**<p>What does this script print?</p>**

<pre><code>a = (1, 2)
b = (1, 2)
a is b
</code></pre>

### 26-answer.txt

**<p>What does this script print?</p>**

<pre><code>a = ()
b = ()
a is b
</code></pre>

### 27-answer.txt

**<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; id(a)
139926795932424
&gt;&gt;&gt; a
[1, 2, 3, 4]
&gt;&gt;&gt; a = a + [5]
&gt;&gt;&gt; id(a)
</code></pre>

### 28-answer.txt

**<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>**

<pre><code>&gt;&gt;&gt; a
[1, 2, 3]
&gt;&gt;&gt; id (a)
139926795932424
&gt;&gt;&gt; a += [4]
&gt;&gt;&gt; id(a)
</code></pre>

### 100-magic_string.py

**<p>Function <code>magic_string()</code> that returns a string “Holberton” n times the number of the iteration (see code)</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
Holberton$
Holberton, Holberton$
Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
</code></pre>

### 101-locked_class.py

**<p>Class <code>LockedClass</code> with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called <code>first_name</code>.</p><p></p>**

<pre><code>guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
</code></pre>

### 103-line1.txt, 103-line2.txt

**<p>Assuming we are using a CPython implementation of Python3 with default options/configuration</p>**

<pre><code>julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
</code></pre>

### 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt

**<p>Assuming we are using a CPython implementation of Python3 with default options/configuration</p>**

<pre><code>julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
</code></pre>

### 105-line1.txt

**<p>Assuming we are using a CPython implementation of Python3 with default options/configuration</p><p>Hint <code>NSMALLPOSINTS</code>, <code>NSMALLNEGINTS</code></p><p><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/70f9ea0e969dfcc407a7427aba4786d87a920494.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T012356Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=607ab6716ff4756788e8140ff63f28aff3bec5bce126e399458b0e5adfda4f93" alt="" style=""></p>**

<pre><code>julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
</code></pre>

### 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt

**<p>Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word)</p>**

<pre><code>guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$ 
</code></pre>

