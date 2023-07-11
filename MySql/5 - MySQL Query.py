
# show all the databases :-
# >>> show databases;


# create database :-
# >>> create database company;


# If database already exists then it will not through any error using this query
# >>> create database if not exists company;


# use any specific database :-
# >>> use database_name;
# e.g.
# >>> use company;


# show tables inside specific database :-
# >>> show tables;


# create table error don't appear :-
# >>> create table if not exists table_name;
# e.g.
# >>> create table if not exists emp_info(emp_id int, emp_name varchar(100), emp_age tinyint, emp_salary int, date_of_join date, designation varchar(100));


# To check the description of table :-
'''
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| emp_id       | int          | YES  |     | NULL    |       |
| emp_name     | varchar(100) | YES  |     | NULL    |       |
| emp_age      | tinyint      | YES  |     | NULL    |       |
| emp_salary   | int          | YES  |     | NULL    |       |
| date_of_join | date         | YES  |     | NULL    |       |
| designation  | varchar(100) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
6 rows in set (0.01 sec)
''''
# >>> desc table_name;
# e.g.
# >>> desc emp_info;


# Insert single info in the table :-
# >>> insert into emp_info(emp_id , emp_name, emp_age, emp_salary, date_of_join, designation) values(1, 'raju kumar', 23, 25000, "2023-05-01", "customer support");


# Insert multiple info in the table :-
# >>> insert into emp_info(emp_id , emp_name, emp_age, emp_salary, date_of_join, designation) values(2, "vijay gupta", 23, 23000, "2022-03-04", "sales ex"),(3, "laxmi wallal", 22, 27000, "2022-10-01", "accounting"),(4, "chandu lal", 22, 26000, "2023-08-15", "stock maintaining"),(5, "archana polu", 25, 28000, null, "teaching");


# fetch all the column from the table :-
# >>> select * from table_name;
# e.g.
# >>> select * from emp_info;



































