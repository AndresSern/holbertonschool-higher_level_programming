# 0x00. Python - Hello, World
In this directory you will learn how to use conditional if, and the while and for loop and differentiate each one

## GENERAL:

1.  Why Python programming is awesome
2.  Who created Python
3.  Who is Guido van Rossum
4.  Where does the name ‘Python’ come from
5.  What is the Zen of Python
6.  How to use the Python interpreter
7.  How to print text and variables using print
8.  How to use strings
9.  What are indexing and slicing in Python
10.  What is the official Holberton Python coding style and how to check your code with PEP 8

## Read or watch:

1.   **[The Python tutorial (only the first three chapters below):](https://docs.python.org/3.4/tutorial/index.html)**
     - **[Whetting Your Appetite:](https://docs.python.org/3.4/tutorial/appetite.html)**
     - **[Using the Python Interpreter:](https://docs.python.org/3.4/tutorial/interpreter.html)**
     - **[An Informal Introduction to Python:](https://docs.python.org/3.4/tutorial/introduction.html)**
2.   **[How To Use String Formatters in Python 3:](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)**
3.   **[Learn to Program:](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)**
4.   **[PEP 8 – Style Guide for Python Code:](https://www.python.org/dev/peps/pep-0008/)**


## Files:

1.  **0-run**: Write a Shell script that runs a Python script.
2.  **1-run_inline** : Write a Shell script that runs Python code.
3.  **2-print.py** : Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
4.  **3-print_number.py** : Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
5.  **4-print_float.py** : Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
6.  **5-print_string.py** : Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
7.  **6-concat.py** : Complete this source code to print Welcome to Holberton School!
8.  **7-edges.py** : Complete this source code
9.  **8-concat_edges.py** : Complete this source code to print object-oriented programming with Python, followed by a new line.
10.  **9-easter_egg.py** : Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
11.  **100-write.py** : Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.


## Tasks

### 0\. 0. Run Python file
*   File: **0-run**

*Write a Shell script that runs a Python script.*

1.  The Python file name will be saved in the environment variable $PYFILE

Example:
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$ 
```

### 1. Run inline
*   File: **1-run_inline**

*Write a Shell script that runs Python code.*

1.  The Python code will be saved in the environment variable $PYCODE

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Holberton School: 98
guillaume@ubuntu:~/py/0x00$ 
```

###  2. Hello, print 
*   File: ** 2-print.py**

*Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.*

1.  Use the function print

```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

###  3. Print integer 
*   File: **3-print_number.py**

*Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.*

1.  The output of the script should be
     - the number, followed by Battery street,
     - followed by a new line
2.  You are not allowed to cast the variable number into a string
3.  Your code must be 3 lines long
4.  You have to use the new print numbers tips (with .format(...))

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

###  4. Print float 
*   File: **4-print_float.py**

*Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.*

1.  The output of the program should be:
     - Float:, followed by the float with only 2 digits
     - followed by a new line
2.  You are not allowed to cast number to string
3.  You have to use the new print formatting tips (with .format(...))

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

###   5. Print string 
* File: **5-print\_numbers.c**
*Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.*

1.  The output of the program should be:
     - 3 times the value of str
     - followed by a new line
     - followed by the 9 first characters of str
     - followed by a new line
2.  You are not allowed to use any loops or conditional statement
3.  Your program should be maximum 5 lines long

```
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$  
```

### 6. Play with strings
*   File: **6-print\_numberz.c**

*Complete this source code to print Welcome to Holberton School!*

1. You are not allowed to use any loops or conditional statements.
2. You have to use the variables str1 and str2 in your new line of code
3. Your program should be exactly 5 lines long

```
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
```


### 7. Copy - Cut - Paste 
*   File: **7-edges.py**

*Complete this source code*

1.  You are not allowed to use any loops or conditional statements
2.  Your program should be exactly 8 lines long
3.  word_first_3 should contain the first 3 letters of the variable word
4.  word_last_2 should contain the last 2 letters of the variable word
5.  middle_word should contain the value of the variable word without the first and last letters

```
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
```

### 8. Create a new sentence 
*   File: **8-concat_edges.py**

*Complete this source code to print object-oriented programming with Python, followed by a new line.*

1.  You can find the source code here
2.  You are not allowed to use any loops or conditional statements
3.  Your program should be exactly 5 lines long
4.  You are not allowed to create new variables
5.  You are not allowed to use string literals

```
guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
```

###  9. Easter Egg 
*   File: **9-easter_egg.py**

*Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.*

1.   Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

```
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
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
```

### 11. Hello, write 
*   File: **10-print\_comb2.c**

*Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.*

1.   Use the function write from the sys module
2.   You are not allowed to use print
3.   Your script should print to stderr
4.   Your script should exit with the status code 1
5.   (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)

```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
```
