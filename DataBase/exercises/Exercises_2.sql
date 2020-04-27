/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3

    Exercises from page 31
*/

-- 1
SELECT * FROM Exam_Marks WHERE exam_date BETWEEN '1999-01-10' AND '1999-01-20';

-- 2
SELECT * FROM Exam_Marks WHERE student_id IN (12, 32);

-- 3
SELECT * FROM SUBJECT_TABLE WHERE SUBJ_NAME LIKE 'И%';

-- 4
SELECT * FROM STUDENT WHERE FIRSTNAME LIKE 'И%' OR name LIKE 'С%';

-- 5
SELECT * FROM Exam_Marks WHERE mark IS NULL;

-- 6
SELECT * FROM Exam_Marks WHERE mark NOT NULL;