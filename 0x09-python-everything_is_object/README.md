# 0x13. C - More singly linked lists

## GENERAL:

 <ol>
	<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
	<li>All your files will be compiled on Ubuntu 14.04 LTS</li>
	<li>Your programs and functions will be compiled with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code></li>
	<li>All your files should end with a new line</li>
	<li>A <code>README.md</code> file, at the root of the folder of the project is mandatory</li>
	<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
	<li>You are not allowed to use global variables</li>
	<li>No more than 5 functions per file</li>
	<li>The only C standard library functions allowed are <code>malloc</code>, <code>free</code> and <code>exit</code>. Any use of functions like <code>printf</code>, <code>puts</code>, <code>calloc</code>, <code>realloc</code> etc… is forbidden</li>
	<li>You are allowed to use <a href="https://github.com/holbertonschool/_putchar.c/blob/master/_putchar.c" title="_putchar" target="_blank">_putchar</a></li>
	<li>You don’t have to push <code>_putchar.c</code>, we will use our file. If you do it won’t be taken into account</li>
	<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
	<li>The prototypes of all your functions and the prototype of the function <code>_putchar</code> should be included in your header file called <code>lists.h</code></li>
	<li>Don’t forget to push your header file</li>
	<li>All your header files should be include guarded</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/VxmJXbHtjDMJAKj7dU-6sg" title="Google" target="_blank">Google</a> </li>
	<li><a href="/rltoken/PqebvZ1ey95sB8eDiYl8_A" title="Youtube" target="_blank">Youtube</a> </li>
</ol>

## INTRODUCTION TO FILES:

