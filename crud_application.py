# create read , update ,delete

import mysql.connector as db
import pandas as pd


class crud:
    def __init__(self):
        # Create Database

        mydb = db.connect(host='localhost', user='root', passwd='rahul')
        cur = mydb.cursor()

        query = '''create database if not exists dbuser;'''
        cur.execute(query)

        mydb.close()

        # create table
        mydb = db.connect(host='localhost', user='root',password='rahul', database='dbuser')          
        cur = mydb.cursor()

        query = '''create table if not exists user_info1(id int not null auto_increment,full_name varchar(100) not null,user_name varchar(100) not null unique,Email varchar(100) unique,location varchar(100) not null,primary key (id));'''

        cur.execute(query)
        print('Database table created sucessfully !')
        mydb.close()

    def connection(self):
        self.mydb = db.connect(host='localhost', user="root", passwd="rahul", database="dbuser")  
        self.cur = self.mydb.cursor()

    def insert_value(self, full_name, user_name, Email, location):
        self.connection()
        # Insert Query
        query = f''' insert into user_info1(full_name, user_name, Email, location ) values('{full_name}', '{user_name}', '{Email}', '{location}');'''

        self.cur.execute(query)

        self.cur.execute("commit;")

        print("value_inserted Sucessfully !")

        self.mydb.close()

    def all_data(self, username):
        self.connection()

        query = f'''select * from user_info1 where user_name="{username}";'''

        self.cur.execute(query)

        data = self.cur.fetchall()
     
        self.mydb.close()
        return data

    def update_info(self, username, new_name=None, new_loc=None):
        self.connection()
        if new_name != None:
            query = f'''update user_info1 set full_name="{new_name}" where user_name="{username}"; '''
            self.cur.execute(query)
            self.cur.execute("commit;")
            self.mydb.close()
        elif new_loc != None:
            query = f'''update user_info1 set location="{new_loc}" where user_name="{username}"; '''
            self.cur.execute(query)
            self.cur.execute("commit;")
            self.mydb.close()
        else:
            print("Invalid UserID!")

    def delete_info(self, username):
        try:
            self.connection()
            query = f'''delete from user_info1 where user_name="{username}";'''
            self.cur.execute(query)
            #print("query executed :")
            self.cur.execute("commit;")
            self.mydb.close()
        except:
            print("Invalid Username !")


if __name__ == "__main__":
    app = crud()

    while True:
        print("\n--------------- Crud Application ---------------")
        print("\n1 - Insert Information\n2 - Read Data\n3 - Update data\n4 - Delete data\n5 - Exit \n")

        ch = input("Enter Your Choice :")
        if ch == "1":
            print('\n--------------- Insert Information ---------------\n')

            full_name = input("Enter your full name: ")
            user_name = input("Enter user name: ")
            Email = input("Enter Email id: ")
            location = input("Enter Location: ")

            app.insert_value(full_name, user_name, Email, location)

        elif ch == "2":
            username = input("Enter your username :")
            
            try:
                data = app.all_data(username)
                if data != []:
                    df = pd.DataFrame(data, columns=["id", "full_name", "user_name", "Email", "location"])
               
                    print()
                    print(df, "\n")
                    
                else:
                    print("!invalid username")
                    
            except:
                print("!invalid username")

        elif ch == "3":
            print("Press 1 for update name and press 2 for update location")
            print("Press any key to cancel")
            username = input("Enter your username :")

            a = input("Enter you update choice :")
            if a == '1':
                name_value = input("Enter new name :")
                app.update_info(username, new_name=name_value)
                print("Name Updated Sucessfully !")

            elif a == '2':
                name_loc = input("Enter new location :")
                app.update_info(username, new_loc=name_loc)
                print("Location Updated Sucessfully !")

            else:
                print("Operation cancel !")
                
        elif ch == "4":
            username = input("Enter your username: ")

            B = input("Are you Sure Y/N: ")

            if B == 'Y' or B == "y":
                #print("method called :")
                app.delete_info(username)
                print(f"Delete Username {username} Sucessfully !")

            else:
                print("delete cancelled !")
                
        elif ch == "5":
            print("\n--------- Program Finish ---------\n")
            break
        
        else:
            print("\n--------- Invalid Input ---------\n")
