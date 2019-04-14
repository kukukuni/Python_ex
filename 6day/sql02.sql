-- SQL02.sql

-- 스미스의 이름, 사번은?

SELECT ename, empno
from emp
where (ename = 'SMITH'); -- 값은 대소문자를 가려서 smith치면 안됨, mssql제외 대부분은 가림림

-- clerk 업무를 하는 직원들의 이름, 사번, 업무는?

select ename, empno, job
FROM emp
where (job = 'CLERK');


-- 급여가 1350이상, empno 7700초과 인 직원들의 이름, 사번, 급여는?
select ename, empno, sal
FROM emp
where (sal >=1350) & (empno>7700);

-- 커미션이 없는 지원들의 이름, 사번, 커미션은?
SELECT ename, empno, comm
from emp
--where (comm = 0) or (comm is null); --null은 상태이기 때문에 is이다. and, or, not가능
where not ( comm > 0); --언어별로 다른데 0말고 null도 넣어주기도 한다.

SELECT ename, empno, ifnull(comm,0)
from emp
where (ifnull (comm, 0)  ==0); --null이면 뒤의 값으로 바꿔주는 역할

-- 부서번호가 10인 직원들의 이름, 사번, 업무, 부서번호는?
SELECT ename, empno, job, deptno
from emp
where (deptno=10);

--상관의 사번이 7566인 직원들의 이름, 사번, 상관의 사번은?

select ename, empno, mgr
from emp
where (mgr=7566);