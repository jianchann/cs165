from app import db
from datetime import datetime,date
# from werkzeug.security import generate_password_hash, check_password_hash

# class ABusiness(db.Model):
#     __tablename__ = 'abusiness'
#     businessName = db.Column(db.String(255), primary_key=True)
#     businessNature = db.Column(db.String(255))
#     businessAddress = db.Column(db.String(255))
#     accounts = db.relationship("Account", backref="abusiness")

#     def __repr__(self):
#         return '<Business %r>' % self.businessName

class Bank(db.Model):
    bankName = db.Column(db.String(50), primary_key=True)
    bankMainAddress = db.Column(db.String(255))
    bankBranches = db.relationship("Branch", backref="bank")
    bankAccounts = db.relationship("BankAccount", backref="bank")
    # accounts = db.relationship("Account", backref="bank")

    def __repr__(self):
        return '<Bank %r>' % self.bankName

class Branch(db.Model):
    bankBranchName = db.Column(db.String(50), primary_key=True)
    bankBranchAddress = db.Column(db.String(255))
    bankName = db.Column(db.String(50), db.ForeignKey('bank.bankName'))
    bankAccounts = db.relationship("BankAccount", backref="branch")

    def __repr__(self):
        return '<Branch %r>' % self.bankBranchName

class BankAccount(db.Model):
    __tablename__ = 'bankaccount'
    bankAcctNo = db.Column(db.Numeric(20), primary_key=True)
    bankName = db.Column(db.String(50), db.ForeignKey('bank.bankName'), primary_key=True)
    bankBranchName = db.Column(db.String(50), db.ForeignKey('branch.bankBranchName'))
    # account = db.relationship("Account", backref=db.backref("bankaccount", uselist=False))

    def __repr__(self):
        return '<BankAccount %r %r>' % self.bankAcctNo % self.bankName

class Tin(db.Model):
    tinNo = db.Column(db.Numeric(9), primary_key=True)
    fName = db.Column(db.String(50))
    mName = db.Column(db.String(50))
    lName = db.Column(db.String(50))
    birthDate = db.Column(db.Date)
    gender = db.Column(db.String(10))
    account = db.relationship("Account", backref=db.backref("tin", uselist=False))

    def __repr__(self):
        return '<Tin %r %r>' % self.tinNo

class CountryofResidence(db.Model):
    __tablename__ = 'countryofresidence'
    countryResidence = db.Column(db.String(50), primary_key=True)
    contactCountryCode = db.Column(db.Numeric(5))
    countryinAddress = db.relationship("CountryinAddress", backref=db.backref("countryofresidence", uselist=False))

    def __repr__(self):
        return '<CountryofResidence %r>' % self.countryResidence

class CountryinAddress(db.Model):
    __tablename__ = 'countryinaddress'
    addressCountry = db.Column(db.String(50), primary_key=True)
    countryResidence = db.Column(db.String(50), db.ForeignKey('countryofresidence.countryResidence'))
    postalCodes = db.relationship("PostalCode", backref="countryinaddress")
    account = db.relationship("Account", backref="countryinaddress")

    def __repr__(self):
        return '<CountryinAddresss %r>' % self.addressCountry

class PostalCode(db.Model):
    __tablename__ = 'postalcode'
    addressPostalCode = db.Column(db.Numeric(10), primary_key=True)
    addressCity = db.Column(db.String(50), primary_key=True)
    addressCountry = db.Column(db.String(50), db.ForeignKey('countryinaddress.addressCountry')) #new pkey
    # account = db.relationship("Account", backref="postalcode")

    def __repr__(self):
        return '<PostalCode %r %r>' % self.addressPostalCode % self.addressCountry

class Account(db.Model):
    acctNo = db.Column(db.Numeric(8), primary_key=True)
    civilStatus = db.Column(db.String(10))
    tinNo = db.Column(db.Numeric(9), db.ForeignKey('tin.tinNo'))
    emailAddress = db.Column(db.String(255))
    addressNumber = db.Column(db.Integer)
    addressStreet = db.Column(db.String(50))
    # addressPostalCode = db.Column(db.Integer) #fkey
    # addressCountryX = db.Column(db.Integer) #fkey
    addressCountry = db.Column(db.String(50), db.ForeignKey('countryinaddress.addressCountry'))
    contactNo = db.Column(db.Numeric(12))
    # businessName = db.Column(db.String(255), db.ForeignKey('business.businessName'))
    employmentStatus = db.Column(db.String(10))
    occupation = db.Column(db.String(20))
    # bankAcctNo = db.Column(db.Integer) #fkey
    # bankNamex = db.Column(db.Integer) #fkey
    bankName = db.Column(db.String(255), db.ForeignKey('bank.bankName'))
    form = db.relationship("Form", backref=db.backref("account", uselist=False))
    # db.ForeignKeyConstraint(['addressPostalCode', 'addressCountryX'], ['postalcode.addressPostalCode', 'postalcode.addressCountry'])
    # db.ForeignKeyConstraint(['bankAcctNo', 'bankNamex'], ['bankaccount.bankAcctNo', 'bankaccount.bankName'])
    def __repr__(self):
        return '<Account %r>' % self.acctNo

