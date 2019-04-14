-- SQL08.sql

-- SCOTT 과 같은 급여를 받는 직원의 이름과 급여는?
--1) SCOTT의 급여는?
select sal
FROM emp
where (ename = 'SCOTT');
--2) 그 급여를 받는 직원의 이름과 급여는?
select ename, sal
from emp
where (sal = 3000);

--3) 결합
select ename, sal
from emp
where (sal = (select sal
						FROM emp
						where (ename = 'SCOTT')));
						
-- 전 직원의 평균급여보다 많이 받는 직원들의 이름, 사번, 급여는?
select ename, empno, sal
from emp
where (sal > (SELECT avg(sal)
						       FROM emp));

-- 전 직원의 평균급여보다 많이 받는 직원들의 이름, 사번, 급여, 급여등급, 부서명은?
select e.ename, e.empno, e.sal, s.grade, d.dname
from emp e join dept d USING(deptno), salgrade s
where (e.sal BETWEEN s.losal and s.hisal)  and (e.sal > (SELECT avg(e.sal)
						       FROM emp));
