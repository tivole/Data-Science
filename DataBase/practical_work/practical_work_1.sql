-- справочник персоналий участников конференции 
CREATE TABLE personalities
(
    -- ID
    personality_id INTEGER NOT NULL PRIMARY KEY,

    -- фамилия
    surname NVARCHAR(35),

    -- имя
    firstname NVARCHAR(35),

    -- отчество
    patronymic NVARCHAR(35),

    -- ученая степень
    academic_degree NVARCHAR(35),

    -- ученое звание
    academic_rank NVARCHAR(35),

    -- научное направление
    scientific_direction NVARCHAR(35),

    -- место работы
    place_of_work NVARCHAR(70),

    -- кафедра
    department NVARCHAR(70),

    -- должность
    position NVARCHAR(70),

    -- страна
    country NVARCHAR(70),

    -- город
    city NVARCHAR(35),

    -- почтовый индекс
    postcode NVARCHAR(9),

    -- адрес
    home_address NVARCHAR(70),

    -- рабочий телефон 
    work_phone NVARCHAR(15),

    -- домашний телефон
    home_phone NVARCHAR(15),

    -- e-mail
    e_mail NVARCHAR(255)
);


-- информация, связанная с участием в конференции
CREATE TABLE participation_information
(
    -- ID
    information_id INTEGER NOT NULL PRIMARY KEY,

    -- докладчик или участник
    speaker_or_participant NVARCHAR(15),

    -- дата рассылки 1-го приглашения
    first_inv_date DATE,

    -- дата поступления заявки
    application_date DATE,

    -- тема доклада
    topic NVARCHAR(255),

    -- отметка о поступлении тезисов
    abstract_entry_mark NVARCHAR(35),

    --  дата рассылки 2-го приглашения
    second_inv_date DATE,

    -- дата поступления оргвзноса
    date_of_registration_fee DATE,

    -- размер поступившего оргвзноса
    amount_of_the_registration_fee FLOAT,

    -- дата приезда
    date_of_arrival DATE,

    -- дата отъезда
    departure_date DATE,

    -- потребность в гостинице
    hotel_need BOOLEAN
);


-- таблица связывающая таблицу "personalities" с таблицой "participation_information"
CREATE TABLE personal_information
(
    id INTEGER NOT NULL PRIMARY KEY,

    CONSTRAINT personality_id FOREIGN KEY (personality_id)
        REFERENCES personalities(personality_id),

    CONSTRAINT information_id FOREIGN KEY (information_id)
        REFERENCES participation_information(information_id),
);
