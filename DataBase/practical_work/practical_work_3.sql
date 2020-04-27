-- 1
SELECT
    p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i
    ON (i.information_id = b.information_id)
WHERE (i.first_inv_date = '2020-04-17');

-- 2