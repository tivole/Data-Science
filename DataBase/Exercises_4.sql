/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 45
*/

-- 1
SELECT COUNT(student_id) FROM EXAM_MARKS WHERE subj_id = 22;

-- 2
SELECT COUNT(DISTINCT subj_id) FROM EXAM_MARKS;

-- 3
SELECT student_id, min(mark) FROM EXAM_MARKS GROUP BY student_id;

-- 4
SELECT student_id, max(mark) FROM EXAM_MARKS GROUP BY student_id;

-- 5
SELECT surname FROM STUDENT GROUP BY surname HAVING surname LIKE 'И%';

-- 6
SELECT subj_name, max(semester) FROM SUBJECTS GROUP BY subj_name;

-- 7
SELECT exam_date, count(student_id) FROM EXAM_MARKS GROUP BY exam_date;

-- 8
SELECT subj_id, AVG(mark) FROM EXAM_MARKS GROUP BY subj_id;

-- 9
SELECT student_id, AVG(mark) FROM EXAM_MARKS GROUP BY student_id;

-- 10
SELECT exam_id, AVG(mark) FROM EXAM_MARKS GROUP BY exam_id;

-- 11
SELECT exam_id, COUNT(student_id) FROM EXAM_MARKS GROUP BY exam_id;

-- 12
SELECT semester, COUNT(subj_id) FROM SUBJECTS GROUP BY semester;

