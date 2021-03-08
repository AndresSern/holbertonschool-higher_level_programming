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

