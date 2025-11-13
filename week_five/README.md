##### Mysql Request

TASK2

REQUEST1:
create database website;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_2_REQUEST_1.png)

REQUEST2:
create table member(
  id int auto_increment primary key,
  name varchar(254) not null,
  email varchar(254) not null,
  password varchar(254) not null,
  follower_count int check(follower_count >0) default 0 not null,
  time datetime not null default current_timestamp
  );

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_2_REQUEST_2.png)

TASK3

REQUEST1:
insert into member(name, email, password, follower_count)values('test', 'test@test.com', 'test', '25');

insert into member(name, email, password, follower_count)
values
('Willy', 'will123@gmail.com', 'W555', '23'),
('Annie', 'ooac@gmail.com', 'oac865', '83'),
('Abigale', 'Abi45@gmail.com', 'BB548', '47'),
('Luka', 'Lukas45@gmail.com', 'Luke4565', '50');

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_1.png)

REQUEST2:
select \* from member where id < 6;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_2.png)

REQUEST3:
select \* from member order by time desc;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_3.png)

REQUEST4:
select \* from member order by time desc limit 1, 3;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_4.png)

REQUEST5:
select \* from member where email = 'test@test.com';

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_5.png)

REQUEST6:
select \* from member where email like '%es%';

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_6.png)

REQUEST7:
select \* from member where email = 'test@test.com' and password = 'test';

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_7.png)

REQUEST78:
update member set name = 'test2' where email = 'test@test.com';

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_3_REQUEST_8.png)

TASK4

REQUEST1:
select count(\*) from member;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_4_REQUEST_1.png)

REQUEST2:
select sum(follower_count) from member;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_4_REQUEST_2.png)

REQUEST3:
select avg(follower_count) from member;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_4_REQUEST_3.png)

REQUEST4:
select avg(follower_count) from (select follower_count from member order by follower_count desc limit 0, 2 ) as temp;

![img](https://github.com/pervertcoder/WeHelp-The-First-Stage/blob/main/week_five/截圖/TASK_4_REQUEST_4.png)
