/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3

    Exercises from page 28 and 31.
*/


SELECT * FROM STUDENT WHERE (stipend < 100 OR NOT ( birthday >= '10-03-1980' and student_id > 103));
SELECT * FROM STUDENT where NOT ((birthday = '10-03-1980' or stipend > 100) and student_id >= 103);
SELECT * from Exam_Marks where exam_date BETWEEN '2000-01-22' AND '2000-01-24';
SELECT * from Exam_Marks where student_id IN (12, 32);
SELECT * from STUDENT where name like 'I%' or name LIKE 'S%';
SELECT * from Exam_Marks where mark IS NULL;
SELECT * from Exam_Marks where mark NOT NULL;