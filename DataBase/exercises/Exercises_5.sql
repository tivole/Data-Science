/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 50
*/

-- 1 (a)
SELECT student_id, surname, stipend*1.2 FROM STUDENT ORDER BY 3;

-- 1 (б)
SELECT student_id, surname, stipend*1.2 FROM STUDENT ORDER BY 2;

-- 2 (а)
SELECT student_id, max(mark) FROM EXAM_MARKS GROUP BY student_id ORDER BY student_id;

-- 2 (б)
SELECT student_id, min(mark) FROM EXAM_MARKS GROUP BY student_id ORDER BY student_id;

-- 3 (а)
SELECT semester, subj_name, subj_id FROM SUBJECTS GROUP BY semester, subj_name, subj_id ORDER BY semester DESC;

-- 3 (б)
SELECT hour, subj_name, subj_id FROM SUBJECTS GROUP BY hour, subj_name, subj_id ORDER BY hour ASC;

-- 4
SELECT exam_date, SUM(mark) FROM EXAM_MARKS GROUP BY exam_date ORDER BY 2 DESC;

-- 5 (а)
SELECT exam_date, AVG(mark) FROM EXAM_MARKS GROUP BY exam_date ORDER BY 2 DESC;

-- 5 (б)
SELECT exam_date, MIN(mark) FROM EXAM_MARKS GROUP BY exam_date ORDER BY 2 DESC;

-- 5 (в)
SELECT exam_date, MAX(mark) FROM EXAM_MARKS GROUP BY exam_date ORDER BY 2 DESC;
