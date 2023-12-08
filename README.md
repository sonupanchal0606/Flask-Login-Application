# Flask-Login-Application
A simple login application using flask

Tools used :
1) Pycharm --> Code editor
2) MAMP
   - Apache server --> to create local server to host application
   - MySql Server (PhpMyAdmin) --> to create database
3) Mac OS M1

Reference : https://www.youtube.com/watch?v=swHI1H7DVsQ

Steps :
1) Download and install PyCharm Community Edition from https://www.jetbrains.com/pycharm/download/
2) Download and install MAMP from "https://www.mamp.info/en/downloads/"
3) Open Pycharm Code Editor --> Create Project "Expense-App"
      - Create main.py to create the flask application
      - Create templates folder to include html files into your project
      - create static folder to include static files like css or js into your project
      - Run the application by click right click on main.py screen -> click on "Run 'main'"
      - The project Directory will look like this : 
      <img width="378" alt="Screenshot 2023-12-08 at 12 50 00 PM" src="https://github.com/sonupanchal0606/connect-php-with-mysql-using-MAMP/assets/55386781/14b82ed4-c764-49a7-bbdf-8dc0212121de">

4) start the MAMP server
<img width="526" alt="Screenshot 2023-12-08 at 12 57 07 PM" src="https://github.com/sonupanchal0606/connect-php-with-mysql-using-MAMP/assets/55386781/585c18d9-10bc-4542-ac71-8fbdc445c1f0">

   - It will Open the the page http://localhost:8888/MAMP/?language=English
   - Tools -> MyPhpAdmin
     <img width="978" alt="Screenshot 2023-12-08 at 1 32 33 PM" src="https://github.com/sonupanchal0606/connect-php-with-mysql-using-MAMP/assets/55386781/effe7d07-94c9-401f-8a47-d8e2c9b28d1e">

5) creatr Database flaskloginDB -> create table users
<img width="1197" alt="Screenshot 2023-12-08 at 1 40 38 PM" src="https://github.com/sonupanchal0606/connect-php-with-mysql-using-MAMP/assets/55386781/341a5816-1b07-4146-b924-701337842b60">

<img width="1202" alt="Screenshot 2023-12-08 at 1 36 27 PM" src="https://github.com/sonupanchal0606/connect-php-with-mysql-using-MAMP/assets/55386781/8598def5-61dc-4c8d-b5d3-6acce9964685">

6) To connect with the PhpMyAdmin DB you can get the reference code here http://localhost:8888/MAMP/?language=English --> MySql -> Examples
   
7) To access the PhpMyAdmin databse from your terminal :
      - cd /Applications/MAMP/Library/bin
      - ./mysql -uroot -proot
mysql> show databases;
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    133
Current database: bank

+--------------------+
| Database           |
+--------------------+
| information_schema |
| bank               |
| flaskloginDB       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.01 sec)

mysql> use flaskloginDB;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------+
| Tables_in_flasklogindb |
+------------------------+
| users                  |
+------------------------+
1 row in set (0.00 sec)

mysql> select * from users;
+---------+----------+--------------------+----------+
| user_id | name     | email              | password |
+---------+----------+--------------------+----------+
|     123 | sonu     | sonu@gmail.com     |      123 |
|     124 | arya     | arya@gmail.com     |      124 |
|     125 | Khaleesi | Khaleesi@gmail.com |      123 |
|     126 | xyz      | xyz@gmail.com      |      123 |
+---------+----------+--------------------+----------+
4 rows in set (0.00 sec)

mysql> 


  


