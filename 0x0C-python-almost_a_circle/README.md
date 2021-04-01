# 0x0C. Python - Almost a circle

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>What is Unit testing and how to implement it in a large project</li>
	<li>How to serialize and deserialize a Class</li>
	<li>How to write and read a JSON file</li>
	<li>What is <code>*args</code> and how to use it</li>
	<li>What is <code>**kwargs</code> and how to use it</li>
	<li>How to handle named arguments in a function</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/LroIjBBI5Gqq3ciR-OHmxg" title="args/kwargs" target="_blank">args/kwargs</a> </li>
	<li><a href="/rltoken/TY4rfu2AZtXlRmPVNZm1Lw" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
	<li><a href="/rltoken/T7uxwxtGdbRRW9pkD4eO0g" title="unittest module" target="_blank">unittest module</a> </li>
	<li><a href="/rltoken/SfEo3RQeAXXYI9yabFRw3g" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**models/rectangle.py**:](#modelsrectanglepy) Write the class <code>Rectangle</code> that inherits from <code>Base</code>Why private attributes with getter/setter? Why not directly public attribute?Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
1.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded)
2.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by adding the public method <code>def area(self)</code> that returns the area value of the <code>Rectangle</code> instance.
3.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by adding the public method <code>def display(self)</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don’t need to handle <code>x</code> and <code>y</code> here.
4.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code>
5.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by improving the public method <code>def display(self)</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code>
6.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args)</code> that assigns an argument to each attributeThis type of argument is called a “no-keyword argument” - Argument order is super important.
7.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args)</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributesThis type of argument is called a “key-worded argument”. Argument order is not important.
8.	[**models/square.py**:](#modelssquarepy) Write the class <code>Square</code> that inherits from <code>Rectangle</code>As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.
9.	[**models/square.py**:](#modelssquarepy) Update the class <code>Square</code> by adding the public getter and setter <code>size</code>
10.	[**models/square.py**:](#modelssquarepy) Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes
11.	[**models/rectangle.py**:](#modelsrectanglepy) Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a <code>Rectangle</code>This dictionary must contain
12.	[**models/square.py**:](#modelssquarepy) Update the class <code>Square</code> by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a <code>Square</code>This dictionary must contain
13.	[**models/base.py**:](#modelsbasepy) JSON is one of the standard formats for sharing data representation.Update the class <code>Base</code> by adding the static method <code>def to_json_string(list_dictionaries)</code> that returns the JSON string representation of <code>list_dictionaries</code>
14.	[**models/base.py**:](#modelsbasepy) Update the class <code>Base</code> by adding the class method <code>def save_to_file(cls, list_objs)</code> that writes the JSON string representation of <code>list_objs</code> to a file
15.	[**models/base.py**:](#modelsbasepy) Update the class <code>Base</code> by adding the static method <code>def from_json_string(json_string)</code> that returns the list of the JSON string representation <code>json_string</code>
16.	[**models/base.py**:](#modelsbasepy) Update the class <code>Base</code> by adding the class method <code>def create(cls, **dictionary)</code> that returns an instance with all attributes already set
17.	[**models/base.py**:](#modelsbasepy) Update the class <code>Base</code> by adding the class method <code>def load_from_file(cls)</code> that returns a list of instances
18.	[**models/**:](#models) Update the class <code>Base</code> by adding the class methods <code>def save_to_file_csv(cls, list_objs)</code> and <code>def load_from_file_csv(cls)</code> that serializes and deserializes in CSV

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### models/rectangle.py

**<p>Write the class <code>Rectangle</code> that inherits from <code>Base</code></p><p>Why private attributes with getter/setter? Why not directly public attribute?</p><p>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded)</p>**

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be &gt; 0
[TypeError] x must be an integer
[ValueError] y must be &gt;= 0
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by adding the public method <code>def area(self)</code> that returns the area value of the <code>Rectangle</code> instance.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by adding the public method <code>def display(self)</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don’t need to handle <code>x</code> and <code>y</code> here.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (&lt;id&gt;) &lt;x&gt;/&lt;y&gt; - &lt;width&gt;/&lt;height&gt;</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by improving the public method <code>def display(self)</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args)</code> that assigns an argument to each attribute</p><p>This type of argument is called a “no-keyword argument” - Argument order is super important.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args)</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributes</p><p>This type of argument is called a “key-worded argument”. Argument order is not important.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$ 
</code></pre>

### models/square.py

**<p>Write the class <code>Square</code> that inherits from <code>Rectangle</code></p><p>As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

guillaume@ubuntu:~/$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9



 ###
 ###
 ###
guillaume@ubuntu:~/$ 
</code></pre>

### models/square.py

**<p>Update the class <code>Square</code> by adding the public getter and setter <code>size</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
guillaume@ubuntu:~/$ 
</code></pre>

### models/square.py

**<p>Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes</p>**

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

guillaume@ubuntu:~/$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
guillaume@ubuntu:~/$ 
</code></pre>

### models/rectangle.py

**<p>Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a <code>Rectangle</code></p><p>This dictionary must contain</p>**

<pre><code>guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

guillaume@ubuntu:~/$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
&lt;class 'dict'&gt;
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
guillaume@ubuntu:~/$ 
</code></pre>

### models/square.py

**<p>Update the class <code>Square</code> by adding the public method <code>def to_dictionary(self)</code> that returns the dictionary representation of a <code>Square</code></p><p>This dictionary must contain</p>**

<pre><code>guillaume@ubuntu:~/$ cat 13-main.py
#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

guillaume@ubuntu:~/$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
&lt;class 'dict'&gt;
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
guillaume@ubuntu:~/$ 
</code></pre>

### models/base.py

**<p>JSON is one of the standard formats for sharing data representation.</p><p>Update the class <code>Base</code> by adding the static method <code>def to_json_string(list_dictionaries)</code> that returns the JSON string representation of <code>list_dictionaries</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 14-main.py
#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

guillaume@ubuntu:~/$ ./14-main.py
{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
&lt;class 'dict'&gt;
[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
&lt;class 'str'&gt;
guillaume@ubuntu:~/$ 
</code></pre>

### models/base.py

**<p>Update the class <code>Base</code> by adding the class method <code>def save_to_file(cls, list_objs)</code> that writes the JSON string representation of <code>list_objs</code> to a file</p>**

<pre><code>guillaume@ubuntu:~/$ cat 15-main.py
#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

guillaume@ubuntu:~/$ ./15-main.py
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
guillaume@ubuntu:~/$ 
</code></pre>

### models/base.py

**<p>Update the class <code>Base</code> by adding the static method <code>def from_json_string(json_string)</code> that returns the list of the JSON string representation <code>json_string</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 16-main.py
#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

guillaume@ubuntu:~/$ ./16-main.py
[&lt;class 'list'&gt;] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
[&lt;class 'str'&gt;] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
[&lt;class 'list'&gt;] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
guillaume@ubuntu:~/$ 
</code></pre>

### models/base.py

**<p>Update the class <code>Base</code> by adding the class method <code>def create(cls, **dictionary)</code> that returns an instance with all attributes already set</p>**

<pre><code>guillaume@ubuntu:~/$ cat 17-main.py
#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

guillaume@ubuntu:~/$ ./17-main.py
[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
guillaume@ubuntu:~/$ 
</code></pre>

### models/base.py

**<p>Update the class <code>Base</code> by adding the class method <code>def load_from_file(cls)</code> that returns a list of instances</p>**

<pre><code>guillaume@ubuntu:~/$ cat 18-main.py
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

guillaume@ubuntu:~/$ ./18-main.py
[139785912033120] [Rectangle] (1) 2/8 - 10/7
[139785912033176] [Rectangle] (2) 0/0 - 2/4
---
[139785911764752] [Rectangle] (1) 2/8 - 10/7
[139785911764808] [Rectangle] (2) 0/0 - 2/4
---
---
[139785912058040] [Square] (5) 0/0 - 5
[139785912061848] [Square] (6) 9/1 - 7
---
[139785911764976] [Square] (5) 0/0 - 5
[139785911765032] [Square] (6) 9/1 - 7
guillaume@ubuntu:~/$ 
</code></pre>

### models/

**<p>Update the class <code>Base</code> by adding the class methods <code>def save_to_file_csv(cls, list_objs)</code> and <code>def load_from_file_csv(cls)</code> that serializes and deserializes in CSV</p>**

<pre><code>guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

guillaume@ubuntu:~/$ ./100-main.py
[140268695797600] [Rectangle] (1) 2/8 - 10/7
[140268695797656] [Rectangle] (2) 0/0 - 2/4
---
[140268695529008] [Rectangle] (1) 2/8 - 10/7
[140268695528952] [Rectangle] (2) 0/0 - 2/4
---
---
[140268695822520] [Square] (5) 0/0 - 5
[140268695826328] [Square] (6) 9/1 - 7
---
[140268695529232] [Square] (5) 0/0 - 5
[140268695529176] [Square] (6) 9/1 - 7
guillaume@ubuntu:~/$ 
</code></pre>

