-- SQL05.sql

-- smith의 부서명은?
SELECT ename, dname
FROM emp, dept
Where (emp.deptno = dept.deptno) and (ename = 'SMITH');
-- Table의 갯수 -1만큼 조인조건이 생겨야함

-- SALES 부서의 직원 이름, 사번은?
SELECT ename, empno
from emp, dept
where (emp.deptno = dept.deptno) and (dname = 'SALES');


-- CLERK  업무를 하는 직원들의 이름, 사번, 부서명, 부서위치는?
select ename, empno, dname, loc
from emp, dept
where (emp.deptno = dept.deptno) and (job = 'CLERK');

-- DALLAS 에서 일하는 직원들의 부서명, 부서위치, 부서번호, 이름, 사번은?
select dname, loc, emp.deptno, ename, empno     --시스템은  두개에서 deptno있으면 뭔지 모르고 오류내서
																						-- 지정해주는 것이 좋다.
from emp, dept
where (emp.deptno = dept.deptno) and (dept.loc = 'DALLAS');

select d.dname, d.loc, e.deptno, e.ename, e.empno   -- 변수로 지정가능
from emp e, dept d
where (e.deptno = d.deptno) and (d.loc = 'DALLAS');

-- 급여가 1500 ~ 2500 사이인 직원들의 이름, 부서명, 급여는?
select e.ename, d.dname, e.sal
from emp e, dept d
where (e.deptno = d.deptno) and (e.sal <2500) and (e.sal>1500);

-- 부서별 직원들의 평균급여, 최소급여, 최대급여, 급여합산은?
-- 부서이름은 내림차순으로 정렬
select d.dname, round(avg(e.sal)), min(e.sal), max(e.sal), sum(e.sal)
from emp e, dept d
where (e.deptno = d.deptno)     
group by d.dname
order by d.dname desc;

-- 업무별 급여합산액이 6000 이상인 업무와 급여합산액은?
select job, sum(sal)
from emp
group by job 
having (sum(sal) > 6000);

-- 업무별 인원수가 3명 미만인 업무와 인원수는?
select job, count(empno)
from emp
group by job 
having (count(empno) < 3);

-- 부서별 급여 최대값이 3000 이하인 부서와 급여합산액은?
select d.dname, max(e.sal)
from emp e, dept d
where (e.deptno = d.deptno)   
group by e.deptno
having (max(sal) <= 3000);

select ename, sal, comm, sal*12, sal*12 + ifnull(comm ,0) as total-- 1년치 급여
from emp;

-- 직원들 중 1년 수입이 20000이 넘는 직원들의 이름, 부서명, 1년 수입은?
-- 1년 수입 : 12개월 급여 + 커미션
select ename, dname, sal*12 + ifnull(comm,0) as Money
from emp, dept
where (emp.deptno = dept.deptno) and Money>20000  ;

-- 부서별 평균 1년 수입금액이 25000이 넘는 부서별 평균 1년 수입금액은?
-- 1년 수입 : 12개월 급여 + 커미션
select dname, round(avg(sal*12 + ifnull(comm,0))) as Money
from emp, dept
where (emp.deptno = dept.deptno) 
group by dname
having Money>25000 ;