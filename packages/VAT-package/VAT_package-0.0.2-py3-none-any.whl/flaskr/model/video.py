from flaskr import db

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    aws_access = db.Column(db.String, nullable=False)
    aws_key = db.Column(db.String, nullable=False)
    upload_time = db.Column(db.DateTime)
    is_public = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='videos')
    comments = db.relationship('Comment', back_populates='video')


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'aws_access': self.aws_access,
            'aws_key': self.aws_key,
            'is_public': self.is_public,
            'user_id': self.user_id,
            'user_email': self.user.email,
            'upload_time': self.upload_time
        }

