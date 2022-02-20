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
	FOREIGN KEY("bandID") REFERENCES "Band"("bandID")
);

CREATE TABLE "Track" (
	"trackID"	INTEGER NOT NULL UNIQUE,
	"releaseID"	INTEGER NOT NULL,
	"NAME"	VARCHAR(50),
	"length"	INTEGER,
	FOREIGN KEY("releaseID") REFERENCES "Release"("releaseID") ON DELETE CASCADE,
	PRIMARY KEY("trackID")
);

INSERT INTO Band (name) VALUES
	("agency you"),
	("reach residents"),
	("limit harmful"),
	("agency you"),
	("vast gravity"),
	("whole pop"),
	("yea immune"),
	("component drivers"),
	("till intended"),
	("near perform");

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