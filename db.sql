# DBMS: MySQL

DROP DATABASE IF EXISTS cs165;
CREATE DATABASE cs165;

USE cs165;

DROP TABLE IF EXISTS bank;
CREATE TABLE bank (
  bankName varchar(50),
  bankMainAddress varchar(255),
  PRIMARY KEY (bankName)
);

DROP TABLE IF EXISTS branch;
CREATE TABLE branch (
  bankBranchName varchar(50),
  bankBranchAddress varchar(255),
  bankName varchar(50),
  PRIMARY KEY (bankBranchName),
  FOREIGN KEY (bankName) REFERENCES bank (bankName)
);

DROP TABLE IF EXISTS bankaccount;
CREATE TABLE bankaccount (
  bankNo decimal(20,0),
  bankName varchar(50),
  bankBranchName varchar(50),
  PRIMARY KEY (bankNo, bankName),
  FOREIGN KEY (bankName) REFERENCES bank (bankName),
  FOREIGN KEY (bankBranchName) REFERENCES branch (bankBranchName)
);

INSERT INTO bank VALUES
    ("Metrobank","Metrobank Plaza, Sen. Gil J. Puyat Avenue, Makati City"),
    ("Unionbank of the Philippines","UnionBank Plaza Bldg., Meralco Avenue, Pasig City"),
    ("Land Bank of the Philippines","LANDBANK Plaza, 1598 M.H. del Pilar, Manila City"),
    ("Banco de Oro","7899 Makati Avenue, Makati City"),
    ("Bank of the Philippine Islands", "6768 Ayala Avenue, Makati City");

INSERT INTO branch VALUES
    ("BPI UP Town Center", "Unit C145A L1 Phase 2, UP Town Center, Katipunan Avenue, Quezon City", "Bank of the Philippine Islands"),
    ("BPI Loyola-Katipunan", "299 Katipunan Avenue, Quezon City", "Bank of the Philippine Islands"),
    ("BDO Katipunan", "Regis Center, 327 Katipunan Avenue, Quezon City", "Banco de Oro"),
    ("Metrobank Katipunan", "339 Katipunan Avenue, Quezon City", "Metrobank"),
    ("Metrobank Blue Ridge", "222 Katipunan Avenue, Quezon City", "Metrobank");

INSERT INTO bankaccount VALUES
    (123756789122421,"Bank of the Philippine Islands", "BPI UP Town Center"),
    (341256989113453,"Bank of the Philippine Islands", "BPI Loyola-Katipunan"),
    (563412089153456,"Banco de Oro", "BDO Katipunan"),
    (783456389121450,"Metrobank", "Metrobank Katipunan"),
    (903456189125451,"Metrobank", "Metrobank Blue Ridge");