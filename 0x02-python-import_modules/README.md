# 0x02. Python - import & modules
In this directory you will learn how import functions and global variables of the other file or import libraries the python

## GENERAL:
1.    Why Python programming is awesome  
2.    How to import functions from another file
3.    How to use imported functions
4.    How to create a module
5.    How to use the built-in function dir()
6.    How to prevent code in your script from being executed when imported
7.    How to use command line arguments with your Python programs

## Read or watch:

1.    Modules: **https://docs.python.org/3.4/tutorial/modules.html**
2.    Command line arguments: **https://docs.python.org/3.4/tutorial/stdlib.html#command-line-arguments**
3.    PEP 8 – Style Guide for Python Code: **https://www.python.org/dev/peps/pep-0008/** 

## Files:

1.  **0-add.py**
2.  **1-calculation.py**
3.  **2-args.py**
4.  **3-infinite_add.py**
5.  **4-hidden_discovery.py**
6.  **5-variable_load.py**
7.  **100-my_calculator.py**
8.  **101-easy_print.py**
9.  **103-fast_alphabet.py**

## Tasks

### 0. Import a simple function from a simple file 
*   File: **0-add.py**

*Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3*

1.   You have to use print function with string format to display integers
2.   You have to assign: 
     -  the value 1 to a variable called a
     -  the value 2 to a variable called b
     -  and use those two variables as arguments when calling the functions add and print
3.   a and b must be defined in 2 different lines: a = 1 and another b = 2 
4.   Your program should print: \<a value\> + \<b value\> = <add(a, b) value> followed with a new line 
5.   You can only use the word add_0 once in your code
6.   You are not allowed to use * for importing or __import__
7.   Your code should not be executed when imported - by using __import__, like the example below 


Example:

```
guillaume@ubuntu:~/0x02$ cat add_0.py
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
```

### 1. My first toolbox! 
*   File: **1-calculation.py**

*Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.*

1.   Do not use the function print (with string format to display integers) more than 4 times
2.   You have to define:
     - the value 10 to a variable a
     - the value 5 to a variable b
     - and use those two variables only, as arguments when calling functions (including print)
3.   a and b must be defined in 2 different lines: a = 10 and another b = 5
4.   Your program should call each of the imported functions. See example below for format
5.   The word calculator_1 should be used only once in your file
6.   You are not allowed to use * for importing or __import__
7.   Your code should not be executed when imported 

```
guillaume@ubuntu:~/0x02$ cat calculator_1.py
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
```

###  2. How to make a script dynamic!
*   File: **2-args.py**

*Write a program that prints the number of and the list of its arguments.*

1.   The output should be:
     - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
     - : (or . if no arguments were passed) followed by
     - a new line, followed by (if at least one argument),
     - one line per argument:
          - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
2.   Your code should not be executed when imported
3.   The number of elements of argv can be retrieved by using: len(argv)
3.   You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

```
guillaume@ubuntu:~/0x02$ ./2-args.py 
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
```

###  3. Infinite addition
*   File: **3-infinite_add.py**

*Write a program that prints the result of the addition of all arguments*

1.   The output should be the result of the addition of all arguments, followed by a new line
2.   You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
3.   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 
```

###  4. Who are you? 
*   File: **4-hidden_discovery.py**

*Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).*

1.   You should print one name per line, in alpha order
2.   You should print only names that do not start with __
3.   Your code should not be executed when imported
4.   Make sure you are running your code in Python3.4.x (hidden_4.pyc has been compiled with this version)

```
guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_holberton
print_school
guillaume@ubuntu:~/0x02$ 
```

###   5. Everything can be imported 
* File: **5-variable_load.py**

* Write a program that imports the variable a from the file variable_load_5.py and prints its value.*

1.  You are not allowed to use * for importing or __import__
2.  Your code should not be executed when imported

```
guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$
```

###  6. Build my own calculator 
*    File: **100-my_calculator.py**

*Write a program that imports all functions from the file calculator\_1.py and handles basic operations.*

1.   Usage: .\/100-my_calculator.py a operator b
     - If the number of arguments is not 3, your program has to:
          - print Usage: ./100-my_calculator.py \<a> \<operator> \<b> followed with a new line
          - exit with the value 1
     - operator can be:
          - \+ for addition
          - for subtraction
          - \* for multiplication
          - \/ for division
     - If the operator is not one of the above:
          - Print Unknown operator. Available operators: +, -, * and / followed with a new line
          - Exit with the value 1
     - You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
     - The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
2.   You are not allowed to use * for importing or __import__
3.   Your code should not be executed when imported

```
guillaume@ubuntu:~/0x02$ cat calculator_1.py
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
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
```


### 7. Easy print 
*   File: **101-easy_print.py** 

*Write a program that prints #pythoniscool, followed by a new line, in the standard output.*

1.   Your program should be maximum 2 lines long
2.   You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

```
guillaume@ubuntu:~/0x02$ ./101-easy_print.py
#pythoniscool
guillaume@ubuntu:~/0x02$ 
```

### 9. Fast alphabet  
*   File: **03-fast_alphabet.py**

*Write a program that prints the alphabet in uppercase, followed by a new line.*

1.   Your program should be maximum 3 lines long
2.   You are not allowed to use:
     - any loops
     - any conditional statements
     - str.join()
     - any string literal
     - any system calls    
