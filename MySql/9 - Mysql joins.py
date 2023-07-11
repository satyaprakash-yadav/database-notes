#                       MYSQL JOINS


# Joins :- To combine two or more tables inside database is called joins.

# 1 - Inner join
# 2 - left join
# 3 - right join
# 4 - cross join
# 5 - full join

# table 1
# customer

# table 2
# orders

## 1 - Inner join :- It used to fetch common records from the tables.

# syntax :-
# select * from table_1 inner join table_2 on table_1.id = table_2.id;

# >>> select * from customer inner join orders on customer.c_id = orders.c_id;


## 2 - left join :- It used to fetch common or left table records;

# syntax :-
# select * from table_1 left join table_2 on table_1.id = table_2.id;

# >>> select * from customer left join orders on customer.c_id = orders.c_id;


## 3 - right join :- It used to fetch all records from the right table and the matching common records from the left table.

# syntax :-
# select * from table_1 left join table_2 on table_1.id = table_2.id;

# >>> select * from customer right join orders on customer.c_id = orders.c_id;


## 4 - cross join :- It used to fetch all records from the both the tables(table_1 and table_2) forms like matrix.

# >>> select * from customer cross join orders;



## 5 - full join or full outer join :- Mysql does not support directly full join.
# full outer join keyword return common records and left table data and right table data.

# >>> select * from customer left join orders on customer.c_id = orders.c_id union select * from customer right join orders on customer.c_id = orders.c_id;




