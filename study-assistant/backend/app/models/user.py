#change karna hai
from app import db
from datetime import datetime

class users(db.model):
    __tablename__ = "users"

    id = db.column(db.int , primary_key = True)

    email = db.column(db.string(120) , unique = true , nullable = False)

    password = db.column(db.string(50),nullable = False)

    created_by = db.column(db.DateTime , default = datetime.utcnow)
    
     # One-to-Many with backref
    sessions = db.relationship(
        "Session",
        backref="user",   # 👈 ye automatically Session.user bana dega
        cascade="all, delete-orphan",
        lazy=True
    ) 

    def __repr__(self):
        return f"<User {self.email}>"
