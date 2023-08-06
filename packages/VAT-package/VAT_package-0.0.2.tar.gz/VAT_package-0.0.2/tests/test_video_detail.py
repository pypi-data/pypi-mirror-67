import random
import pytest
import json
from .test_video_upload import upload_random_videos
from .test_user_detail import findCommonKeys

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_success(client, auth_headers, video_num):
    body = upload_random_videos(client, auth_headers, video_num)
    # get video detail
    res = client.get('/video/detail/1', headers=auth_headers)
    assert res.status_code == 200
    assert 'errorMsg' not in res.json
    assert res.json['title'] == body['title']


@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_upload_video_without_authorization(client, video_num):
    res = client.get('/video/detail/' + str(video_num))
    assert res.status_code == 401


@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_non_existing_video(client, auth_headers, video_num):
    res = client.get('/video/detail/'+ str(video_num), headers=auth_headers)
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'Video does not exist'

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_private_video(client, auth_headers, auth_headers2, video_num):
    # upload as auth1
    body = upload_random_videos(client, auth_headers, video_num, 0)
    # auth1 should can get video
    res = client.get('/video/detail/1', headers=auth_headers)
    assert res.status_code == 200
    assert res.json['title'] == body['title']
    assert res.json['is_public'] == 0
    # auth2 cannot get video
    res = client.get('/video/detail/1', headers=auth_headers2)
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'Video does not exist'

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_get_video_detail_with_comments(client, auth_headers, video_num):
    # upload a video
    upload_random_videos(client, auth_headers, video_num)
    # post a comment for the video
    body = post_comment_for_specific_video(client, auth_headers, 1)
    # get the video detail
    res = client.get('/video/detail/1', headers=auth_headers)

    assert res.status_code == 200
    for key in findCommonKeys(res.json['comments'][0], body):
        assert res.json['comments'][0][key] == body[key]

def post_comment_for_specific_video(client, auth_headers, video_id):
    body = {
        'video_id': video_id,
        'comment': f'This is a comment for posting a comment for a specific video',
        'content': random.randint(0, 5),
        'lang': random.randint(0, 5),
        'visual': random.randint(0, 5),
        'clarity': random.randint(0, 5),
        'brevity': random.randint(0, 5),
    }
    res = client.post('/comment', json=body, headers=auth_headers)
    assert res.status_code == 200
    return body



