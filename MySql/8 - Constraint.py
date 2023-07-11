# constraint is used to impliment restriction on columns.


# 1 - NOT NULL -
# 2 - UNIQUE   _| primary key
# 3 - DEFAULT
# 4 - CHECK
# 5 - AUTO_INCREMENT :- by default start from 1 and increase by 1
# 6 - PRIMARY KEY
# 7 - FOREIGN KEY

## create table with constraints (Default):-

# >>> insert into student(s_id, s_name, s_age, contact) values(1, "Mahesh", 25, 7896541230);

## Add Dynamic city or constraints :-

# >>> insert into student(s_id, s_name, s_age, contact, city) values(2, "Mahi", 24, 789654321, "thane");


## create table with AUTO_INCREMENT or PRIMARY KEY :-

# >>> create table customer(c_id int not null unique auto_increment, c_name varchar(100) not null, c_email varchar(100) not null, primary key(c_id));


## create table with FOREIGN KEY :-

# >>> create table orders(o_id int not null auto_increment, o_date date not null, amount int not null, c_id int not null, primary key(o_id), foreign key(c_id) references customer(c_id));



#      Add constrain in existing table

## create new table for constrain :-

# >>> create table temp(id int, name varchar(50), contact varchar(50));


## add Not null constrain in existing table

# >>> alter table temp modify id int NOT null;

#********************************************************************************


## add UNIQUE Constrain to existing table

# >>> alter table temp add unique(id);

#**********************************************************************************

## add default constraint in existing table

# >>> alter table temp alter contact set default 1111111;

#************************************************************************************

# Add check constraint in existing column

# >>>  alter table temp add check (age > 18);

#***************************************************************************************

## Add primary key constraint in existing table

# >>> alter table temp add primary key(id);














