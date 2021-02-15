# 0x00. Python - Hello, World
In this directory you will learn how to use conditional if, and the while and for loop and differentiate each one

## GENERAL:
1.  Why Python programming is awesome 
2.  Why indentation is so important in Python
3.  How to use the if, if ... else statements
4.  How to use comments
5.  How to affect values to variables
6.  How to use the while and for loops
7.  How is Pythons for different from Cs?
8.  How to use the break and continues statements
9.  How to use else clauses on loops
10.  What does the pass statement do, and when to use it
11.  How to use range
12.  What is a function and how do you use functions
13.  What does return a function that does not use any return statement
14.  Scope of variables
15.  Whats a traceback
16.  What are the arithmetic operators and how to use them

## Read or watch:

1.   **[More Control Flow Tools:](https://docs.python.org/3.4/tutorial/controlflow.html)**
2.   **[Myths about Indentation:](https://files.meetup.com/1544869/Python%20Indentation%20Myths.pdf)**
3.   **[IndentationError:](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)** 
4.   **[How To Use String Formatters in Python 3:](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)**
5.   **[Learn to Program:](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)**
6.   **[Learn to Program 2 : Looping:](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)**
7.   **[PEP 8  Style Guide for Python Code:](https://www.python.org/dev/peps/pep-0008/)**

## Files:

1.  **0-positive_or_negative.py**
2.  **1-last_digit.py**
3.  **2-print_alphabet.py**
4.  **3-print_alphabt.py**
5.  **4-print_hexa.py**
6.  **5-print_comb2.py**
7.  **6-print_comb3.py**
8.  **7-islower.py**
9.  **8-uppercase.py**
10.  **9-print_last_digit.py**
11.  **10-add.py**
12.  **12-fizzbuzz.py**
13.  **100-print_tebahpla.py**
14.  **101-remove_char_at.py**

## Tasks

### 0. Positive anything is better than negative nothing
*   File: **0-positive_or_negative.py**

*This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.*

1.    This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.
2.    You don’t have to understand what import, random. randint do. Please do not touch this code
3.    You don’t have to understand what import, random. randint do. Please do not touch this code
      -  The number, followed by
            - if the number is greater than 0: is positive
            - if the number is 0: is zero
            - if the number is less than 0: is negative
      - followed by a new line 

Example:

```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
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
```
### 1. The last digit 
*   File: **1-last_digit.py**

*This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.*

1.    The variable number will store a different value every time you will run this program
2.    You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)

3.    The output of the program should be:
      -  The string Last digit of, followed by
      -  the number, followed by
      -  the string is, followed by the last digit of number, followed by
            - if the last digit is greater than 5: the string and is greater than 5
            - f the last digit is 0: the string and is 0
            - if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
      - followed by a new line 

```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
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
```

###  2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game 
*   File: **2-print_alphabet.py**

*Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.*

1.    You can only use one print function with string format
2.    You can only use one loop in your code
3.    You are not allowed to store characters in a variable
4.    You are not allowed to import any module
  
```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

###  3. When I was having that alphabet soup, I never thought that it would pay off
*   File: **3-print_alphabt.py**

*Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.*

1.  Print all the letters except q and e
2.  You can only use one print function with string format
3.  You can only use one loop in your code
4.  You are not allowed to store characters in a variable
5.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
```

###  4. Hexadecimal printing 
*   File: **4-print_hexa.py**

*Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)*

1.  You can only use one print function with string format
2.  You can only use one loop in your code
3.  You are not allowed to store numbers or strings in a variable
4.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
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
```

###   5. 00...99
* File: **5-print_comb2.py**
*Write a program that prints numbers from 0 to 99.*

1.  Numbers must be separated by ,, followed by a space
2.  Numbers should be printed in ascending order, with two digits
3.  The last number should be followed by a new line
4.  You can only use no more than 2 print functions with string format
5.  You can only use one loop in your code
6.  You are not allowed to store numbers or strings in a variable
7.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$ 
```

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need 
*   File: **6-print_comb3.py**

*Write a program that prints all possible different combinations of two digits.*

1.  Numbers must be separated by ,, followed by a space
2.  The two digits must be different
3.  01 and 10 are considered the same combination of the two digits 0 and 1
4.  Print only the smallest combination of two digits
5.  Numbers should be printed in ascending order, with two digits
6.  The last number should be followed by a new line
7.  You can only use no more than 3 print functions with string format
8.  You can only use no more than 2 loops in your code
9.  You are not allowed to store numbers or strings in a variable
10.  You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```


### 7. islower
*   File: **7-islower.py** 

*Write a function that checks for lowercase character.*

1.  Prototype: def islower(c):
2.  Returns True if c is lowercase
3.  Returns False otherwise
4.  You are not allowed to import any module
5.  You are not allowed to use str.upper() and str.isupper()
6.  Tips: ord()

```
guillaume@ubuntu:~/0x01$ cat 7-main.py
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
```

### 8. To uppercase 
*   File: **8-uppercase.py**

*Write a function that prints a string in uppercase followed by a new line.*

1.    Prototype: def uppercase(str):
2.    You can only use no more than 2 print functions with string format
3.    You can only use one loop in your code
4.    You are not allowed to import any module
5.    You are not allowed to use str.upper() and str.isupper()
6.    Tips: ord()
  
```
guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton School 98 Battery street")

guillaume@ubuntu:~/0x01$ ./8-main.py
HOLBERTON
HOLBERTON SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$ 
```

###  9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important 
*   File: **9-print_last_digit.py**

*Write a function that prints the last digit of a number.*

1.  Prototype: def print_last_digit(number):
2.  Returns the value of the last digit
3.  You are not allowed to import any module 
  
```
guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$ 
```

### 10. a + b 
*   File: **10-add.py**

*Write a function that adds two integers and returns the result.* 

1.   Prototype: def add(a, b):
2.   Returns the value of a + b
3.   You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ cat 10-main.py
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
```

### 11. a ^ b 
*   File: **11-pow.py**

*Write a function that computes a to the power of b and return the value.* 
 
1.   Prototype: def pow(a, b):
2.   Returns the value of a ^ b
3.   You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ cat 11-main.py
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
```

### 12. Fizz Buzz 
*   File: **12-fizzbuzz.py**

*Write a function that prints the numbers from 1 to 100 separated by a space.* 

1.    For multiples of three print Fizz instead of the number and for multiples of five print 6.    Buzz.
2.    For numbers which are multiples of both three and five print FizzBuzz.
3.    Prototype: def fizzbuzz():
4.    Each element should be followed by a space
5.    You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
guillaume@ubuntu:~/0x01$ 
```

### 14. Smile in the mirror 
*   File: **100-print_tebahpla.py**

*Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.* 

1.    You can only use one print function with string format
2.    You can only use one loop in your code
3.    You are not allowed to store characters in a variable
4.    You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
```
