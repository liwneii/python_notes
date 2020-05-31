# MySQL

## 准备工作

### service启动/停止：service mysql start/stop
client链接/退出：mysql -uroot -ppassword/quit

### 

## 数据库的操作

### 库操作

- 显示数据库：show databases; 
    - 显示时间/版本：show now()/show version();
            - 创建数据库：create database dataname charset=utf8;
使用数据库：use database dataname;
显示数据库信息：show create database dataname;
删除数据库：drop database dataname;
查询数据库：select database();

### 表操作

- 查询表：show tables;|
创建表：create table tablename(id int, name varchar(30));
查询表头信息：desc tablename; / show create table tablename;
删除表：drop table tablename;

  example:
      create table aaa(
      id int primary key not null auto_increment,
      name varchar(30),
      age tinyint(3) unsigned default 0,
      high decimal(5,2),
      gender enum("man", "woman", "secret") default "secret",
      cls_id int unsigned
      );

- 插入数据：insert  into tablename values（0, “name”,  age, height, "man", 0）;
查询数据：select * from tablename where 条件;
example:  select name as 姓名, height as 身高 from tablename where age > 18 and others;
- 添加字段：alter table tablename add birthday datetime;
修改字段参数：alter table tablename modify birthday date; 
修改字段名称及参数：alter table tablename change birthday birth date default "2000-01-01";
删除字段：alter table tablename drop height;

## 分支主题 3

*XMind - Trial Version*