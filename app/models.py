from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    xp = db.Column(db.Integer)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self, id, username, email, password_hash, xp):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.xp = xp

    def __repr__(self):
        return '<user %r, username %r>' % (self.id, self.username)
