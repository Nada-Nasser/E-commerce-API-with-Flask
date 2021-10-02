from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    hashed_password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), default=1000)
    items = db.relationship('Item', backref="owned_user", lazy=True)

    def __repr__(self):
        return f"Userid:{self.id}, name:{self.name}\n"

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]} $"
        else:
            return f"{self.budget} $"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password_plain_text):
        self.hashed_password = bcrypt.generate_password_hash(password_plain_text).decode('utf-8')

    def check_password_correction(self,attempt_password):
        return bcrypt.check_password_hash(self.hashed_password, attempt_password)

    def can_purchase(self, item_price):
        return self.budget >= item_price

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Item id:{self.id}, name:{self.name}"
