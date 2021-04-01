	# 0x0E. SQL - More queries 

## GENERAL :open_book::open_book::open_book::

 <ol>
	<li>How to create a new MySQL user</li>
	<li>How to manage privileges for a user to a database or table</li>
	<li>What’s a <code>PRIMARY KEY</code></li>
	<li>What’s a <code>FOREIGN KEY</code></li>
	<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
	<li>How to retrieve datas from multiple tables in one request</li>
	<li>What are subqueries</li>
	<li>What are <code>JOIN</code> and <code>UNION</code></li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/u4h2MXcCQfadszlRMQy-gw" title="How To Create a New User and Grant Permissions in MySQL" target="_blank">How To Create a New User and Grant Permissions in MySQL</a> </li>
	<li><a href="/rltoken/ztrEKQexfEDtZ-8EUsG70Q" title="How To Use MySQL GRANT Statement To Grant Privileges To a User" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a> </li>
	<li><a href="/rltoken/LBrFqCMm9N9woTX7sS7e0g" title="MySQL constraints" target="_blank">MySQL constraints</a> </li>
	<li><a href="/rltoken/YYpPtkqFeKSCsAU4Y_y3Og" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
	<li><a href="/rltoken/npLCp3WasK0SUSUQqCF25A" title="Basic query operation: the join" target="_blank">Basic query operation: the join</a> </li>
	<li><a href="/rltoken/GmRLMhkY-pPvjcpzyDvmRg" title="SQL technique: multiple joins and the distinct keyword" target="_blank">SQL technique: multiple joins and the distinct keyword</a> </li>
	<li><a href="/rltoken/ryjyRRN7696rJV0maP03Xw" title="SQL technique: join types" target="_blank">SQL technique: join types</a> </li>
	<li><a href="/rltoken/L7Fi5w8GZG5MSdQZ19e88g" title="SQL technique: union and minus" target="_blank">SQL technique: union and minus</a> </li>
	<li><a href="/rltoken/V9vpLbtkFwV4EZYoiz2NBA" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
	<li><a href="/rltoken/ySKSdhFeMDddea07XrDzeQ" title="The Seven Types of SQL Joins" target="_blank">The Seven Types of SQL Joins</a> </li>
	<li><a href="/rltoken/-uqP0a89xUl3SsmV_ZtxRA" title="MySQL Tutorial" target="_blank">MySQL Tutorial</a> </li>
	<li><a href="/rltoken/jn4SHgwVtOJF0LQYPEIs-g" title="SQL Style Guide" target="_blank">SQL Style Guide</a> </li>
	<li><a href="/rltoken/YjNAE7DcadDbT_a7iI0sYw" title="MySQL 5.7 SQL Statement Syntax" target="_blank">MySQL 5.7 SQL Statement Syntax</a> </li>
	<li><a href="/rltoken/9ppVdXqFMn-v1eKuxsOvaQ" title="Design" target="_blank">Design</a></li>
	<li><a href="/rltoken/zo6dqYxsXby3S3uON5JfOg" title="Normalization" target="_blank">Normalization</a></li>
	<li><a href="/rltoken/ZaMMezT-GdpgHB9pmM78iw" title="ER Modeling" target="_blank">ER Modeling</a></li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-privileges.sql**:](#0-privilegessql) Script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).
1.	[**1-create_user.sql**:](#1-create_usersql) Script that creates the MySQL server user <code>user_0d_1</code>. 
2.	[**2-create_read_user.sql**:](#2-create_read_usersql) Script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>. 
3.	[**3-force_name.sql**:](#3-force_namesql) Script that creates the table <code>force_name</code> on your MySQL server.
4.	[**4-never_empty.sql**:](#4-never_emptysql) Script that creates the table <code>id_not_null</code> on your MySQL server.
5.	[**5-unique_id.sql**:](#5-unique_idsql) Script that creates the table <code>unique_id</code> on your MySQL server.
6.	[**6-states.sql**:](#6-statessql) Script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.
7.	[**7-cities.sql**:](#7-citiessql) Script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.
8.	[**8-cities_of_california_subquery.sql**:](#8-cities_of_california_subquerysql) Script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.
9.	[**9-cities_by_state_join.sql**:](#9-cities_by_state_joinsql) Script that lists all cities contained in the database <code>hbtn_0d_usa</code>.
10.	[**10-genre_id_by_show.sql**:](#10-genre_id_by_showsql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a>script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.
11.	[**11-genre_id_all_shows.sql**:](#11-genre_id_all_showssql) Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>10-genre_id_by_show.sql</code>)script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.
12.	[**12-no_genre.sql**:](#12-no_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>11-genre_id_all_shows.sql</code>)script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked. 
13.	[**13-count_shows_by_genre.sql**:](#13-count_shows_by_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>12-no_genre.sql</code>)script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.
14.	[**14-my_genres.sql**:](#14-my_genressql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>13-count_shows_by_genre.sql</code>)script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.
15.	[**15-comedy_only.sql**:](#15-comedy_onlysql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>14-my_genres.sql</code>)script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.
16.	[**16-shows_by_genre.sql**:](#16-shows_by_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>15-comedy_only.sql</code>)script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.
17.	[**100-not_my_genres.sql**:](#100-not_my_genressql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>16-shows_by_genre.sql</code>)script that uses the <code>hbtn_0d_tvshows</code> database to list all genres not linked to the show <code>Dexter</code>
18.	[**101-not_a_comedy.sql**:](#101-not_a_comedysql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>100-not_my_genres.sql</code>)script that lists all shows without the genre <code>Comedy</code> in the database <code>hbtn_0d_tvshows</code>.
19.	[**102-rating_shows.sql**:](#102-rating_showssql) Import the database <code>hbtn_0d_tvshows_rate</code> dump to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql" title="download" target="_blank">download</a>script that lists all shows from <code>hbtn_0d_tvshows_rate</code> by their rating.

## FILES :bookmark_tabs::bookmark_tabs::bookmark_tabs::

### 0-privileges.sql

**<p>Script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).</p>**

<pre><code>guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
</code></pre>

### 1-create_user.sql

**<p>Script that creates the MySQL server user <code>user_0d_1</code>. </p>**

<pre><code>guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
</code></pre>

### 2-create_read_user.sql

**<p>Script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>. </p>**

<pre><code>guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost'
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost'
guillaume@ubuntu:~/$ 
</code></pre>

### 3-force_name.sql

**<p>Script that creates the table <code>force_name</code> on your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ 
</code></pre>

### 4-never_empty.sql

**<p>Script that creates the table <code>id_not_null</code> on your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
1   Holberton
guillaume@ubuntu:~/$ 
</code></pre>

### 5-unique_id.sql

**<p>Script that creates the table <code>unique_id</code> on your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ 
</code></pre>

### 6-states.sql

**<p>Script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$ 
</code></pre>

### 7-cities.sql

**<p>Script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ 
</code></pre>

### 8-cities_of_california_subquery.sql

**<p>Script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$ 
</code></pre>

### 9-cities_by_state_join.sql

**<p>Script that lists all cities contained in the database <code>hbtn_0d_usa</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$ 
</code></pre>

### 10-genre_id_by_show.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a></p><p>script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$ 
</code></pre>

### 11-genre_id_all_shows.sql

**<p>Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>10-genre_id_by_show.sql</code>)</p><p>script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$ 
</code></pre>

### 12-no_genre.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>11-genre_id_all_shows.sql</code>)</p><p>script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked. </p>**

<pre><code>guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$ 
</code></pre>

### 13-count_shows_by_genre.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>12-no_genre.sql</code>)</p><p>script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$ 
</code></pre>

### 14-my_genres.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>13-count_shows_by_genre.sql</code>)</p><p>script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$ 
</code></pre>

### 15-comedy_only.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>14-my_genres.sql</code>)</p><p>script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$ 
</code></pre>

### 16-shows_by_genre.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>15-comedy_only.sql</code>)</p><p>script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
guillaume@ubuntu:~/$ 
</code></pre>

### 100-not_my_genres.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>16-shows_by_genre.sql</code>)</p><p>script that uses the <code>hbtn_0d_tvshows</code> database to list all genres not linked to the show <code>Dexter</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Adventure
Comedy
Fantasy
guillaume@ubuntu:~/$ 
</code></pre>

### 101-not_a_comedy.sql

**<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>100-not_my_genres.sql</code>)</p><p>script that lists all shows without the genre <code>Comedy</code> in the database <code>hbtn_0d_tvshows</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
Better Call Saul
Breaking Bad
Dexter
Game of Thrones
Homeland
House
guillaume@ubuntu:~/$ 
</code></pre>

### 102-rating_shows.sql

**<p>Import the database <code>hbtn_0d_tvshows_rate</code> dump to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql" title="download" target="_blank">download</a></p><p>script that lists all shows from <code>hbtn_0d_tvshows_rate</code> by their rating.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    0
guillaume@ubuntu:~/$ 
</code></pre>
