-- SQL06.sql

-- SMITH의 이름, 급여, 급여등급은?
SELECT e.ename, e.sal, s.grade
FROM emp e, salgrade s
WHERE (e.sal BETWEEN s.losal and s.hisal) and e.ename = 'SMITH';

-- 3등급의 급여등급을 가지고 있는 직원들의 이름, 급여, 급여등급은?
select e.ename, e.sal, s.grade
from emp e, salgrade s
where (e.sal BETWEEN s.losal and s.hisal) and (grade = 3);

-- 급여가 1401~2000 인 직원들의 이름, 급여, 급여등급, 부서명은?
select e.ename, e.sal, s.grade, d.dname
from emp e, salgrade s, dept d
where (e.sal BETWEEN s.losal and s.hisal) and (e.deptno = d.deptno) and (grade = 3);
-- 마지막을 (e.sal BETWEEN 1401 and 2000)으로 해도 됨

-- 시카고에서 근무하는 직원들의 이름, 부서명, 위치, 급여, 급여등급은?
select e.ename, d.dname, d.loc, e.sal, s.grade
from emp e, salgrade s, dept d
where (e.sal BETWEEN s.losal and s.hisal) and (e.deptno = d.deptno) and (loc = 'CHICAGO')
order by (grade);

-- SMITH의 이름, 사번, 상관의 이름, 사번은?
select e.ename, e.empno, h.ename, h.empno
from emp e, emp h
where (e.mgr = h.empno)and (e.ename = 'SMITH');
-- 테이블을 복사하여 자기참조를 한다.

--  SMITH의 이름, 사번, 부서명, 상관의 이름, 사번, 부서명은?
select  ee.ename, ee.empno, de.dname, em.ename, em.empno, de.dname
FROM emp ee, emp em, dept de, dept dm
WHERE (ee.mgr = em.empno) and (ee.deptno = de.deptno) and (em.deptno = dm.deptno)
				and (ee.ename = 'SMITH');

--  SMITH의 이름, 사번, 부서명, 상관의 이름, 사번, 급여, 급여등급은?
select  ee.ename, ee.empno, de.dname, em.ename, em.empno, em.sal, sm.grade
FROM emp ee, emp em, dept de, dept dm, salgrade se, salgrade sm
WHERE (ee.mgr = em.empno) and (ee.deptno = de.deptno) and (em.deptno = dm.deptno)
				and (ee.sal BETWEEN se.losal and se.hisal) and (em.sal BETWEEN sm.losal and sm.hisal)
				and (ee.ename = 'SMITH');
				
--  SMITH의 이름, 사번, 부서명, 상관의 이름, 사번, 급여등급, 부서명은?
select  ee.ename, ee.empno, de.dname, em.ename, em.empno, sm.grade, dm.dname
FROM emp ee, emp em, dept de, dept dm, salgrade se, salgrade sm
WHERE (ee.mgr = em.empno) and (ee.deptno = de.deptno) and (em.deptno = dm.deptno)
				and (ee.sal BETWEEN se.losal and se.hisal) and (em.sal BETWEEN sm.losal and sm.hisal)
				and (ee.ename = 'SMITH');




