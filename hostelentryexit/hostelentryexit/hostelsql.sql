CREATE TABLE hostel_db (h_num INTEGER NOT NULL PRIMARY KEY, 
username VARCHAR(20) NOT NULL, password VARCHAR(20) NOT NULL);

INSERT INTO hostel_db (h_num, username, password)
VALUES (1, "guard1", "queenofcampus");
INSERT INTO hostel_db (h_num, username, password)
VALUES (16, "guard16", "olympus");



SELECT * FROM hostel_db;