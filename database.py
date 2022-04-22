import sqlite3
con=sqlite3.connect("projectDB.db")
print("Database created successfully")

# con.execute("drop table users")
# con.execute("create table users(user_id integer primary key autoincrement, name text not null, gender text not null, email text not null, phone text not null, password text not null);")

# con.execute("DELETE FROM users WHERE email = 'abc@gmail.com';")
# res=con.execute("select * from users")
# for i in res:
#     print(i[0],i[1],i[2],i[3],i[4],i[5])

# con.execute('drop table products')
# con.execute("create table products(id integer primary key autoincrement, name text not null, image text not null, price float not null, onSale integer, onSalePrice float not null, kind text not null);")
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Laptop","Laptop.png",70000,0,70000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("iPad ","iPad.png",45000,1,40000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("A C","A C.png",20000,0,20000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Washing Machine","Washing Machine.png",20000,0,20000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("MacBook","MacBook.png",90000,0,90000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Tab","Tab.png",40000,1,35000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Freeze","Freeze.png",20000,1,15000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("AirPods","AirPods.png",20000,0,20000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("iPhone","iPhone.png",65000,1,60000,'electronics'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("SmartPhone","SmartPhone.png",10000,0,10000,'electronics'))
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Polo Tshirt","Polo Tshirt.png",500,1,400,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Womens Tshirt","Womens Tshirt.png",350,0,350,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Jeans","Jeans.png",999,0,999,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Jacket","Jacket.png",3500,1,3000,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Shirt","Shirt.png",1200,1,900,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Hoodie","Hoodie.png",1500,1,1200,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Tshirt","Tshirt.png",300,0,300,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Kurta","Kurta.png",2000,0,2000,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Tuxedo","Tuxedo.png",10000,1,8000,'cloth'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Womens Shirt","Womens Shirt.png",900,1,800,'cloth'))
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Geometry Box","Geometry Box.png",250,0,250,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Pencil","Pencil.png",10,0,10,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("FeviStick","FeviStick.png",45,1,35,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Scissors","Scissors.png",100,0,100,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("A4 Sheets","A4 Sheets.png",200,0,200,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Ball Pen","Ball Pen.png",15,1,10,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Drawing Set","Drawing Set.png",500,0,500,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("ClipBoard","ClipBoard.png",100,0,100,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Parker Pen","Parker Pen.png",450,1,400,'stationary-products'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("NoteBook","NoteBook.png",87,0,87,'stationary-products'))
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Dining Tbale","Dining Tbale.png",7000,0,7000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Sofa cum Bed","Sofa cum Bed.png",4000,1,4000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Royal Wing Chair","Royal Wing Chair.png",4000,0,4500,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Bean Bag","Bean Bag.png",1000,1,1000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Chair","Chair.png",1000,0,1000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Study Table","Study Table.png",2000,1,2000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Revolving chair","Revolving chair.png",3500,0,3500,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("King Size Bed","King Size Bed.png",20000,1,20000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Recliner","Recliner.png",30000,0,30000,'furniture'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Couch","Couch.png",10000,1,10000,'furniture'))
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Sunscreen","Sunscreen.png",300,0,300,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Shampoo","Shampoo.png",200,1,200,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Deo","Deo.png",500,0,500,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Facial Mask","Facial Mask.png",150,0,150,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Conditioner","Conditioner.png",200,1,200,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Lipsticks","Lipsticks.png",700,0,700,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Face Wash","Face Wash.png",400,0,400,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Nail Paint","Nail Paint.png",100,1,100,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Perfume","Perfume.png",1500,0,1500,'personal-care'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Body Lotion","Body Lotion.png",250,0,250,'personal-care'))
#
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 1","Toy 1.png",200,1,200,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 2","Toy 2.png",300,0,300,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 3","Toy 3.png",400,1,400,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 4","Toy 4.png",500,1,500,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 5","Toy 5.png",600,0,600,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 6","Toy 6.png",700,1,700,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 7","Toy 7.png",800,1,800,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 8","Toy 8.png",900,0,900,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 9","Toy 9.png",1000,1,1000,'toys'))
# con.execute("INSERT INTO products (name,image,price,onSale,onSalePrice,kind) VALUES (?,?,?,?,?,?) ", ("Toy 10","Toy 10.png",1100,1,1100,'toys'))
# con.commit()

res=con.execute("SELECT * FROM products")
for i in res:
    print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])

#con.execute("create table cart(image text,name text,qty integer, price text, subTotal text, id integer );")

con.execute('drop table purchases')
con.execute("create table purchases(uid integer, name text, image text, quantity integer, id integer, date text);")
# con.commit()


res=con.execute("SELECT * FROM users")
for i in res:
    print(i[0],i[1],i[2],i[3],i[4])


# con.execute("create table queries(name text,phone text,mail integer, message text);")


res=con.execute("SELECT * FROM queries")
for i in res:
    print(i[0],i[1],i[2],i[3])

con.execute('drop table deliveryDetails')
con.execute("create table deliveryDetails(uid integer, name text, mobile text, ddate text, mail text, method text, address text);")
# con.commit()

res=con.execute("SELECT * FROM deliveryDetails")
for i in res:
    print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])