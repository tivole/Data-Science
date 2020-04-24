/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 55
*/

-- 1
SELECT mark 
FROM EXAM_MARKS 
WHERE student_id = 
	(SELECT student_id 
	FROM STUDENT 
	WHERE surname = 'Зайцева');

-- 2
SELECT DISTINCT firstname 
FROM STUDENT, EXAM_MARKS 
WHERE mark > 
	(SELECT AVG(mark) 
	FROM EXAM_MARKS) 
	AND STUDENT.student_id = EXAM_MARKS.student_id 
	AND subj_id = 10;
 
-- 3
SELECT DISTINCT firstname 
FROM STUDENT, EXAM_MARKS 
WHERE mark < 
	(SELECT AVG(mark) 
	FROM EXAM_MARKS) 
	AND STUDENT.student_id = EXAM_MARKS.student_id 
	AND subj_id = 22;

-- 4
SELECT student_id, COUNT(subj_id) 
FROM EXAM_MARKS 
GROUP BY student_id 
HAVING COUNT(subj_id) > 1;

-- 5
SELECT student_id, firstname, stipend 
FROM STUDENT A 
WHERE stipend = 
	(SELECT MAX(stipend) 
	FROM STUDENT B 
	WHERE A.city = B.city);

-- 6
SELECT student_id, firstname 
FROM STUDENT A 
WHERE A.city IS NOT NULL 
AND city NOT IN 
	(SELECT B.city 
	FROM UNIVERSITY B);

-- 7 (а)
SELECT DISTINCT student_id, firstname, univ_name, A.city 
FROM STUDENT A, UNIVERSITY B 
WHERE A.city < > B.city 
AND A.city IS NOT NULL 
AND A.univ_id = B.univ_id;

-- 7 (б)
SELECT DISTINCT student_id, firstname 
FROM STUDENT A 
WHERE city NOT IN 
	(SELECT city 
	FROM UNIVERSITY B 
	WHERE A.univ_id = B.univ_id);
