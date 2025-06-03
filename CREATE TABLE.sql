create table student
 (
 
   id int,
   name varchar(100),
   roll varchar(20),
   phone varchar(20),
   age int
 );
insert into student(id,name,roll,phone,age) value(11,"harsha",425,900000000,21);
insert into student(id,name,roll,phone,age) value(10,"sunny",423,900000000,20);
select * from student;



create table sales
 (
 
   serial_no int,
   product_id int,
   product_name varchar(100),
   quantity int,
   category varchar(20)
   
 );
insert into sales(serial_no,product_id,product_name,quantity,category) values
(401,1001,"Mobile",100,"ELECTRONICS"),
(402,1002,"PEPSI",100,"SOFT-DRINK"),
(403,1003,"T-SHIRT",120,"FASHION"),
(404,1004,"SUN-SCREEN",145,"BEAUTY"),
(405,1005,"DOSA",130,"FOOD"),
(406,1006,"FORD-1969",110,"VEHICLE"),
(407,1007,"F-1",130,"SPORTS");


select SUM(quantity) as Total_Sales
from sales


SELECT * 
    from details
    right join student 
    on student.roll_no = details.roll_no;

    SELECT * 
    from details
    left join student 
    on student.roll_no = details.roll_no;


    create database practice;
use practice;
create table student(
  roll_no int primary key,
  name varchar(150) not null,
  course_name varchar(100) not null
  );
  
  create table details(
     roll_no int,
     address text,
     phone_no varchar(20) not null,
     FOREIGN KEY (roll_no) REFERENCES student(roll_no)
	);
    insert into student(roll_no,NAME,course_name) values
    (1,"A","ECE"),
    (2,"B","CSE"),
    (3,"C","AI"),
    (4,"D","EEE"),
    (5,"E","MECH");
    SELECT * FROM STUDENT;
    insert into DETAILS(roll_no,address,phone_no) values
    (1," ",9000545537),
	(2," ",9000545536),
    (3,"KDP",9000545538),
    (4,"BAY",9000545539),
    (5,"ATP",9000545540);
    SELECT * FROM DETAILS;
    SELECT * 
    from student 
    join details 
    on student.roll_no = details.roll_no; 
    select s.roll_no,s.name,s.course_name,d.phone_no from student s
    left join details d on s.roll_no = d.roll_no;
	insert into student(roll_no,NAME,course_name) values
    (10,"H","ECE");
	SELECT * 
    from details
    right join student 
    on student.roll_no = details.roll_no;
    
    
  
    
     
     
     
  