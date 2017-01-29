from app import db
from app.mod_auth import Base


class NoteCategory(Base):
    __tablename__ = 'note_category'

    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))
    notes = db.relationship('Note', backref=db.backref('note_content', lazy='dynamic', uselist=True))

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            user_id=self.user_id
        )

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<NoteCategory %r>' % (self.name)
