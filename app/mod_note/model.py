from app import db
from app.mod_auth import Base


class Note(Base):
    __tablename__ = 'note_content'

    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String(1024 * 8), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('note_category.id'))
    category = db.relationship('NoteCategory', backref=db.backref('note_category', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))
    user = db.relationship('User', backref=db.backref('auth_users', lazy='dynamic'))

    def is_owned_by(self, user_id):
        return user_id == self.user_id

    def __init__(self, title, content, category_id, user_id):
        self.title = title
        self.content = content
        self.category_id = category_id
        self.user_id = user_id

    def serialize(self):
        return dict(
            id=self.id,
            title=self.title,
            content=self.content,
            category_id=self.category_id,
            user_id=self.user_id
        )

    def __repr__(self):
        return '<Note %r>' % (self.title)
