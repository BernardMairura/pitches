from . import db




class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")



class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())