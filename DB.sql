CREATE Table Subject
(
SID SERIAL PRIMARY KEY ,
SUBJECT varchar(50)     
);

CREATE TABLE Questions
(
QNO SERIAL PRIMARY KEY,
Question varchar(1000),
OptnA varchar(500),
OptnB varchar(500),
OptnC varchar(500),
OptnD varchar(500),
OptnAns varchar(500),
SID integer references Subject(SID)     
);

CREATE Table Student_Quiz
(
SQID SERIAL PRIMARY KEY,
id integer references public."Student_student"(id),
QNO integer references Questions(QNO),
ANS varchar(500),
StartTime timestamp,
EndTime timestamp,
);

CREATE Table Student_Result
(
SRID SERIAL PRIMARY KEY,
id integer references public."Student_student"(id),
SID integer references Subject(SID),
Marks integer,
QuizDate date
)


SELECT * FROM questions OFFSET floor(random() * (SELECT COUNT(*) FROM questions Where sid = 1)) LIMIT 2;


create table Company
(
CompId SERIAL PRIMARY KEY,
CompName varchar(200),
CompEmail varchar(200),
CompPhone bigint,
CompAddress varchar(300),
CompDetails varchar(500)
);


create Table Student_Company
(
SCID SERIAL PRIMARY KEY,
CompId integer references Company(CompId),
id integer references public."Student_student"(id) 
);


create table CompNotification
(
CNID SERIAL PRIMARY KEY,
CompId integer references Company(CompId),
startDate date,
endDate date,
message varchar(300)
);
