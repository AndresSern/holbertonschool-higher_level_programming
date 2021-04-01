# 0x12. JavaScript - Warm up

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>Why JavaScript programming is amazing</li>
	<li>How to run a JavaScript script</li>
	<li>How to create variables and constants</li>
	<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
	<li>What are all the data types available in JavaScript</li>
	<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
	<li>How to use comments</li>
	<li>How to affect values to variables</li>
	<li>How to use <code>while</code> and <code>for</code> loops</li>
	<li>How to use <code>break</code> and <code>continue</code> statements</li>
	<li>What is a function and how do you use functions</li>
	<li>What does a function that does not use any <code>return</code> statement return</li>
	<li>Scope of variables</li>
	<li>What are the arithmetic operators and how to use them</li>
	<li>How to manipulate dictionary</li>
	<li>How to import a file</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Writing JavaScript Code" target="_blank">Writing JavaScript Code</a> </li>
	<li><a href="/rltoken/iE6zaLw7pybp648IfRmk5Q" title="Variables" target="_blank">Variables</a> </li>
	<li><a href="/rltoken/4td1BbZAYn4Dldi6k0CY7A" title="Data Types" target="_blank">Data Types</a> </li>
	<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Operators" target="_blank">Operators</a> </li>
	<li><a href="/rltoken/ALCoiVRvxmsjdqCUdWC_lg" title="Operator Precedence" target="_blank">Operator Precedence</a> </li>
	<li><a href="/rltoken/Nlfhdy6Thyu_WgtBSqoAUw" title="Controlling Program Flow" target="_blank">Controlling Program Flow</a> </li>
	<li><a href="/rltoken/Ta66PZ6_16K3q99oELvjkQ" title="Functions" target="_blank">Functions</a> </li>
	<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Objects and Arrays" target="_blank">Objects and Arrays</a> </li>
	<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Intrinsic Objects" target="_blank">Intrinsic Objects</a> </li>
	<li><a href="/rltoken/mduSK-WOoRe6WohU1p2zZQ" title="Module patterns" target="_blank">Module patterns</a> </li>
	<li><a href="/rltoken/kNWuHjyUvjr74wU2hBqd_A" title="var, let and const" target="_blank">var, let and const</a> </li>
	<li><a href="/rltoken/qkp1hdLiI8DJje88bxcL6w" title="JavaScript Tutorial" target="_blank">JavaScript Tutorial</a> </li>
	<li><a href="/rltoken/ieSajamJQ-Nv3XzcS_d5lA" title="Modern JS" target="_blank">Modern JS</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-javascript_is_amazing.js**:](#0-javascript_is_amazingjs) Script that prints “JavaScript is amazing”
1.	[**1-multi_languages.js**:](#1-multi_languagesjs) Script that prints 3 lines
2.	[**2-arguments.js**:](#2-argumentsjs) Script that prints a message depending of the number of arguments passedReference <a href="/rltoken/E5x0rMmgii1g_Da9R7DUag" title="process.argv" target="_blank">process.argv</a>
3.	[**3-value_argument.js**:](#3-value_argumentjs) Script that prints the first argument passed to it
4.	[**4-concat.js**:](#4-concatjs) Script that prints two arguments passed to it, in the following format “<first argument> is <second argument>”</second></first>
5.	[**5-to_integer.js**:](#5-to_integerjs) Script that prints <code>My number &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer
6.	[**6-multi_languages_loop.js**:](#6-multi_languages_loopjs) Script that prints 3 lines (like <code>1-multi_languages.js</code>) but by using an array of string and a loop
7.	[**7-multi_c.js**:](#7-multi_cjs) Script that prints <code>x</code> times “C is fun”
8.	[**8-square.js**:](#8-squarejs) Script that prints a square
9.	[**9-add.js**:](#9-addjs) Script that prints the addition of 2 integers
10.	[**10-factorial.js**:](#10-factorialjs) Script that computes and prints a factorial
11.	[**11-second_biggest.js**:](#11-second_biggestjs) Script that searches the second biggest integer in the list of arguments.
12.	[**12-object.js**:](#12-objectjs) Update this script to replace the value <code>12</code> with <code>89</code>
13.	[**13-add.js**:](#13-addjs) Function that returns the addition of 2 integers.<a href="/rltoken/M3uMoMlngAtefSYF1c7PNQ" title="Tip" target="_blank">Tip</a> 
14.	[**100-let_me_const.js**:](#100-let_me_constjs) File that modifies the value of <code>myVar</code> to <code>333</code><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T014022Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=63f755d0a41bed318b6accc0df846d49ef0c3909a0b0dec4cf4236c65b4c1383" alt="" style="">Do you get it? Tweet! Post! Talk about it!Hint Scope<strong>This exercise doesn’t pass <code>semistandard</code></strong> so don’t worry about it.
15.	[**101-call_me_moby.js**:](#101-call_me_mobyjs) Function that executes <code>x</code> times a function.
16.	[**102-add_me_maybe.js**:](#102-add_me_maybejs) Function that increments and calls a function.
17.	[**103-object_fct.js**:](#103-object_fctjs) Update this script by adding a new function <code>incr</code> that increments the integer <code>value</code>.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-javascript_is_amazing.js

**<p>Script that prints “JavaScript is amazing”</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 1-multi_languages.js

**<p>Script that prints 3 lines</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 2-arguments.js

**<p>Script that prints a message depending of the number of arguments passed</p><p>Reference <a href="/rltoken/E5x0rMmgii1g_Da9R7DUag" title="process.argv" target="_blank">process.argv</a></p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 3-value_argument.js

**<p>Script that prints the first argument passed to it</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 4-concat.js

**<p>Script that prints two arguments passed to it, in the following format “<first argument> is <second argument>”</second></first></p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 5-to_integer.js

**<p>Script that prints <code>My number &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 6-multi_languages_loop.js

**<p>Script that prints 3 lines (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 7-multi_c.js

**<p>Script that prints <code>x</code> times “C is fun”</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 8-square.js

**<p>Script that prints a square</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 9-add.js

**<p>Script that prints the addition of 2 integers</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 10-factorial.js

**<p>Script that computes and prints a factorial</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 11-second_biggest.js

**<p>Script that searches the second biggest integer in the list of arguments.</p>**

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 12-object.js

**<p>Update this script to replace the value <code>12</code> with <code>89</code></p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 13-add.js

**<p>Function that returns the addition of 2 integers.</p><p><a href="/rltoken/M3uMoMlngAtefSYF1c7PNQ" title="Tip" target="_blank">Tip</a> </p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 100-let_me_const.js

**<p>File that modifies the value of <code>myVar</code> to <code>333</code></p><p><img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T014022Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=63f755d0a41bed318b6accc0df846d49ef0c3909a0b0dec4cf4236c65b4c1383" alt="" style=""></p><p>Do you get it? Tweet! Post! Talk about it!</p><p>Hint Scope</p><p><strong>This exercise doesn’t pass <code>semistandard</code></strong> so don’t worry about it.</p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 101-call_me_moby.js

**<p>Function that executes <code>x</code> times a function.</p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 102-add_me_maybe.js

**<p>Function that increments and calls a function.</p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
</code></pre>

### 103-object_fct.js

**<p>Update this script by adding a new function <code>incr</code> that increments the integer <code>value</code>.</p>**

<pre><code>guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
</code></pre>