class Form(db.Model):
    formNo = db.Column(db.Numeric(15), primary_key=True)
    acctNo = db.Column(db.Integer, db.ForeignKey('account.acctNo'))
    
    def __repr__(self):
        return '<Form %r>' % self.formNo
    

# IF EVER WE DO E-COMMERCE

# class QuotationRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship("User", backref="quotation_requests")
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
#     company = db.relationship("Company", backref="quotation_requests")
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     product = db.relationship("Product", backref="quotation_requests")
#     quantity = db.Column(db.Integer, nullable=True)
#     price = db.Column(db.Integer, nullable=True)
#     status = db.Column(db.Integer, default=0)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship("User", backref="orders")
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
#     company = db.relationship("Company", backref="orders")
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     product = db.relationship("Product", backref="orders")
#     quantity = db.Column(db.Integer, nullable=True)
#     price = db.Column(db.Integer, nullable=True)
#     status = db.Column(db.Integer, default=0)
#     Payment = db.relationship("Payment", backref=db.backref("order", uselist=False))
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)

# class Payment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # TODO: Include payment details
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#     order = db.relationship("Product", backref=db.backref("payment", uselist=False))
#     status = db.Column(db.Integer, default=0)


# branch_users = db.Table('branch_users',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('branch_id', db.Integer, db.ForeignKey('branch.id'), primary_key=True)
# )

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     picture_url = db.Column(db.String(255), nullable=True)
#     public_id = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(255), nullable=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     contact_number = db.Column(db.String(120), unique=True, nullable=True)
#     access = db.Column(db.Integer, default=0) # 0 = regular user, 1 = branch admin, 2 = company admin
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

#     def set_password(self, password):
#         self.password = generate_password_hash(password + str(self.public_id))

#     def check_password(self, password):
#         return check_password_hash(self.password, password + str(self.public_id))

#     def __repr__(self):
#         return '<User %r>' % self.name

# class Company(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     logo_url = db.Column(db.String(255), nullable=True)
#     industry_name = db.Column(db.String(100), nullable=True)
#     street_address = db.Column(db.Text, nullable=True)
#     region = db.Column(db.String(100), nullable=True)
#     city = db.Column(db.String(100), nullable=True)
#     contact_number = db.Column(db.String(120), unique=True, nullable=False)
#     branches = db.relationship("Branch", backref="company")
#     users = db.relationship("User", backref="company")
#     established_date = db.Column(db.DateTime, nullable=True)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)

#     def __repr__(self):
#         return '<Business %r>' % self.name

# class Branch(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=True)
#     location = db.Column(db.Text, nullable=True)
#     public_id = db.Column(db.String(50), unique=True)
#     users = db.relationship('User', secondary=branch_users, lazy='subquery',
#                            backref=db.backref('branches', lazy=True))
#     company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#                            onupdate=datetime.utcnow)
#     deleted = db.Column(db.Boolean(), default=False)


# class ProductMaterial(db.Model):
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
#     material_id = db.Column(db.Integer, db.ForeignKey('material.id'), primary_key=True)
#     quantity = db.Column(db.Float, nullable=False)
#     material = db.relationship("Material", back_populates="products")
#     product = db.relationship("Product", back_populates="materials")


# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     price = db.Column(db.Float, nullable=True)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)
#     materials = db.relationship(
#         "ProductMaterial", back_populates="product")

#     def __repr__(self):
#         return '<Product %r>' % self.name

# class Material(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     unit = db.Column(db.String(20), nullable=True)
#     description = db.Column(db.Text, nullable=True)
#     cost = db.Column(db.Float, nullable=True)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#         onupdate=datetime.utcnow)
#     products = db.relationship(
#         "ProductMaterial", back_populates="material")

#     def __repr__(self):
#         return '<Material %r>' % self.name

# class Transaction(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
#     material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=True)
#     product_id = db.Column(
#         db.Integer, db.ForeignKey('product.id'), nullable=True)
#     quantity = db.Column(db.Float, nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     inflow = db.Column(db.Boolean, nullable=False)
#     transaction_date = db.Column(db.DateTime, nullable=False)
#     supplier_name = db.Column(db.String(50), nullable=True)
#     description = db.Column(db.Text, nullable=True)
#     created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     updated_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
#                            onupdate=datetime.utcnow)