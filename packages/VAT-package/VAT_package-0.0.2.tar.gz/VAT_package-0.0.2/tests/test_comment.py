import sqlite3
import random
import pytest
from flaskr import db
from flaskr.model import Comment
from .test_video_upload import upload_random_videos

def test_success(client, auth_headers):
    upload_random_videos(client, auth_headers, 1)
    body = post_a_comment(client, auth_headers, 1)
    comment = db.session.query(Comment).filter_by(video_id=1).one()
    assert comment is not None
    assert comment.video_id == body['video_id']
    assert comment.comment == body['comment']

def test_comment_with_non_existing_video(client, auth_headers):
    body = {
        'video_id': 1,
        'comment': f'This is a comment 1',
    }
    res = client.post('/comment', json=body, headers=auth_headers)
    assert res.status_code == 200
    assert 'errorMsg' in res.json
    assert res.json['errorMsg'] == 'video does not exist!'

def test_authorization(client):
    body = {
        'video_id': 0,
        'comment': 'This is a comment',
    }
    res = client.post('/comment', json=body)
    assert res.status_code == 401

@pytest.mark.parametrize("video_num", [1, 2, 3, 4, 5])
def test_post_multiple_comments_video(client, auth_headers, video_num):
    for num in range(video_num):
        upload_random_videos(client, auth_headers, num)
        body = post_a_comment(client, auth_headers, num+1)
        comment = db.session.query(Comment).filter_by(video_id=num+1).one()
        assert comment.video_id == body['video_id']
        assert comment.comment == body['comment']

@pytest.mark.parametrize("rating_num", [0, 1, 2, 3, 4, 5])
def test_post_comment_with_rating(client, auth_headers, rating_num):
    upload_random_videos(client, auth_headers, 1)
    body = {
        'video_id': 1,
        'comment': 'This is a comment for testing rating',
        'content': rating_num,
        'lang': rating_num,
        'visual': rating_num,
        'clarity': rating_num,
        'brevity': rating_num
    }
    res = client.post('/comment', json=body, headers=auth_headers)
    assert res.status_code == 200

    comment = db.session.query(Comment).filter_by(video_id=1).one()

    assert comment.video_id == body['video_id']
    assert comment.comment == body['comment']
    assert comment.content == body['content']
    assert comment.lang == body['lang']
    assert comment.visual == body['visual']
    assert comment.clarity == body['clarity']
    assert comment.brevity == body['brevity']

def post_a_comment(client, auth_headers, num):
    body = {
        'video_id': num,
        'comment': f'This is a comment {num}',
    }
    res = client.post('/comment', json=body, headers=auth_headers)
    assert res.status_code == 200
    return body
