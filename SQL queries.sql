/* TABLE CREATION */

CREATE TABLE "Publisher" (
	"publisherID"	INTEGER NOT NULL UNIQUE,
	"name"	VARCAHR(50),
	PRIMARY KEY("publisherID")
);

CREATE TABLE "Band" (
	"bandID"	INTEGER NOT NULL UNIQUE,
	"publisherID"	INTEGER,
	"name"	VARCHAR(50),
	"creationDate"	VARCHAR(50),
	FOREIGN KEY("publisherID") REFERENCES "Publisher"("publisherID") ON DELETE CASCADE,
	PRIMARY KEY("bandID")
);

CREATE TABLE "Member" (
	"memberID"	INTEGER NOT NULL UNIQUE,
	"firstName"	VARCHAR(50),
	"lastName"	VARCHAR(50),
	PRIMARY KEY("memberID")
);

CREATE TABLE "MembersInBands" (
	"bandID"	INTEGER NOT NULL,
	"memberID"	INTEGER,
	FOREIGN KEY("bandID") REFERENCES "Band"("bandID"),
	FOREIGN KEY("memberID") REFERENCES "Member"("memberID")
);

CREATE TABLE "Release" (
	"releaseID"	INTEGER NOT NULL UNIQUE,
	"bandID"	INTEGER NOT NULL,
	"name"	VARCHAR(50),
	"type"	VARCHAR(50),
	"date"	VARCHAR(50),
	PRIMARY KEY("releaseID"),
	FOREIGN KEY("bandID") REFERENCES "Band"("bandID") ON DELETE CASCADE
);

CREATE TABLE "Track" (
	"trackID"	INTEGER NOT NULL UNIQUE,
	"releaseID"	INTEGER NOT NULL,
	"NAME"	VARCHAR(50),
	"length"	INTEGER,
	FOREIGN KEY("releaseID") REFERENCES "Release"("releaseID") ON DELETE CASCADE,
	PRIMARY KEY("trackID")
);

INSERT INTO Band (name, publisherID) VALUES
	("agency you", NULL),
	("reach residents", 1),
	("limit harmful", 3),
	("agency you", 5),
	("vast gravity", NULL),
	("whole pop", NULL),
	("yea immune", 1),
	("component drivers", 2),
	("till intended", NULL),
	("near perform", 5);

INSERT INTO Member (firstName, lastName) VALUES
	('Thad', 'Hubbartt'),
	('Daniela', 'Ephriam'),
	('Kermit', 'Offret'),
	('Valeri', 'Friday'),
	('Josephina', 'Jacobus'),
	('Cathey', 'Detone'),
	('Sherryl', 'Lesa'),
	('Zenia', 'Mccord'),
	('Sheena', 'Yankee'),
	('Vivan', 'Bazil'),
	('Sherri', 'Prosch'),
	('Le', 'Betit'),
	('Ceola', 'Nahl'),
	('Lenora', 'Daichendt'),
	('Dalton', 'Romaine'),
	('Brande', 'Mangina'),
	('Renata', 'Wolnik'),
	('Teodoro', 'Millimaki'),
	('Zella', 'Yusef'),
	('Breann', 'Zilka');

INSERT INTO MembersInBands (bandID, memberID) VALUES
	(1,1),
	(1,2),
	(2,3),
	(2,1),
	(2,4),
	(3,5),
	(4,6),
	(4,7),
	(4,4),
	(5,8),
	(5,9),
	(5,10),
	(5,11),
	(6,12),
	(6,10),
	(6,9),
	(7,13),
	(7,14),
	(7,17),
	(8,15),
	(8,16),
	(8,17),
	(9,18),
	(9,11),
	(10,19),
	(10,20);

INSERT INTO Publisher (name) VALUES
	("cent cells LTD"),
	("near perform productions"),
	("coming revolution LTD"),
	("fatal conservation LTD"),
	("options partners productions");

INSERT INTO Release (bandID, name) VALUES
	(1, "lexington"),
	(2, "planets"),
	(3, "pushed"),
	(4, "hearts"),
	(5, "help"),
	(6, "complaints"),
	(7, "retention"),
	(8, "adjustable"),
	(9, "normal"),
	(1, "overseas"),
	(1, "adult"),
	(2, "bye"),
	(3, "conventions"),
	(4, "battery"),
	(5, "outstanding"),
	(6, "experiments"),
	(7, "excluded"),
	(8, "approximate"),
	(9, "wu"),
	(10, "emergency");

/* INSERT INTO Track (releaseID, name, length) VALUES */