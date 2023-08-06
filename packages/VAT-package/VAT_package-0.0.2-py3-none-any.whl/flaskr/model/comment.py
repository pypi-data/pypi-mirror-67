from flaskr import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    content = db.Column(db.Integer)
    lang = db.Column(db.Integer)
    visual = db.Column(db.Integer)
    clarity = db.Column(db.Integer)
    brevity = db.Column(db.Integer)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    video = db.relationship('Video', back_populates='comments')
    user = db.relationship('User')


    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'content': self.content,
            'lang': self.lang,
            'visual': self.visual,
            'clarity': self.clarity,
            'brevity': self.brevity,
            'video_id': self.video_id,
            'user_id': self.user_id,
            'user_email': self.user.email,
        }

