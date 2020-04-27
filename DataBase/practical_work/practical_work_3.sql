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
SELECT p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i ON (i.information_id = b.information_id)
WHERE (i.date_of_registration_fee = '2020-04-24' AND i.amount_of_the_registration_fee > 100);

-- 3
SELECT p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i
    ON (i.information_id = b.information_id)
WHERE (i.date_of_registration_fee = '2020-04-24');

-- 4
SELECT p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i
    ON (i.information_id = b.information_id)
WHERE (i.date_of_registration_fee BETWEEN '2020-04-22' AND '2020-04-25');

-- 5
SELECT i.topic
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i
    ON (i.information_id = b.information_id)
WHERE (p.city = 'Moscow');

-- 6
SELECT p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i
    ON (i.information_id = b.information_id)
WHERE (p.city = 'Moscow' AND i.hotel_need = TRUE);