from app import db
from datetime import datetime,date

# CREATE TABLE Bank (
#   bankName varchar(50),
#   bankMainAddress varchar(255),
#   PRIMARY KEY (bankName)
# );
class Bank(db.Model):
    bankName = db.Column(db.String(50), primary_key=True)
    bankMainAddress = db.Column(db.String(255))
    bankBranches = db.relationship("Branch", backref="bank")
    bankAccounts = db.relationship("BankAccount", backref="bank")
    # accounts = db.relationship("Account", backref="bank")

    def __repr__(self):
        return '<Bank %r>' % self.bankName

# CREATE TABLE Branch (
#   bankBranchName varchar(50),
#   bankBranchAddress varchar(255),
#   bankName varchar(50),
#   PRIMARY KEY (bankBranchName),
#   FOREIGN KEY (bankName) REFERENCES bank (bankName)
# );
class Branch(db.Model):
    bankBranchName = db.Column(db.String(50), primary_key=True)
    bankBranchAddress = db.Column(db.String(255))
    bankName = db.Column(db.String(50), db.ForeignKey('bank.bankName'))
    bankAccounts = db.relationship("BankAccount", backref="branch")

    def __repr__(self):
        return '<Branch %r>' % self.bankBranchName

# CREATE TABLE BankAccount (
#   bankAcctNo decimal(20,0),
#   bankName varchar(50),
#   bankBranchName varchar(50),
#   PRIMARY KEY (bankNo, bankName),
#   FOREIGN KEY (bankName) REFERENCES bank (bankName),
#   FOREIGN KEY (bankBranchName) REFERENCES branch (bankBranchName)
# );
class BankAccount(db.Model):
    __tablename__ = 'bankaccount'
    bankAcctNo = db.Column(db.Numeric(20), primary_key=True)
    bankName = db.Column(db.String(50), db.ForeignKey('bank.bankName'), primary_key=True)
    bankBranchName = db.Column(db.String(50), db.ForeignKey('branch.bankBranchName'))
    # account = db.relationship("Account", backref=db.backref("bankaccount", uselist=False))

    def __repr__(self):
        return '<BankAccount %r %r>' % self.bankAcctNo % self.bankName







# REST OF THE TABLES FOLLOW (NOT IMPLEMENTED):

# class Business(db.Model):
#     __tablename__ = 'abusiness'
#     businessName = db.Column(db.String(255), primary_key=True)
#     businessNature = db.Column(db.String(255))
#     businessAddress = db.Column(db.String(255))
#     accounts = db.relationship("Account", backref="abusiness")

#     def __repr__(self):
#         return '<Business %r>' % self.businessName


# class Tin(db.Model):
#     tinNo = db.Column(db.Numeric(9), primary_key=True)
#     fName = db.Column(db.String(50))
#     mName = db.Column(db.String(50))
#     lName = db.Column(db.String(50))
#     birthDate = db.Column(db.Date)
#     gender = db.Column(db.String(10))
#     account = db.relationship("Account", backref=db.backref("tin", uselist=False))

#     def __repr__(self):
#         return '<Tin %r %r>' % self.tinNo

# class CountryofResidence(db.Model):
#     __tablename__ = 'countryofresidence'
#     countryResidence = db.Column(db.String(50), primary_key=True)
#     contactCountryCode = db.Column(db.Numeric(5))
#     countryinAddress = db.relationship("CountryinAddress", backref=db.backref("countryofresidence", uselist=False))

#     def __repr__(self):
#         return '<CountryofResidence %r>' % self.countryResidence

# class CountryinAddress(db.Model):
#     __tablename__ = 'countryinaddress'
#     addressCountry = db.Column(db.String(50), primary_key=True)
#     countryResidence = db.Column(db.String(50), db.ForeignKey('countryofresidence.countryResidence'))
#     postalCodes = db.relationship("PostalCode", backref="countryinaddress")
#     account = db.relationship("Account", backref="countryinaddress")

#     def __repr__(self):
#         return '<CountryinAddresss %r>' % self.addressCountry

# class PostalCode(db.Model):
#     __tablename__ = 'postalcode'
#     addressPostalCode = db.Column(db.Numeric(10), primary_key=True)
#     addressCity = db.Column(db.String(50), primary_key=True)
#     addressCountry = db.Column(db.String(50), db.ForeignKey('countryinaddress.addressCountry')) #new pkey
#     # account = db.relationship("Account", backref="postalcode")

#     def __repr__(self):
#         return '<PostalCode %r %r>' % self.addressPostalCode % self.addressCountry

# class Account(db.Model):
#     acctNo = db.Column(db.Numeric(8), primary_key=True)
#     civilStatus = db.Column(db.String(10))
#     tinNo = db.Column(db.Numeric(9), db.ForeignKey('tin.tinNo'))
#     emailAddress = db.Column(db.String(255))
#     addressNumber = db.Column(db.Integer)
#     addressStreet = db.Column(db.String(50))
#     # addressPostalCode = db.Column(db.Integer) #fkey
#     # addressCountryX = db.Column(db.Integer) #fkey
#     addressCountry = db.Column(db.String(50), db.ForeignKey('countryinaddress.addressCountry'))
#     contactNo = db.Column(db.Numeric(12))
#     # businessName = db.Column(db.String(255), db.ForeignKey('business.businessName'))
#     employmentStatus = db.Column(db.String(10))
#     occupation = db.Column(db.String(20))
#     # bankAcctNo = db.Column(db.Integer) #fkey
#     # bankNamex = db.Column(db.Integer) #fkey
#     bankName = db.Column(db.String(255), db.ForeignKey('bank.bankName'))
#     form = db.relationship("Form", backref=db.backref("account", uselist=False))
#     # db.ForeignKeyConstraint(['addressPostalCode', 'addressCountryX'], ['postalcode.addressPostalCode', 'postalcode.addressCountry'])
#     # db.ForeignKeyConstraint(['bankAcctNo', 'bankNamex'], ['bankaccount.bankAcctNo', 'bankaccount.bankName'])
#     def __repr__(self):
#         return '<Account %r>' % self.acctNo

# class Form(db.Model):
#     formNo = db.Column(db.Numeric(15), primary_key=True)
#     acctNo = db.Column(db.Integer, db.ForeignKey('account.acctNo'))
    
#     def __repr__(self):
#         return '<Form %r>' % self.formNo