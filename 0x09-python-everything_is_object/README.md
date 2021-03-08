# 0x0B. Python - Input/Output


## GENERAL:

 <ol>
	<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
	<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
	<li>All your files should end with a new line</li>
	<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
	<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
	<li>Your code should use the <code>PEP 8</code> style (version 1.7.*)</li>
	<li>All your files must be executable</li>
	<li>The length of your files will be tested using <code>wc</code></li>
</ol>:


## RESOURCES:

 <ul>
<li><a href="/rltoken/c5ypFfQwcM-SZ-7tr3WuxA" title="7.2. Reading and Writing Files" target="_blank">7.2. Reading and Writing Files</a> </li>
<li><a href="/rltoken/1wqMFejKqBva-Lxws0lftw" title="8.7. Predefined Clean-up Actions" target="_blank">8.7. Predefined Clean-up Actions</a> </li>
<li><a href="/rltoken/8aSPOpBZj9B1DB6GfoEWfg" title="Dive Into Python 3: Chapter 11. Files" target="_blank">Dive Into Python 3: Chapter 11. Files</a> (<em>until “11.4 Binary Files” (included)</em>)</li>
<li><a href="/rltoken/XBqM3BrA_rUBw6DXw4X98Q" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/derf9VLFVDnSgX2n-drwnw" title="Learn to Program 8 : Reading / Writing Files" target="_blank">Learn to Program 8 : Reading / Writing Files</a> </li>
<li><a href="/rltoken/Y77h8aeRoljlN643yKfdTg" title="Automate the Boring Stuff with Python" target="_blank">Automate the Boring Stuff with Python</a> (<em>ch. 8 p 180-183 and ch. 14 p 326-333</em>)</li>
</ul>:


## INTRODUCTION TO FILES:


<ol>
	<li>[0-read_file.py:](#0-read_filepy) Write a function that reads a text file</li>
	<li>[1-write_file.py:](#1-write_filepy) Write a function that writes a string to a text file</li>
	<li>[2-append_write.py:](#2-append_writepy) Write a function that appends a string at the end of a text file</li>
	<li>[3-to_json_string.py:](#3-to_json_stringpy) Write a function that returns the JSON representation of an object (string):</li>
	1.  [0-list_databases.sql:](#0-list_databasessql) TWrite a script that lists all databases of your MySQL server.
</ol>
## FILES:


### 0-read_file.py


*Write a function that returns the JSON representation of an object (string):*


<ul>
<li>Prototype: <code>def read_file(filename=""):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage <code>file permission</code> or <code>file doesn't exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>


<pre><code>guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ 
</code></pre>


### 1-write_file.py


*Write a function that returns the JSON representation of an object (string):*


<ul>
<li>Prototype: <code>def write_file(filename="", text=""):</code></li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage file permission exceptions.</li>
<li>Your function should create the file if doesn’t exist.</li>
<li>Your function should overwrite the content of the file if it already exists.</li>
<li>You are not allowed to import any module</li>
</ul>


<pre><code>guillaume@ubuntu:~/0x0B$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
Holberton School is so cool!
guillaume@ubuntu:~/0x0B$ 
</code></pre>


### 2-append_write.py


*Write a function that returns the JSON representation of an object (string):*


<ul>
<li>Prototype: <code>def append_write(filename="", text=""):</code></li>
<li>If the file doesn’t exist, it should be created</li>
<li>You must use the <code>with</code> statement</li>
<li>You don’t need to manage <code>file permission</code> or <code>file doesn't exist</code> exceptions.</li>
<li>You are not allowed to import any module</li>
</ul>


<pre><code>guillaume@ubuntu:~/0x0B$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:~/0x0B$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
Holberton School is so cool!
Holberton School is so cool!
guillaume@ubuntu:~/0x0B$ 
</code></pre>


### 3-to_json_string.py


*Write a function that returns the JSON representation of an object (string):*


<ul>
<li>Prototype: <code>def to_json_string(my_obj):</code></li>
<li>You don’t need to manage exceptions if the object can’t be serialized.</li>
</ul>


<pre><code>guillaume@ubuntu:~/0x0B$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0B$ ./3-main.py
[1, 2, 3]
&lt;class 'str'&gt;
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
&lt;class 'str'&gt;
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ 
</code></pre>
