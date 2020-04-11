/*
    SQL В ПРИМЕРАХ И ЗАДАЧАХ.
    ISBN 985-475-004-3
    Exercises from page 58
*/

-- 1
SELECT * FROM STUDENT A WHERE EXISTS (SELECT * FROM UNIVERSITY B WHERE A.univ_id = B.univ_id AND RATING>300);

-- 2
SELECT * FROM STUDENT A JOIN UNIVERSITY B ON A.univ_id = B.univ_id AND RATING > 300;