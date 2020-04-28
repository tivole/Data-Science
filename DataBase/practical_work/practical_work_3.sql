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
-- first solution
SELECT p.*
FROM personalities AS p
    INNER JOIN personal_information AS b
    ON (p.personality_id = b.personality_id)
    INNER JOIN participation_information AS i ON (i.information_id = b.information_id)
WHERE (i.date_of_registration_fee = '2020-04-24' AND i.amount_of_the_registration_fee > 100);

-- second solution
INSERT INTO personalities
    (
    surname,
    firstname,
    patronymic,
    academic_degree,
    academic_rank,
    scientific_direction,
    place_of_work,
    department,
    position,
    country,
    city,
    postcode,
    home_address,
    work_phone,
    home_phone,
    e_mail
    )
VALUES
    (
        99,
        'Lionel',
        'Rodrigo',
        'Sergio',
        'Doctor of Mathematics',
        'Docent',
        'Mathematics',
        'Moscow State University',
        'Discrete Mathematics',
        'Lecturer',
        'Russia',
        'Moscow',
        '191028',
        'g. MOSKVA, ul. Lesnaya d. 5, kv. 176',
        '+79535554156',
        '+79025556911',
        'torettoelovit@mail.ru'
    );

    INSERT INTO participation_information
    (
    speaker_or_participant,
    first_inv_date,
    application_date,
    topic,
    abstract_entry_mark,
    second_inv_date,
    date_of_registration_fee,
    amount_of_the_registration_fee,
    date_of_arrival,
    departure_date,
    hotel_need
    )
VALUES
    ( 
        99,
        'speaker',
        '2020-04-20',
        '2020-04-21',
        'Counting conjectures and beyond',
        'Entried',
        '2020-04-23',
        '2020-04-24',
        91.5,
        '2020-04-21',
        '2020-04-26',
        TRUE
    );

    INSERT INTO personal_information
    (
    personality_id,
    information_id
    )
VALUES
    (
        99,
        99
    );



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