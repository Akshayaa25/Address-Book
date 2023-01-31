# Personal Address Book

import pymysql
from tabulate import tabulate

try:
    connection = pymysql.connect(host="localhost", user="root", password='', db="addressbook")
    cursor = connection.cursor()

    headers = ["Name", "Phone Number", "City"]

    # Functions
    def search():
        info = input("Search name/phone number/city : ")
        cmd = "select * from contactlist where namelist like '%"+info +"%' or phone like '%"+info+"%' or city like '%"+info+"%'"
        cursor.execute(cmd)
        data = cursor.fetchall()
        if len(data) > 0:
            print(tabulate(data, headers, tablefmt="fancy_grid",numalign="center", stralign="center"))
        else:
            print("Given data not found in the address book")
        print("----------------------x----------------------")

    def viewall():
        cmd = "select * from contactlist"
        cursor.execute(cmd)
        data = cursor.fetchall()
        print(tabulate(data, headers, tablefmt="fancy_grid",numalign="center", stralign="center"))
        print("----------------------x----------------------")

    def add():
        name = input("Enter the name : ")
        phone = int(input("Enter the phone : "))
        city = input("Enter the city : ")
        column = (name, phone, city)
        cmd = "insert into contactlist values(%s,%s,%s)"
        cursor.execute(cmd, column)
        print("----------------------x----------------------")

    def edit():
        editname = input("Enter the name you want to edit : ")
        cmd = "select * from contactlist where namelist='%s'" % (editname)
        cursor.execute(cmd)
        if cursor.fetchone():
            print("What do you want to edit?")
            print("1.Name \n2.Phone number \n3.City")
            ch = int(input("Enter the choice number : "))
            if ch == 1:
                name = input("Enter the name : ")
                cmd = "update contactlist set namelist='%s'where namelist='%s'" % (name, editname)
                cursor.execute(cmd)
            elif ch == 2:
                phone = int(input("Enter the phone number : "))
                cmd = "update contactlist set phone='%d'where namelist='%s'" % (phone, editname)
                cursor.execute(cmd)
            elif ch == 3:
                city = input("Enter the city : ")
                cmd = "update contactlist set city='%s'where namelist='%s'" % (city, editname)
                cursor.execute(cmd)
            else:
                print("Choice number is incorrect")
        else:
            print("Name Not Found")
        print("----------------------x----------------------")

    def delcontact():
        name = input("Enter the name you want to delete : ")
        cmd = "select * from contactlist where namelist='%s'" % (name)
        cursor.execute(cmd)
        if cursor.fetchone():
            print("Are you sure you want to delete this contact?")
            print("1.Yes\t2.No")
            confirmation = int(input("Enter the choice number : "))
            if (confirmation == 1):
                cmd = "delete from contactlist where namelist='%s'" % (name)
                cursor.execute(cmd)
                print("Deleted this contact successfully")
        else:
            print("Name Not Found")
        print("----------------------x----------------------")

    def deleteall():
        print("Are you sure you want to delete all contacts?")
        print("1.Yes\t2.No")
        confirmation = int(input("Enter the choice number : "))
        if (confirmation == 1):
            cmd = "truncate table contactlist"
            cursor.execute(cmd)
            print("Deleted all contacts successfully")
            print("----------------------x----------------------")

    while True:
        print("What do you want to do?")
        print("1.Search Contact \n2.View all contacts \n3.Add contact \n4.Edit contact \n5.Delete contact \n6.Delete all contacts \n7.Close")
        choice = int(input("Enter the choice number : "))

        if choice == 1:
            search()

        elif choice == 2:
            viewall()

        elif choice == 3:
            add()

        elif choice == 4:
            edit()

        elif choice == 5:
            delcontact()

        elif choice == 6:
            deleteall()

        else:
            print("Address Book Closed")
            break

    connection.commit()
    connection.close()

except (Exception) as ex:
    print(ex.__class__, ex.args)
    print("Oops! Something went wrong")
