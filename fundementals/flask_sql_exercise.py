from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mtech@localhost/sales'

db = SQLAlchemy(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "Customers('{}', '{}', '{}')".format(self.name, self.email, self.address)


db.create_all()
cust_1 = Customers(name='abc', address='Ahm', email='abc@gmail.com')
cust_2 = Customers(name='mno', address='Hyd', email='mno@gmail.com')
cust_3 = Customers(name='pqr', address='Delhi', email='pqr@gmail.com')

db.session.add(cust_1)
db.session.add(cust_2)
db.session.add(cust_3)
db.session.commit()

