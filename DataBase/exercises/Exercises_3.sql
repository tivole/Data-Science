/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 42
*/

-- 1
SELECT concat(student_id,';', UPPER(surname),';', UPPER(firstname),';', stipend,';', kurs,';', city,';', birthday,';', univ_id) FROM STUDENT;

-- 2
SELECT CONCAT(SUBSTRING(firstname, 1, 1),'.', UPPER(surname),';', 'местожительства-', UPPER(city),';', 'родился-', CONVERT(Varchar(10), birthday, 105) ) FROM STUDENT;

-- 3
SELECT CONCAT(SUBSTRING(LOWER(firstname), 1, 1),'.', LOWER(surname),';', 'местожительства-', LOWER(city),';', 'родился:', CONVERT(Varchar(10), birthday, 106) ) FROM STUDENT;

-- 4
SELECT CONCAT(firstname,' ', surname, ' родился в ', year(birthday), ' году') FROM STUDENT;

-- 5
SELECT surname, firstname, stipend*100 FROM STUDENT;

-- 6
SELECT CONCAT(UPPER(firstname),' ', UPPER(surname), ' родился/ась в ', year(birthday), ' году') FROM STUDENT WHERE kurs IN (1,2,4);

-- 7
SELECT CONCAT('Код-', univ_id, ';', univ_name, '-г.   ', UPPER(city), ';', 'Рейтинг=', rating) FROM UNIVERSITY;

-- 8
SELECT CONCAT('Код-', univ_id, ';', univ_name, '-г.   ', UPPER(city), ';', 'Рейтинг=', ROUND(rating, -1)) FROM UNIVERSITY;
