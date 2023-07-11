# MYSQL Opeartor :-


# 1 - Arithmetic operator :-

# + , -, * , / , %

# these are the arithmetic operator to perform maths operations to the tables.

# >>> select emp_name, emp_salary+1000, designation from emp_info;

# >>> select emp_name, emp_salary-500.50, designation from emp_info;

# >>> select emp_name, emp_salary*3, designation from emp_info;

# >>> select emp_name, emp_salary/3, designation from emp_info;

# >>> select emp_name, emp_salary%3, designation from emp_info;



# --------------------------------------------------------------------------------

# Logical Operator :-

# AND   , &&
# all expression are True then AND return True otherwise False.

# >>> select * from emp_info where emp_salary > 18000 && emp_salary < 24000;

# OR    , ||
# if one expression True then OR return True otherwise False.

# >>> select * from emp_info where emp_salary > 18000 or emp_salary < 22000;


# --------------------------------------------------------------------------------

# Relational & Comparision Operator :-

# > greater then

# < less then

# >= greater then equals to

# <= less then equals to

# =  equals to

# != equals to


# Fetch only those records where employee designation is 'sales ex' 
# >>> select * from emp_info where designation = "sales ex";


# Fetch those records the employee salary is in between 18000 to 24000
# >>> select * from emp_info where emp_salary >= 18000 and emp_salary <= 23000;


# >>> select emp_id, emp_name from emp_info where emp_id !=7;


# --------------------------------------------------------------------------------

# 4 - IS NULL , IS NOT NULL Operator :-
# Null is datatype to represent Empty Data Set

# those record which have null data set
# >>> select * from emp_info where date_of_join is null;


# those record which don't have null data set
# >>> select * from emp_info where date_of_join is not null;


# --------------------------------------------------------------------------------

# 5 - In , Not In Operator :-

# In
# >>> select * from emp_info where emp_name in ("raju kumar", 'vijay gupta', 'laxmi wallal');

# Not  In
# >>>  select * from emp_info where emp_name not in ("raju kumar", 'vijay gupta', 'laxmi wallal');


# --------------------------------------------------------------------------------

# 6 - Between __AND__ , NOt Between __AND__ Operator :-
# Works with Numeric data

# >>> select * from emp_info where emp_salary between 25000 AND 26000;

# >>> select * from emp_info where emp_salary not between 25000 AND 26000;


# --------------------------------------------------------------------------------


# 7 - Wild card characters :-

# '%'   - for any character or any length

# '_'   - for any character but single length


# --------------------------------------------------------------------------------

# 8 - Like , Not Like Operators :-

# >>> select * from emp_info where emp_name like "r%r";

# >>> select * from emp_info where emp_name not like "r%r";

# >>> select * from emp_info where emp_name like "v__________";

# >>> select * from emp_info where emp_name not like "v__________";














