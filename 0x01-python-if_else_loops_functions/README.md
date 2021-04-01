# 0x01. Python - if/else, loops, functions

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why Python programming is awesome</li>
	<li>Why indentation is so important in Python</li>
	<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
	<li>How to use comments</li>
	<li>How to affect values to variables</li>
	<li>How to use the <code>while</code> and <code>for</code> loops</li>
	<li>How is Python’s <code>for</code> different from <code>C</code>‘s?</li>
	<li>How to use the <code>break</code> and <code>continues</code> statements</li>
	<li>How to use <code>else</code> clauses on loops</li>
	<li>What does the <code>pass</code> statement do, and when to use it</li>
	<li>How to use <code>range</code></li>
	<li>What is a function and how do you use functions</li>
	<li>What does return a function that does not use any <code>return</code> statement</li>
	<li>Scope of variables</li>
	<li>What’s a traceback</li>
	<li>What are the arithmetic operators and how to use them</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/R7uTXYVOjUilq6rCjsQcFg" title="More Control Flow Tools" target="_blank">More Control Flow Tools</a> (<em>Read until “4.6. Defining Functions” included</em>)</li>
	<li><a href="/rltoken/Y-HaMMJBKPseiVDo_v9PVg" title="Myths about Indentation" target="_blank">Myths about Indentation</a> </li>
	<li><a href="/rltoken/AorC2VSZ4yCOx-AbatvKLA" title="IndentationError" target="_blank">IndentationError</a> </li>
	<li><a href="/rltoken/arGQeiwUbFn3JOoYpw84yA" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
	<li><a href="/rltoken/mlo-dauC8pSM_NrO5VYobw" title="Learn to Program" target="_blank">Learn to Program</a> </li>
	<li><a href="/rltoken/mlo-dauC8pSM_NrO5VYobw" title="Learn to Program 2 : Looping" target="_blank">Learn to Program 2 : Looping</a> </li>
	<li><a href="/rltoken/mq1IFaMhqpk2IHE0dC6UuQ" title="PEP 8 -- Style Guide for Python Code" target="_blank">PEP 8 – Style Guide for Python Code</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-positive_or_negative.py**:](#0-positive_or_negativepy) This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.
1.	[**1-last_digit.py**:](#1-last_digitpy) This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.
2.	[**2-print_alphabet.py**:](#2-print_alphabetpy) Program that prints the ASCII alphabet, in lowercase, not followed by a new line.
3.	[**3-print_alphabt.py**:](#3-print_alphabtpy) Program that prints the ASCII alphabet, in lowercase, not followed by a new line.
4.	[**4-print_hexa.py**:](#4-print_hexapy) Program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)
5.	[**5-print_comb2.py**:](#5-print_comb2py) Program that prints numbers from <code>0</code> to <code>99</code>.
6.	[**6-print_comb3.py**:](#6-print_comb3py) Program that prints all possible different combinations of two digits.
7.	[**7-islower.py**:](#7-islowerpy) Function that checks for lowercase character. 
8.	[**8-uppercase.py**:](#8-uppercasepy) Function that prints a string in uppercase followed by a new line.
9.	[**9-print_last_digit.py**:](#9-print_last_digitpy) Function that prints the last digit of a number.
10.	[**10-add.py**:](#10-addpy) Function that adds two integers and returns the result.
11.	[**11-pow.py**:](#11-powpy) Function that computes <code>a</code> to the power of <code>b</code> and return the value.
12.	[**12-fizzbuzz.py**:](#12-fizzbuzzpy) Function that prints the numbers from 1 to 100 separated by a space. 
13.	[**13-insert_number.c, lists.h**:](#13-insert_numberc-listsh) <strong>Technical interview preparation</strong> Function in C that inserts a number into a sorted singly linked list.
14.	[**100-print_tebahpla.py**:](#100-print_tebahplapy) Program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and <code>Y</code> in uppercase) , not followed by a new line.
15.	[**101-remove_char_at.py**:](#101-remove_char_atpy) Function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the “C array index”).
16.	[**102-magic_calculation.py**:](#102-magic_calculationpy) Write the Python function <code>def magic_calculation(a, b, c)</code> that does exactly the same as the following Python bytecode<a href="/rltoken/k56wUejC7YSyV7C8LDQGnA" title="tips - ByteCode" target="_blank">tips - ByteCode</a>

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-positive_or_negative.py

**<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 1-last_digit.py

**<p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 2-print_alphabet.py

**<p>Program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
</code></pre>

### 3-print_alphabt.py

**<p>Program that prints the ASCII alphabet, in lowercase, not followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
</code></pre>

### 4-print_hexa.py

**<p>Program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
</code></pre>

### 5-print_comb2.py

**<p>Program that prints numbers from <code>0</code> to <code>99</code>.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 6-print_comb3.py

**<p>Program that prints all possible different combinations of two digits.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 7-islower.py

**<p>Function that checks for lowercase character. </p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 8-uppercase.py

**<p>Function that prints a string in uppercase followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton School 98 Battery street")

guillaume@ubuntu:~/0x01$ ./8-main.py
HOLBERTON
HOLBERTON SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 9-print_last_digit.py

**<p>Function that prints the last digit of a number.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 10-add.py

**<p>Function that adds two integers and returns the result.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 11-pow.py

**<p>Function that computes <code>a</code> to the power of <code>b</code> and return the value.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/0x01$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 12-fizzbuzz.py

**<p>Function that prints the numbers from 1 to 100 separated by a space. </p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 13-insert_number.c, lists.h

**<p><strong>Technical interview preparation</strong> </p><p>Function in C that inserts a number into a sorted singly linked list.</p>**

<pre><code>carrie@ubuntu:0x01$ cat lists.h 
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

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
</code></pre>

### 100-print_tebahpla.py

**<p>Program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and <code>Y</code> in uppercase) , not followed by a new line.</p>**

<pre><code>guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
</code></pre>

### 101-remove_char_at.py

**<p>Function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the “C array index”).</p>**

<pre><code>guillaume@ubuntu:~/0x01$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

guillaume@ubuntu:~/0x01$ ./101-main.py
Holerton School
Chcago
 is fun!
School
Python
guillaume@ubuntu:~/0x01$ 
</code></pre>

### 102-magic_calculation.py

**<p>Write the Python function <code>def magic_calculation(a, b, c)</code> that does exactly the same as the following Python bytecode</p><p><a href="/rltoken/k56wUejC7YSyV7C8LDQGnA" title="tips - ByteCode" target="_blank">tips - ByteCode</a></p>**

<pre><code>  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (&lt;)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     &gt;&gt;   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (&gt;)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     &gt;&gt;   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
</code></pre>