0.	[0-print_listint.c:](#0-print_listintc) Write a function that prints all the elements of a
1.	[1-listint_len.c:](#1-listint_lenc) Write a function that returns the number of elements in a linked
2.	[2-add_nodeint.c:](#2-add_nodeintc) Write a function that adds a new node at the beginning of a
3.	[3-add_nodeint_end.c:](#3-add_nodeint_endc) Write a function that adds a new node at the end of a
4.	[4-free_listint.c:](#4-free_listintc) Write a function that frees a
5.	[5-free_listint2.c:](#5-free_listint2c) Write a function that frees a
6.	[6-pop_listint.c:](#6-pop_listintc) Write a function that deletes the head node of a
7.	[7-get_nodeint.c:](#7-get_nodeintc) Write a function that returns the nth node of a
8.	[8-sum_listint.c:](#8-sum_listintc) Write a function that returns the sum of all the data (n) of a
9.	[9-insert_nodeint.c:](#9-insert_nodeintc) Write a function that inserts a new node at a given position.
10.	[10-delete_nodeint.c:](#10-delete_nodeintc) Write a function that deletes the node at index
11.	[100-reverse_listint.c:](#100-reverse_listintc) Write a function that reverses a
## FILES:

### 0-print_listint.c

*<p>Function that prints all the elements of a <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>size_t print_listint(const listint_t *h);</code></li>
	<li>Return: the number of nodes</li>
	<li>Format: see example</li>
	<li>You are allowed to use <code>printf</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 0-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *new;
    listint_t hello = {8, NULL};
    size_t n;

    head = &amp;hello;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        printf("Error\n");
        return (1);
    }
    new-&gt;n = 9;
    new-&gt;next = head;
    head = new;
    n = print_listint(head);
    printf("-&gt; %lu elements\n", n);
    free(new);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-print_listint.c -o a
julien@ubuntu:~/0x13. More singly linked lists$ ./a
9
8
-&gt; 2 elements
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 1-listint_len.c

*<p>Function that returns the number of elements in a linked <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>size_t listint_len(const listint_t *h);</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 1-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *new;
    listint_t hello = {8, NULL};
    size_t n;

    head = &amp;hello;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        printf("Error\n");
        return (1);
    }
    new-&gt;n = 9;
    new-&gt;next = head;
    head = new;
    n = listint_len(head);
    printf("-&gt; %lu elements\n", n);
    free(new);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 1-main.c 1-listint_len.c -o b
julien@ubuntu:~/0x13. More singly linked lists$ ./b
-&gt; 2 elements
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 2-add_nodeint.c

*<p>Function that adds a new node at the beginning of a <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>listint_t *add_nodeint(listint_t **head, const int n);</code></li>
	<li>Return: the address of the new element, or <code>NULL</code> if it failed</li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 2-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint(&amp;head, 0);
    add_nodeint(&amp;head, 1);
    add_nodeint(&amp;head, 2);
    add_nodeint(&amp;head, 3);
    add_nodeint(&amp;head, 4);
    add_nodeint(&amp;head, 98);
    add_nodeint(&amp;head, 402);
    add_nodeint(&amp;head, 1024);
    print_listint(head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 2-main.c 2-add_nodeint.c 0-print_listint.c -o c
julien@ubuntu:~/0x13. More singly linked lists$ ./c
1024
402
98
4
3
2
1
0
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 3-add_nodeint_end.c

*<p>Function that adds a new node at the end of a <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>listint_t *add_nodeint_end(listint_t **head, const int n);</code></li>
	<li>Return: the address of the new element, or <code>NULL</code> if it failed</li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 3-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 3-main.c 3-add_nodeint_end.c 0-print_listint.c -o d
julien@ubuntu:~/0x13. More singly linked lists$ ./d
0
1
2
3
4
98
402
1024
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 4-free_listint.c

*<p>Function that frees a <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>void free_listint(listint_t *head);</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 4-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    free_listint(head);
    head = NULL;
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 4-main.c 3-add_nodeint_end.c 0-print_listint.c 4-free_listint.c -o e
julien@ubuntu:~/0x13. More singly linked lists$ valgrind ./e
==3643== Memcheck, a memory error detector
==3643== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==3643== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==3643== Command: ./e
==3643==
0
1
2
3
4
98
402
1024
==3643==
==3643== HEAP SUMMARY:
==3643==     in use at exit: 0 bytes in 0 blocks
==3643==   total heap usage: 9 allocs, 9 frees, 1,152 bytes allocated
==3643==
==3643== All heap blocks were freed -- no leaks are possible
==3643==
==3643== For counts of detected and suppressed errors, rerun with: -v
==3643== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 5-free_listint2.c

*<p>Function that frees a <code>listint_t</code> list.</p>*

<ul>
	<li>Prototype: <code>void free_listint2(listint_t **head);</code></li>
	<li>The function sets the <code>head</code> to <code>NULL</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 5-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    free_listint2(&amp;head);
    printf("%p\n", (void *)head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 5-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c -o f
julien@ubuntu:~/0x13. More singly linked lists$ valgrind ./f
==3843== Memcheck, a memory error detector
==3843== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==3843== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==3843== Command: ./f
==3843==
0
1
2
3
4
98
402
1024
(nil)
==3843==
==3843== HEAP SUMMARY:
==3843==     in use at exit: 0 bytes in 0 blocks
==3843==   total heap usage: 9 allocs, 9 frees, 1,152 bytes allocated
==3843==
==3843== All heap blocks were freed -- no leaks are possible
==3843==
==3843== For counts of detected and suppressed errors, rerun with: -v
==3843== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 6-pop_listint.c

*<p>Function that deletes the head node of a <code>listint_t</code> linked list, and returns the head node’s data (n).</p>*

<ul>
	<li>Prototype: <code>int pop_listint(listint_t **head);</code></li>
	<li>if the linked list is empty return <code>0</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 6-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    int n;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    n = pop_listint(&amp;head);
    printf("- %d\n", n);
    print_listint(head);
    n = pop_listint(&amp;head);
    printf("- %d\n", n);
    print_listint(head);
    free_listint2(&amp;head);
    printf("%p\n", (void *)head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 6-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c 6-pop_listint.c -o g
julien@ubuntu:~/0x13. More singly linked lists$ valgrind ./g
==4369== Memcheck, a memory error detector
==4369== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==4369== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==4369== Command: ./g
==4369==
0
1
2
3
4
98
402
1024
- 0
1
2
3
4
98
402
1024
- 1
2
3
4
98
402
1024
(nil)
==4369==
==4369== HEAP SUMMARY:
==4369==     in use at exit: 0 bytes in 0 blocks
==4369==   total heap usage: 9 allocs, 9 frees, 1,152 bytes allocated
==4369==
==4369== All heap blocks were freed -- no leaks are possible
==4369==
==4369== For counts of detected and suppressed errors, rerun with: -v
==4369== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 7-get_nodeint.c

*<p>Function that returns the nth node of a <code>listint_t</code> linked list.</p>*

<ul>
	<li>Prototype: <code>listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);</code></li>
	<li>where <code>index</code> is the index of the node, starting at <code>0</code></li>
	<li>if the node does not exist, return <code>NULL</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 7-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *node;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    node = get_nodeint_at_index(head, 5);
    printf("%d\n", node-&gt;n);
    print_listint(head);
    free_listint2(&amp;head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 7-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c 7-get_nodeint.c -o h
julien@ubuntu:~/0x13. More singly linked lists$ ./h
0
1
2
3
4
98
402
1024
98
0
1
2
3
4
98
402
1024
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 8-sum_listint.c

*<p>Function that returns the sum of all the data (n) of a <code>listint_t</code> linked list.</p>*

<ul>
	<li>Prototype: <code>int sum_listint(listint_t *head);</code></li>
	<li>if the list is empty, return <code>0</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 8-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    int sum;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    sum = sum_listint(head);
    printf("sum = %d\n", sum);
    free_listint2(&amp;head);
    return (0);
}
julien@ubuntu:~/c0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 8-main.c 3-add_nodeint_end.c 5-free_listint2.c 8-sum_listint.c -o i
julien@ubuntu:~/0x13. More singly linked lists$ ./i
sum = 1534
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 9-insert_nodeint.c

*<p>Function that inserts a new node at a given position.</p>*

<ul>
	<li>Prototype: <code>listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n);</code></li>
	<li>where <code>idx</code> is the index of the list where the new node should be added. Index starts at <code>0</code></li>
	<li>Returns: the address of the new node, or <code>NULL</code> if it failed</li>
	<li>if it is not possible to add the new node at index <code>idx</code>, do not add the new node and return <code>NULL</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 9-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    printf("-----------------\n");
    insert_nodeint_at_index(&amp;head, 5, 4096);
    print_listint(head);
    free_listint2(&amp;head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 9-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c 9-insert_nodeint.c -o j
julien@ubuntu:~/0x13. More singly linked lists$ ./j
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
4096
98
402
1024
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 10-delete_nodeint.c

*<p>Function that deletes the node at index <code>index</code> of a <code>listint_t</code> linked list.</p>*

<ul>
	<li>Prototype: <code>int delete_nodeint_at_index(listint_t **head, unsigned int index);</code></li>
	<li>where <code>index</code> is the index of the node that should be deleted. Index starts at <code>0</code></li>
	<li>Returns: <code>1</code> if it succeeded, <code>-1</code> if it failed</li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 10-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 5);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    printf("-----------------\n");
    delete_nodeint_at_index(&amp;head, 0);
    print_listint(head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 10-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c 10-delete_nodeint.c -o k
julien@ubuntu:~/0x13. More singly linked lists$ valgrind ./k
==5571== Memcheck, a memory error detector
==5571== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==5571== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==5571== Command: ./k
==5571==
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
402
1024
-----------------
1
2
3
4
402
1024
-----------------
2
3
4
402
1024
-----------------
3
4
402
1024
-----------------
4
402
1024
-----------------
402
1024
-----------------
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
==5571==
==5571== HEAP SUMMARY:
==5571==     in use at exit: 0 bytes in 0 blocks
==5571==   total heap usage: 9 allocs, 9 frees, 1,152 bytes allocated
==5571==
==5571== All heap blocks were freed -- no leaks are possible
==5571==
==5571== For counts of detected and suppressed errors, rerun with: -v
==5571== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>

### 100-reverse_listint.c

*<p>Function that reverses a <code>listint_t</code> linked list.</p>*

<ul>
	<li>Prototype: <code>listint_t *reverse_listint(listint_t **head);</code></li>
	<li>Returns: a pointer to the first node of the reversed list</li>
	<li>You are not allowed to use more than <code>1</code> loop.</li>
	<li>You are not allowed to use <code>malloc</code>, <code>free</code> or arrays</li>
	<li>You can only declare a maximum of two variables in your function</li>
</ul>

<pre><code>julien@ubuntu:~/0x13. More singly linked lists$ cat 100-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 0);
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 2);
    add_nodeint_end(&amp;head, 3);
    add_nodeint_end(&amp;head, 4);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 402);
    add_nodeint_end(&amp;head, 1024);
    print_listint(head);
    reverse_listint(&amp;head);
    print_listint(head);
    free_listint2(&amp;head);
    return (0);
}
julien@ubuntu:~/0x13. More singly linked lists$ gcc -Wall -pedantic -Werror -Wextra 100-main.c 3-add_nodeint_end.c 0-print_listint.c 5-free_listint2.c 100-reverse_listint.c -o l
julien@ubuntu:~/0x13. More singly linked lists$ valgrind ./l
==3117== Memcheck, a memory error detector
==3117== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==3117== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==3117== Command: ./l
==3117==
0
1
2
3
4
98
402
1024
1024
402
98
4
3
2
1
0
==3117==
==3117== HEAP SUMMARY:
==3117==     in use at exit: 0 bytes in 0 blocks
==3117==   total heap usage: 9 allocs, 9 frees, 1,152 bytes allocated
==3117==
==3117== All heap blocks were freed -- no leaks are possible
==3117==
==3117== For counts of detected and suppressed errors, rerun with: -v
==3117== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
julien@ubuntu:~/0x13. More singly linked lists$
</code></pre>
