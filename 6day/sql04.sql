-- SQL04.sql

-- 직원들의 수?
select count(empno)
from emp;
--group by 1; 오라클은 하나의 그룹으로 봐라라는 뜻으로 됨

-- 업무당 인원수는?
select job, count(empno)
from emp
group by job;

-- job의 갯수는?
select count(DISTINCT job)
from emp;
-- 중복을 줄이는것은 DISTINCT

-- 커미션을 받는 직원들의 수는?
select count(comm)
from emp
where (comm >0);

-- 직원들의 평균급여, 최소급여, 최대급여, 급여합산은?
select round(avg(sal)), min(sal), max(sal), sum(sal)
from emp;

select job, count(empno), round(avg(sal)), min(sal), max(sal), sum(sal)
from emp
group by job;

--	부서번호별 인원수와 최대급여는?
SELECT deptno, count(empno), max(sal)
from emp
group by deptno;