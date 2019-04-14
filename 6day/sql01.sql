-- SQL01.sql
select * 
from emp;

-- 직원들의 이름, 사번, 업무(JOB)은?
select ename, empno, job
from emp;

--부서들의 부서명, 부서위치는?
SELECT dname, loc
from dept;

-- 1 + 2 ?
select 1 + 2;

-- 직원들의 이름, 사번, 급여?
SELECT ename as '이름',
			   empno as "사번",
			   sal as 급여
from emp;

select  ename || empno
from emp; --병합한다.

select  ename || "의 사번은 " || empno as "사람들의 사번"
from emp; --병합한다.

--직원들의 업무(Job)은?
select DISTINCT job
FROM emp;

--직원들의 업무, 이름, 사번?
SELECT job, ename, empno
FROM	emp
order by job ASC, ename desc;  --기본적으로는  ASC이다.

-- 직원들의 이름, 사번, 상관의 사번
-- 상관의 사번 순으로 정리하세요.
SELECT job, empno, mgr
from emp
order by mgr;   -- Null이 가장 앞에 온다.

