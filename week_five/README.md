##### Mysql Request

TASK2

REQUEST1:create database website;

![img]()

REQUEST2:mysql> create table member(
-> id int auto_increment primary key,
-> name varchar(254) not null,
-> email varchar(254) not null,
-> password varchar(254) not null,
-> follower_count int check(follower_count >0) default 0 not null,
-> time datetime not null default current_timestamp
-> );

![img]()

TASK3

REQUEST1:insert into member(name, email, password, follower_count)values('test', 'test@test.com', 'test', '25');

insert into member(name, email, password, follower_count)
values
('Willy', 'will123@gmail.com', 'W555', '23'),
('Annie', 'ooac@gmail.com', 'oac865', '83'),
('Abigale', 'Abi45@gmail.com', 'BB548', '47'),
('Luka', 'Lukas45@gmail.com', 'Luke4565', '50');

![img]()

REQUEST2:select \* from member where id < 6;

![img]()

REQUEST3:select \* from member order by time desc;

![img]()

REQUEST4:select \* from member order by time desc limit 1, 3;

![img]()

REQUEST5:select \* from member where email = 'test@test.com';

![img]()

REQUEST6:select \* from member where email like '%es%';

![img]()

REQUEST7:select \* from member where email = 'test@test.com' and password = 'test';

![img]()

REQUEST78:update member set name = 'test2' where email = 'test@test.com';

![img]()

TASK4

REQUEST1:select count(\*) from member;

![img]()

REQUEST2:select sum(follower_count) from member;

![img]()

REQUEST3:select avg(follower_count) from member;

![img]()

REQUEST4:select avg(follower_count) from (select follower_count from member order by follower_count desc limit 0, 2 ) as temp;

![img]()
