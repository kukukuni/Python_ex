-- SQL07.sql

select * from dept;

-- 부서별 소속직원 이름, 사번, 업무 (단, 모든 부서명 게시)
select  d.dname, e.ename, e.empno, e.job
FROM dept d, emp e
WHERE (d.deptno = e.deptno);
-----------------------------------------------------------------------------------------------------
-->emp2, dept2
select * from emp2;
select * from dept2;

select *
from emp2 e, dept2 d
where (e.deptno = d.deptno) --이건 표준은 아니다. 개발자들이 좋아함
and (e.ename = 'Jane');

select *
from emp2 e join dept2 d on  (e.deptno = d.deptno) --이건 ANSI 표준이다. 무조건 어떤 쿼리든 되기때문에	
where (e.ename = 'Jane');												  --이관의 걱정이 없다.

select *
from emp2 e inner join dept2 d on (e.deptno = d.deptno); --이너조인은 양쪽의 같은것만 고르는 것

select *
from emp2 e NATURAL join dept2 d ;

select *
from emp2 e join dept2 d using  (deptno) ; --넷다 같은것인데, join과 inner를 가장 많이 사용

select *
from emp2 e left outer join dept2 d on (e.deptno = d.deptno); --join을 기준으로 왼쪽은 다 나와라

select *
from dept2 d left outer join emp2 e  on (e.deptno = d.deptno);  

-- 이 버전에서는 안되지만,
-- 항상 left/ right/ FULL outer join

 -- 없는것도 나오게할때 즉 Null도 나올때 outerjoin을 함
select d.dname, count(e.ename) 
FROM dept2 d left outer join emp2 e using(deptno)
GROUP by d.dname; 
-------------------------------------------------------------------------------------------------------------------
-- emp, dept
-- 모든 부서의 인원수와 평균 1년 수입금액은?

select d.dname, count(e.ename), round(avg(e.sal*12 + ifnull(e.comm,0))) 
FROM dept d left outer join emp e using(deptno)
group by d.dname
