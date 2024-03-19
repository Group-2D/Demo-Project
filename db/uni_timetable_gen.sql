CREATE DATABASE timetable_gen;
\c timetable_gen


CREATE TABLE modules (
	mod_id SERIAL PRIMARY KEY,
	mod_name VARCHAR(40) NOT NULL,
	mod_enrolled INT NOT NULL,
	mod_lectures INT NOT NULL,
	mod_practicals INT NOT NULL,
	mod_tutorials INT NOT NULL
);

CREATE TABLE lecturer (
	lecturer_id SERIAL PRIMARY KEY,
	lecturer_fname VARCHAR(20) NOT NULL,
	lecturer_lname VARCHAR(20) NOT NULL,
	lecturer_availability VARCHAR(100)
);

CREATE TABLE building (
	building_id SERIAL PRIMARY KEY,
	building_name VARCHAR(20)
);

CREATE TABLE room (
	room_id SERIAL PRIMARY KEY,
	room_name VARCHAR(30),
	room_capacity INT NOT NULL,
	building_id INT NOT NULL REFERENCES building(building_id)
);

CREATE TABLE lecture (
	lecture_id SERIAL PRIMARY KEY,
	mod_id INT NOT NULL REFERENCES modules(mod_id),
	room_id INT NOT NULL REFERENCES room(room_id),
	lecturer_id INT NOT NULL REFERENCES lecturer(lecturer_id),
	lecture_start DECIMAL,
	lecture_end DECIMAL
);
