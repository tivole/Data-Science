/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3

    Exercises from page 27 and 28.
*/

-- 11
SELECT * FROM STUDENT WHERE (stipend < 100 OR NOT ( birthday >= '10-03-1980' and student_id > 103));

-- 12
SELECT * FROM STUDENT where NOT ((birthday = '10-03-1980' or stipend > 100) and student_id >= 103);
