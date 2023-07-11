#                       Aggregate Function

# aggregate function perform a calculation on a set of values and return a single value.

# 1 - count()
# 2 - sum()
# 3 - avg()
# 4 - min()
# 5 - max()
# 6 - concat()
# 7 - group concat()
# 8 - limit()
# 9 - desc()


# 1 - count()
# return count of specific column.

# >>> select count(emp_name) from emp_info;


# 2 - sum()
# it will return sum of the column works only with Numeric type column.

# >>> select sum(emp_salary) from emp_info;


# 3 - avg()
# it will return avg of the column works only with Numeric type column.

# >>> select avg(emp_age) from emp_info;


# 4 - min()
# return the minimum value inside from the column.

# >>> select min(emp_salary) from emp_info;


# 5 - max()
# return the maxmium value inside from the column.

# >>>  select max(emp_salary) from emp_info;


# 6 - concat()
# concatenation of two columns.

# >>>  select concat(emp_name ,"   ",designation) from emp_info;



## 8 - limit()
# we can retrict the output using limit.

# >>> select * from emp_info limit 3;


# 9 - desc()
# show output in descending order.

# >>> select * from emp_info order by emp_name desc;






