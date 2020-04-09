/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 42
*/

-- 1
SELECT student_id||';'||UPPER(surname)||';'||UPPER(firstname)||';'||stipend||';'||UPPER(City)||';'||birthday||';'||univ_id from STUDENT;

-- 2
SELECT SUBSTR(firstname, 1, 1)||'.'||UPPER(surname)||';местожительства-'||UPPER(city)||';родился-'||birthday from STUDENT;

-- 3
