import logging
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flaskr import db
from flaskr.model import Comment
from flaskr.model import Video

logger = logging.getLogger(__name__)
bp = Blueprint('comment', __name__)

@bp.route('/comment', methods=['POST'])
@jwt_required
def video_comment():
    '''Post a comment on video'''
    user_id = get_jwt_identity()

    comment = Comment()
    comment.comment = request.json.get('comment')
    comment.content = request.json.get('content')
    comment.lang = request.json.get('lang')
    comment.visual = request.json.get('visual')
    comment.clarity = request.json.get('clarity')
    comment.brevity = request.json.get('brevity')
    comment.video_id = request.json['video_id']
    comment.user_id = user_id
    video_count = db.session.query(Video).filter_by(id=comment.video_id).count()
    if video_count == 0:
        return {'errorMsg': 'video does not exist!'}
    db.session.add(comment)
    db.session.commit()

    return {'msg': 'success'}
