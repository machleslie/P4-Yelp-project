from __init__ import db

class User (db.Model):
    __tablename__ = 'users'
    
    id=db.Column(db.integer,primary_key=True)
    name =db.Column(db.String(50),nullable=False)
    email =db.Column(db.String(50),nullable=False)
    review_count=db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    average_stars=db.Column(db.String)
    profile_photo=db.Column(db.String)
    reviews = db.relationship('reviews',backref="users")
    
    
class Review (db.Model):
    __tablename__ ='reviews'
    
    id=db.Column(db.Integrer,primary_key=True)
    stars =db.Column(db.Integer,nullable=False)
    text=db.Column(db.String,nullable=False)
    date =db.Column(db.Srting)
    
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    business_id =db.column(db.Integer, db.ForeignKey('businesses.id'))
    
class Business(db.Model):
    __tablename__ ="businesses"
    
    id=db.column(db.Integer,primary_key=True)
    name=db.column(db.String,nullable=False)
    address=db.Column(db.string)
    city=db.column(db.String)
    reviews_count=db.Column(db.Integer)
    open_from=db.Column(db.Time)
    closed_in=db.Column(db.Time)
    
    category_id=db.Column(db.integer,db.ForeignKey("categories.id"))
    
    reviews=db.relationship('reviews',backref="businesses")
    
class Category(db.Model):
    __tablename__='categories'
    
    id=db.Column(db.Integer,primary_key=True)
    category_name=db.Column(db.String,nullable=False)
    png=db.Column(db.String)
    
    businesses=db.relationship('businesses',backref="categories")
    