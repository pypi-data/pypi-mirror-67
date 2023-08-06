from .test_video_upload import upload_random_videos
import pytest
from statistics import mean

def test_single_rating(client, auth_headers):
    upload_random_videos(client, auth_headers, 1)

    body = post_rating(client, auth_headers)

    res = client.get('/detail', headers=auth_headers)
    assert res.status_code == 200

    for key in findCommonKeys(res.json, body):
        assert res.json[key] == body[key]

def test_multiple_rating(client, auth_headers):
    upload_random_videos(client, auth_headers, 1)

    body1 = post_rating(client, auth_headers)

    body2 = post_rating(client, auth_headers, video_id=1, content=2, lang=3, visual=4, clarity=5, brevity=1)

    res = client.get('/detail', headers=auth_headers)
    assert res.status_code == 200

    for key in findCommonKeys(res.json, body1):
        assert res.json[key] == mean([body1[key], body2[key]])



def test_auth(client):
    res = client.get('/detail')
    assert res.status_code == 401


def findCommonKeys(dict1, dict2):
    return set(dict1).intersection(set(dict2))


def post_rating(client, auth_headers, video_id=1, content=1, lang=2, visual=3, clarity=4, brevity=5):
    body = {
        'video_id': video_id,
        'comment': 'This is a comment for testing detail',
        'content': content,
        'lang': lang,
        'visual': visual,
        'clarity': clarity,
        'brevity': brevity
    }
    res = client.post('/comment', json=body, headers=auth_headers)
    assert res.status_code == 200
    return body
