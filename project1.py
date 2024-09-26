# Boutique Management System
import mysql.connector
db = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = "boutique"
)
mycursor = db.cursor()

print("Welcome To The Shop")

print("Select one to Procced")

print("1. Customer\n2. Employees\n3. Employer")
print("Enter a Role:")
choice = input()

if choice == 'Customer' or choice == '1':
    print("Your Role Is Customer")
elif choice == 'Employees' or choice == '2':
    print("Your Role Is Employees")
elif choice == 'Employer' or choice == '3':
    print("Your Role is Employer")
else:
    print("You are selected wrong role")
    exit()

print("Welcome",choice,"! Please Login")

nam = input("Enter Your Name:")
user = str(input("Enter a Username:"))
pas = (input("enter a Password:"))

username = "admin"
password = "131003"

if user == username and pas == password :
    print("Login Successfully Welcome",nam)
else:
    print("Login Unsuccessfully! Please Enter a valid Username and Password ")
    exit()

print("Welcome",choice,nam,"!!")

if choice == "Customer" or choice == '1':
    a = input("Enter your Name:")
    b = input("Enter your Gender:")
    c = input("Enter your Customer_ID:")
    d = input("Enter your Address:")
    sql = "Insert Into customer(Name,Gender,Customer_ID,Address) VALUES(%s,%s,%s,%s)"
    val = (a, b, c, d)
    mycursor.execute(sql,val)
    db.commit()
    print("Customer deatil added")
    
    print("1.Booking Order\n2.View Booking\n3.Delete Booking\n4.Update Their Details")
    choose = input("select a one option")

elif choice=="Employees" or choice == '2':
   
  id = int(input("Enter a Emp_Id:"))
  pas = input("Enter a password:")
  Name =  input("Enter Your Name:")
  Gen = input("Enter your Gender:")

  if id  and pas and Name and Gen:
    print("Sign In Successfully! Welcome Employee",nam)
  else:
    print("Sign In Unsuccessfully! Please Enter all Information Correctly")
    exit()
  
  sql = "Insert Into employees(Emp_Id,Password,Name,Gender) VALUES(%s,%s,%s,%s)"
  val = (id,pas,Name,Gen)
  mycursor.execute(sql,val)
  db.commit()
  print("Employees data added successfully")

  if choice == "Employees" or choice == '2' :
     print("1.updating delivered orders of customers\n2.Adding a new product\n3.Deleting a product\n4.View Product")
  choose = input("select a one option")
 

elif choice == "Employer" or choice == '3':
   print("1.View Product\n2.View new Employee\n3.Adding a product\n4.Adding a new Employee\n5.Deleting a Product\n6.Removing a Employee")
   choose = input("select a one option")

else:
   print("Invalid Option Select! select Right option")
   exit()

if choice == "Employer" or choice == '3':
 if choose == '4':
  print("add a new employee")
  while True:
   a = input("Enter your Name:")
   b = input("Enter your Emp_Id:")
   c = input("Enter your password:")
   d = input("Enter your Address:")

   sql = "INSERT INTO employer(Name,Emp_Id,password,Address) VALUES(%s, %s, %s, %s)"
   val = (a, b, c, d)

   mycursor.execute(sql,val)
   db.commit()
   print(mycursor.rowcount,"Successfully add a new employee")
 
 elif choose == '2':
  print("View new employee")
  
  sql = "Select*From employer"
  mycursor.execute(sql)
  abc = mycursor.fetchall()
  for s in abc:
   print(s)
  print("fetching successfully")
  
 elif choose == '3':
   print("Adding a new Product")
   while True:
    s = input("Enter a Product_id:") 
    t = input("Enter a Product_Name:")
    u = input("Enter a Product_size:")
    v = input("Enter a Product_Color:")

    sql = "Insert Into product(Product_id,Product_Name,Product_size,Product_Color) Values(%s,%s,%s,%s)"
    val = (s, t, u, v)

    mycursor.execute(sql,val)
    db.commit()
    print(mycursor.rowcount,"Successfully Added new product")

 elif choose == '1':
  print("View New Product")
 
  sql = "Select*From product"
  mycursor.execute(sql)

  result = mycursor.fetchall()
  for s in result:
    print(s)
  print("successfully feteching a products")

 elif choose == '5':
    print("Deleting a Product")
    sql ="Select*From product"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for u in result:
      print(u)

    l = input("Please enter the Product ID of the product you want to delete.")
              
    sql = "Delete From product where Product_id = %s"
    adr = (l,)
    mycursor.execute(sql,adr)
    db.commit()
    print("successfully Delted product",l)

 elif choose == '6':
    print("Removing a Employee")
    sql ="Select*From employer"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for u in result:
      print(u)

    h = input("Please enter the Name of the Employee you want to Remove.")
              
    sql = "Delete From employer where Name = %s"
    car = (h,)
    mycursor.execute(sql,car)
    db.commit()
    print("successfully Removing a Employee",h)

 else:
  print("Your Selected  Option Invalid! Select a Right Opton")


