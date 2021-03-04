# SQL - Introduction
In this directory you will learn how to use conditional if, and the while and for loop and differentiate each one

## GENERAL:

1.  What’s a database
2.  What’s a relational database
3.  What does SQL stand for
4.  What’s MySQL
5.  How to create a database in MySQL
6.  What does DDL and DML stand for
7.  How to CREATE or ALTER a table
8.  How to SELECT data from a table
9.  How to INSERT, UPDATE or DELETE data
10.  What are subqueries
11.  How to use MySQL functions

## RESOURSES:

1.   **[What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)**
2.   **[A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)**
3.   **[Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)**
4.   **[Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)**
5.   **[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)**
6.   **[SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)**
7.   **[What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)**
8.   **[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)**
9.   **[MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)**


## Install MySQL 5.7 on Ubuntu 14.04 LTS

* You need to downloand MYSQL to test the files of this directory with the following commands

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```
* Check if you can to enter to my MySQL server with the followin command

```
$ mysql -hlocalhost -uroot -p
```

## Introduction To The Files:

1.  [0-list_databases.sql:](#0-list_databases.sql) TWrite a script that lists all databases of your MySQL server.
2.  [:](#0-positive_or_negativepy) Text Here
3.  [:](#0-positive_or_negativepy) Text Here
4.  [:](#0-positive_or_negativepy) Text Here
5.  [:](#0-positive_or_negativepy) Text Here
6.  [:](#0-positive_or_negativepy) Text Here
7.  [:](#0-positive_or_negativepy) Text Here
8.  [:](#0-positive_or_negativepy) Text Here
9.  [:](#0-positive_or_negativepy) Text Here
10.  [:](#0-positive_or_negativepy) Text Here
11.  [:](#0-positive_or_negativepy) Text Here
12.  [:](#0-positive_or_negativepy) Text Here
13.  [:](#0-positive_or_negativepy) Text Here 
14.  [:](#0-positive_or_negativepy) Text Here

## Files

### 0-list_databases.sql

*Write a script that lists all databases of your MySQL server.*

Example:

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 

```
### 1-create_database_if_missing.sql

*Write a script that creates the database hbtn_0c_0 in your MySQL server.*

1.  If the database hbtn_0c_0 already exists, your script should not fail
2.  You are not allowed to use the SELECT or SHOW statements

```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
```

### 2-remove_database.sql

*Write a script that deletes the database hbtn_0c_0 in your MySQL server.*

1.  If the database hbtn_0c_0 doesn’t exist, your script should not fail
2.  You are not allowed to use the SELECT or SHOW statements
  
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 
```
### 3-list_tables.sql

*TWrite a script that lists all the tables of a database in your MySQL server.*

1. The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)  

```
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$ 
```

### 4-first_table.sql

*Write a script that creates a table called first_table in the current database in your MySQL server.*
1. first_table description: 
    - id INT 
    - name VARCHAR(256)
2. The database name will be passed as an argument of the mysql command
3. If the table first_table already exists, your script should not fail1.  
  
  
```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
```

### 5-full_table.sql

*Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.*

1.  The database name will be passed as an argument of the mysql command
2.  You are not allowed to use the DESCRIBE or EXPLAIN statements

```
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$ 
```

### 6-list_values.sql

*Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.*

1.  All fields should be printed
2.  The database name will be passed as an argument of the mysql command

```
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
```

### 7-insert_value.sql

*Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

1.  New row:
     - id = 89
     - name = Holberton School
2.  The database name will be passed as an argument of the mysql command

```
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$ 
```
### 8-count_89.sql

*Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

1.  The database name will be passed as an argument of the mysql command
  
```
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
```

### 9-full_creation.sql

*TWrite a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.*

1.  second_table description:
    - id INT
    - name VARCHAR(256)
    - score INT
2.  The database name will be passed as an argument to the mysql command
3.  If the table second_table already exists, your script should not fail
4.  You are not allowed to use the SELECT and SHOW statements
5.  Your script should create these records:
    - id = 1, name = “John”, score = 10
    - id = 2, name = “Alex”, score = 3
    - id = 3, name = “Bob”, score = 14
    - id = 4, name = “George”, score = 8
```
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$  
```

### 10-top_score.sql

*Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  Results should display both the score and the name (in this order)
2.  Records should be ordered by score (top first)
3.  The database name will be passed as an argument of the mysql command

  
  
```
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 
```

### 11-best_score.sql

*Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  Results should display both the score and the name (in this order)
2.  Records should be ordered by score (top first)
3.  The database name will be passed as an argument of the mysql command  
  
```
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 

```


### 12-no_cheating.sql
*TEXT HERE *

*Write a script that updates the score of Bob to 10 in the table second_table.*

1.  You are not allowed to use Bob’s id value, only the name field
2.  The database name will be passed as an argument of the mysql command

```
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
```


### 13-change_class.sql

*Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  The database name will be passed as an argument of the mysql command

```
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
```

### 14-average.sql

*Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  The result column name should be average
2.  The database name will be passed as an argument of the mysql command
  
```
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
```

### 15-groups.sql

*Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  The result should display:
    - the score
    - the number of records for this score with the label number
2.  The list should be sorted by the number of records (descending)
3.  The database name will be passed as an argument to the mysql command

  
```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
```

### 16-no_link.sql

*Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.*

1.  Don’t list rows without a name value
2.  Results should display the score and the name (in this order)
3.  Records should be listed by descending score
4.  The database name will be passed as an argument to the mysql command

  
```
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
```

### 100-move_to_utf8.sql

*Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.  You need to convert all of the following to UTF8:*

1.  Database hbtn_0c_0
2.  Table first_table
3.  Field name in first_table

  
```
guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$ 
```

### 101-avg_temperatures.sql

*TWrite a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).*

```
guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
guillaume@ubuntu:~/$ 
```

### 102-top_city.sql

*Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)*

1.    
2.    
3.    
  
  
```
guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$ 
```

### T103-max_state.sql

*Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0) Write a script that displays the max temperature of each state (ordered by State name)*
  
```
guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
```

