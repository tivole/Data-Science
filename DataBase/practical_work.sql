-- справочник персоналий участников конференции 
CREATE TABLE personalities (
    personality_id INTEGER NOT NULL PRIMARY KEY, -- ID
    surname NVARCHAR(35), -- фамилия
    firstname NVARCHAR(35), -- имя
    patronymic NVARCHAR(35), -- отчество
    academic_degree NVARCHAR(35), -- ученая степень
    academic_rank NVARCHAR(35), -- ученое звание
    scientific_direction NVARCHAR(35), -- научное направление
    place_of_work NVARCHAR(70), -- место работы
    department NVARCHAR(70), -- кафедра
    position NVARCHAR(70), -- должность
    country NVARCHAR(70), -- страна
    city NVARCHAR(35), -- город
    postcode NVARCHAR(9), -- почтовый индекс
    home_address NVARCHAR(70), -- адрес
    work_phone NVARCHAR(15), -- рабочий телефон 
    home_phone NVARCHAR(15), -- домашний телефон
    e_mail NVARCHAR(255) -- e-mail
);

-- информация, связанная с участием в конференции
CREATE TABLE participation_information (
    information_id INTEGER NOT NULL PRIMARY KEY, -- ID
    speaker_or_participant NVARCHAR(15), -- докладчик или участник
    first_inv_date DATE, -- дата рассылки 1-го приглашения
    application_date  DATE, -- дата поступления заявки
    topic NVARCHAR(255), -- тема доклада
    abstract_entry_mark NVARCHAR(35), -- отметка о поступлении тезисов
    second_inv_date DATE, --  дата рассылки 2-го приглашения
    date_of_registration_fee DATE, -- дата поступления оргвзноса
    amount_of_the_registration_fee FLOAT, -- размер поступившего оргвзноса
    date_of_arrival DATE, -- дата приезда
    departure_date DATE, -- дата отъезда
    hotel_need BOOLEAN -- потребность в гостинице
);