elif choice == "Employess" or choice == '2' :
  if choose == '2':
    print("Adding a new product")
    while True:
      m = input("Enter a Product_id:")
      n = input("Enter a Product_Name:")
      o = input("Enter a Product_size:")
      p = input("Enter a Product_Color:")

      sql = "Insert Into product(Product_id,Product_Name,Product_size,Product_Color) Values(%s,%s,%s,%s)"
      val = (m, n, o, p)

      mycursor.execute(sql,val)
      db.commit()
      print(mycursor.rowcount,"successfully Add a new Product")

  elif choose == "3":
     print("Delete a Product")
     sql ="Select*From product"
     mycursor.execute(sql)
     result = mycursor.fetchall()
     for k in result:
      print(k)

     r = input("Please enter the Product ID of the product you want to delete.")
              
     sql = "Delete From product where Product_id = %s"
     adr = (r,)
     mycursor.execute(sql,adr)
     db.commit()
     print("successfully Deleted product",r)
  
  elif choose == '4':
     print("view product")
  
     sql ="Select*From product"
     mycursor.execute(sql)
     result = mycursor.fetchall()
     for u in result:
      print(u)
     print("View Product successfully")

  elif choose == '1':
     print("updating delivered orders of customers")

     order_conformation = input("Has the product been delivered? (yes/no): ")

     if order_conformation == 'yes':
       print("Order delivered Successfully")
     elif order_conformation == 'no':
       print("Order not delivered")
     else:
       print("Enter a wrong value")
       exit()

     sql = "select*From order1 where Status = 'Pending'"
     mycursor.execute(sql)
     result = mycursor.fetchall()
     for s in result:
       print(s)
     a = input("Enter a id where you update status:")
     sql = "Update order1 Set Status = 'Delivered' Where Status = 'pending' and id = %s"
     va = (a,)
     mycursor.execute(sql,va)
     db.commit()
     print("updated successfully")
  else:
   print("Your Selected  Option Invalid! Select a Right Opton")
 
elif choice == "Customer" or choice == '1':
  if choose == '1':
    print("Book Order??")

    sql = "Select*From product"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for y in result:
      print(y)  
    print("Successfully Feteching all products")
    
    a= input("Enter a Product_Id of the product you want to book.")
    
    sql = "Select*From product Where Product_Id = %s"
    xyz = (a,)
    mycursor.execute(sql,xyz)
    res = mycursor.fetchall()
    for h in res:
      print(h)
    print("Booking Successfully",nam)

    for h in res:
        
        id= h[0]
        Product_id = h[1]        
        Product_Name = h[2]   
        Product_size = h[3]   
        product_color = h[4]

    sql = "Insert Into order1(Product_id,Product_Name,Product_size,product_color,Status) VALUES(%s,%s,%s,%s,%s)"
    val = (Product_id,Product_Name,Product_size,product_color,'Pending')
    mycursor.execute(sql,val)
    db.commit()
    print("successfully added new order ")
  

  elif choose=='2':
     print("View Booking")
  
     sql = "Select*From order1"
     mycursor.execute(sql)
     res = mycursor.fetchall()
     for s in res:
      print(s)
     print("View a product successfully")

  elif choose == '3':
    print("Delete a order") 
    
    sql = "select*from order1"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for f in result:
      print(f)
    print("fetching oreder")

    b = input("Please enter the Product ID of the product you want to delete order.")

    sql = "Delete From order1 where Product_Id = %s"
    val = (b,)
    mycursor.execute(sql,val)
    db.commit()
    print("successfully deleted order",b)
  

  elif choose == '4':
    print("Update Their Details")

    sql = "Select*From customer"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for s in result:
      print(s)
    print("Fetching data")

    d = input("Enter a update data:")
    column = input("Enter a column:")
    e = input("Enter Id, where the update data:")

    sql = f"update customer set {column} =%s where Id =  %s "
    val = (d,e)
    mycursor.execute(sql,val)
    db.commit()
    print("Updated successfully")
  
  else:
    print("Slect Wrong Option")


