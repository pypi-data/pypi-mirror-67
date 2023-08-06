import logging
import bcrypt
import datetime
import re
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flaskr import db
from flaskr.model import User

logger = logging.getLogger(__name__)
bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    email = request.json['email'].lower()
    password = request.json['password'].encode('utf-8')

    if isFieldEmpty(email, password):
        return emailPassEmpty(email, password)

    if not valid_email(email):
        return {'errorMsg': 'Invalid email'}
    if user_exists(email):
        return {'errorMsg': 'User already exists'}

    new_user = User(email, password)
    db.session.add(new_user)
    db.session.commit()

    return {'msg': 'success'}

@bp.route('/login', methods=['POST'])
def login():
    email = request.json['email'].lower()
    password = request.json['password'].encode('utf-8')

    if isFieldEmpty(email, password):
        return emailPassEmpty(email, password)

    user = db.session.query(User).filter_by(email=email).one_or_none()
    # user not registered
    if user is None:
        return {'errorMsg': 'User not registered'}
    # password incorrect
    if not bcrypt.checkpw(password, user.passwordhash):
        return {'errorMsg': 'Wrong password'}

    expires = datetime.timedelta(days=30)
    access_token = create_access_token(identity=user.id, expires_delta=expires)
    return {'access_token': access_token}

@bp.route('/detail', methods=['GET'])
@jwt_required
def detail():
    user_id = get_jwt_identity()
    user = db.session.query(User).filter_by(id=user_id).one()

    comments = []
    for video in user.videos:
        comments.extend(video.comments)

    def compute_average(mapper, comments):
        arr = list(filter(lambda x: x is not None, map(mapper, comments)))
        if len(arr) == 0:
            return 0.0
        return sum(arr) / len(arr)

    content = compute_average(lambda c: c.content, comments)
    lang = compute_average(lambda c: c.lang, comments)
    visual = compute_average(lambda c: c.visual, comments)
    clarity = compute_average(lambda c: c.clarity, comments)
    brevity = compute_average(lambda c: c.brevity, comments)

    ret = user.to_dict()
    ret['content'] = content
    ret['lang'] = lang
    ret['visual'] = visual
    ret['clarity'] = clarity
    ret['brevity'] = brevity
    return ret

def user_exists(email):
    return db.session.query(User).filter_by(email=email).count() > 0

def valid_email(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)

@bp.route('/changePass', methods=['POST'])
@jwt_required
def changePass():
    user_id = get_jwt_identity()
    old_password = request.json['oldPass'].encode('utf-8')
    new_password = request.json['newPass'].encode('utf-8')

    #check if old password is valid
    user = db.session.query(User).filter_by(id=user_id).one()

    if not bcrypt.checkpw(old_password, user.passwordhash):
        return {'errorMsg': 'Wrong password'}

    user.passwordhash = bcrypt.hashpw(new_password, bcrypt.gensalt())
    db.session.commit()

    return {'msg': 'success'}


def isFieldEmpty(*fields):
    for field in fields:
        if not field:
            return True
    return False

def emailPassEmpty(email, password):
    if not email:
        return {'errorMsg': 'Email field is empty'}

    if not password:
        return {'errorMsg': 'Password field is empty'}

    return None


