select * from demo.user;

use demo;
select * from user;

select * from user;

-- CRUD

-- C
insert into `user` values (null, 'ck', 25);
insert into `user` values (null, 'ziqi', '18'); -- 隐身转换
insert into `user` (`id`, `name`, `age`) values (null, '赵杰飞', 30);
insert into `user` (`name`, `age`) values ('黄国强', 30);
insert into `user` (`age`, `name`) values ('50', '张益达');
insert into `user` (`name`) values ('test');

-- U
update user set name='宋振哲';
update user set name='宋振哲' where name='test';

-- update [TABLE_NAME] set [COL_NAME] = [NEW_VALUE] where <expression> ... 

-- D
delete from user;
delete from user where name = 'young';

-- TRUNCATE
truncate user;

drop user;

-- R
select * from user;
select id, name, age from user;
select name, age from user;

select name, age from user order by age desc;
select name, age from user order by age desc, name asc;

select count(id) from user;

select count(id) cn from user;
select count(id) 'id cn' from user;
select count(id) as 'id cn' from user;

select name, age, count(id) from user group by age;

select name, age, count(id) 'cn' from user group by age having cn > 1 and age < 20;

select id, name, age from user where name = 'miracle';
select id, name, age from user where name <> 'miracle';
select id, name, age from user where name != 'miracle';
select id, name, age from user where age > 16 and age < 40;
select id, name, age from user where age > 16 or age < 40;
select id, name, age from user where age between 18 and 30; -- between 是左闭右闭区间
select id, name, age from user where age in (20, 22, 24, 26, 28, 30);
select id, name, age from user where age not in (20, 22, 24, 26, 28, 30);
select id, name, age, type, address from user where address is NULL;
select id, name, age, type, address from user where address is not NULL;

-- 级联
-- 表在取别名的时候，不能有引号
select U.name, U.age, U.address, T.value from `user` U, `type` as T
where U.type = T.id; -- inner JOIN

select U.name, U.age, U.address, T.value
from `user` U
inner join `type` T on U.type = T.id;

select U.name, U.age, U.address, T.value
from `user` U
left join `type` T on U.type = T.id;

select U.name, U.age, U.address, T.value
from `type` T
left join `user` U on U.type = T.id;

select U.name, U.age, U.address, T.value
from `type` T
right join `user` U on U.type = T.id;

select U.name, U.age, U.address, T.value
from `type` T
cross join `user` U on U.type = T.id;


select * from `user`,`type`

-- Aggregation
select id, name, age, address, type from user;
select avg(age) from user;
select sum(age) from user;
select min(age), max(age) from user;

select name, age, case when age >30 then '中年人' when age <=30 then '青年人' end '年龄分布' from user;
select name, age, case age when 30 then '30岁' when 50 then '50岁' end 'age' from user;

select name, age, IF(address is null, '不存在地址', address) '地址?' from user;
select name, age, IFNULL(address, '不存在地址') from user;