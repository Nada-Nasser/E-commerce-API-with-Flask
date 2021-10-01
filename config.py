from market import db
from market.models import User, Item

db.drop_all()

db.create_all()

user = User(name="ahmed", email_address="ahmed@gmail.com", hashed_password="123456789")
user2 = User(name="mohamed", email_address="mohamed@gmail.com", hashed_password="555888222")

db.session.add(user)
db.session.add(user2)

print(User.query.all())

item1 = Item(name="IPhone", price=5000, barcode="555666", description="It's a new Iphone")
item2 = Item(name="Laptop", price=12000, barcode="789741", description="It's a new Laptop")

db.session.add(item1)
db.session.add(item2)

print(Item.query.all())

item1.owner = User.query.filter_by(name="mohamed").first().id
item2.owner = User.query.filter_by(name="ahmed").first().id

db.session.add(item1)
db.session.commit()
