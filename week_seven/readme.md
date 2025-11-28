先建立一份.env 檔案

按照.env.example 的格式填入自己的資料庫資訊

使用前請先按照步驟建立資料庫以及資料表

create database memberdatabase;

create table memberinfo(

id int auto_increment primary key,

name varchar(254) not null,

email varchar(254) not null,

password varchar(254) not null

);

create table search_history(

id int primary key auto_increment,

search_person_id int not null,

target_user_id int not null,

search_time datetime not null default current_timestamp,

foreign key(search_person_id) references memberinfo(id)

);
