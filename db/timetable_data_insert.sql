INSERT INTO building (building_name)
VALUES
	('Anglesea'),
	('Liongate'),
	('Park'),
	('Richmond');

INSERT INTO lecturer (
	lecturer_fname,
	lecturer_lname,
	lecturer_availability
)

VALUES

	('John','Smith','EX001'),
	('Lisa','Franklin','EX003'),
	('Herbert','Jones','EX009'),
	('Richard','Johnson','EX004'),
	('Hugh','Piper','EX006'),
	('Javier','Rodriguez','EX007'),
	('Kathlyn','Ferguson','EX008');

INSERT INTO modules (
	mod_name,
	mod_enrolled,
	mod_lectures,
	mod_practicals,
	mod_tutorials
)

VALUES

	('Comp Tutorial Level 4','200','0','0','1'),
	('Programming','200','1','2','0'),
	('Networks','200','1','1','0'),
	('Database Systems Development','200','1','2','0'),
	('Core Computing Concepts','200','1','1','0'),
	('Architecture and Operating Systems','200','1','2','0');
