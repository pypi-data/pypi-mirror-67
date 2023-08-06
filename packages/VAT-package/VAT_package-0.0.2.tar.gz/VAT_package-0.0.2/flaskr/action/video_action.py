import logging
from datetime import datetime, timezone
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from flaskr import db
from flaskr.model import Video

logger = logging.getLogger(__name__)
bp = Blueprint('video', __name__)

@bp.route('/video/upload', methods=['POST'])
@jwt_required
def upload():
    '''User uploads a video'''
    user_id = get_jwt_identity()

    video = Video()
    video.title = request.json['title']
    video.description = request.json.get('description')
    video.aws_key = request.json['aws_key']
    video.aws_access = request.json['aws_access']
    video.is_public = request.json['is_public']
    video.user_id = user_id
    video.upload_time = datetime.now(timezone.utc)

    if video_exists(video.aws_key):
        return {'errorMsg': 'video already exists'}

    if not video.aws_key:
        return {'errorMsg': 'AWS key is empty'}

    if not video.aws_access:
        return {'errorMsg': 'AWS access is empty'}

    db.session.add(video)
    db.session.commit()
    return {'msg': 'success'}

@bp.route('/video/my_list', methods=['POST'])
@jwt_required
def my_list():
    '''Returns a list of videos the user has uploaded'''
    user_id = get_jwt_identity()

    video_list = db.session.query(Video)\
        .filter_by(user_id=user_id)\
        .order_by(Video.upload_time.desc())\
        .all()
    video_list = list(map(lambda v: v.to_dict(), video_list))
    return {'video_list': video_list}

@bp.route('/video/detail/<int:video_id>', methods=['GET'])
@jwt_required
def detail(video_id):
    '''Returns a video by id'''
    user_id = get_jwt_identity()

    video = db.session.query(Video)\
        .filter_by(id=video_id)\
        .filter(db.or_(Video.is_public == 1, Video.user_id == user_id))\
        .one_or_none()
    if video is None:
        return {'errorMsg': 'Video does not exist'}

    ret = video.to_dict()
    ret['comments'] = list(map(lambda c: c.to_dict(), video.comments))
    return ret

@bp.route('/video/changeTitle', methods=['POST'])
@jwt_required
def change_title():

    user_id = get_jwt_identity()
    aws_access = request.json['aws_access']
    aws_key = request.json['aws_key']
    title = request.json['title']

    video = db.session.query(Video).filter_by(aws_access=aws_access, aws_key=aws_key)\
        .filter(Video.user_id == user_id)\
        .one_or_none()

    if video is None:
        return {'errorMsg': 'Video does not exist'}

    video.title = title
    db.session.commit()
    return {'msg': 'success'}

@bp.route('/video/changeDescription', methods=['POST'])
@jwt_required
def change_description():

    user_id = get_jwt_identity()
    aws_access = request.json['aws_access']
    aws_key = request.json['aws_key']
    description = request.json['description']

    video = db.session.query(Video).filter_by(aws_access=aws_access, aws_key=aws_key)\
        .filter(Video.user_id == user_id)\
        .one_or_none()

    if video is None:
        return {'errorMsg': 'Video does not exist'}

    video.description = description
    db.session.commit()
    return {'msg': 'success'}


@bp.route('/video/list', methods=['POST'])
@jwt_required
def all_list():
    '''Returns a list of videos
       pageNo: page number, start from 0
       pageSize: number of videos per page
    '''

    pageNo = request.json['pageNo']
    pageSize = request.json['pageSize']
    if pageSize > 50:
        pageSize = 50
    offset = pageNo * pageSize

    video_list = db.session.query(Video)\
        .filter_by(is_public=1)\
        .order_by(Video.upload_time.desc())\
        .limit(pageSize)\
        .offset(offset)\
        .all()

    video_list = list(map(lambda v: v.to_dict(), video_list))
    return {'video_list': video_list}

def video_exists(aws_key):
    return db.session.query(Video).filter_by(aws_key=aws_key).count() > 0
