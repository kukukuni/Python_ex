-------------------------------------------------

drop table emp2;
create table emp2 (ename varchar2(10), 
                   deptno number(2));

create table dept2 (dname varchar2(10),
                    deptno number(2)); 
                    
insert into emp2 values ('Jane',10);
insert into emp2 values ('Alice',10);
insert into emp2 values ('Sophia',20);
insert into emp2 values ('Tom',null);

select * from emp2;

insert into dept2 values ('HR',10);
insert into dept2 values ('SALES',20);
insert into dept2 values ('IT',null);

select * from emp2;
select * from dept2;

------------------------------------------------