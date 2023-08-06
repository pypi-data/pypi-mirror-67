import pytest
import random
from .test_video_upload import upload_random_videos
from .test_video_list import upload_many_random_videos

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_success(client, auth_headers, video_num):
    video = upload_random_videos(client, auth_headers, video_num)
    body = fetch_my_list(client, auth_headers)
    assert len(body['video_list']) == 1
    assert body['video_list'][0]['title'] == video['title']

def test_empty(client, auth_headers):
    body = fetch_my_list(client, auth_headers)
    assert 'errorMsg' not in body
    assert 'video_list' in body
    assert len(body['video_list']) == 0


def test_authorization(client):
    res = client.post('/video/my_list')
    assert res.status_code == 401

@pytest.mark.parametrize("count", map(lambda x: random.randint(10, 21), range(0, 5)))
def test_success_many_videos(client, auth_headers, count):

    # upload videos as auth1
    upload_many_random_videos(client, auth_headers, count)
    body = fetch_my_list(client, auth_headers)
    assert len(body['video_list']) == count

@pytest.mark.parametrize("count", map(lambda x: random.randint(10, 21), range(0, 5)))
def test_only_uploader_video_in_list(client, auth_headers, auth_headers2, count):
    upload_many_random_videos(client, auth_headers, count)
    body = fetch_my_list(client, auth_headers)
    assert len(body['video_list']) == count

    # auth2 should not see any videos
    body = fetch_my_list(client, auth_headers2)
    assert len(body['video_list']) == 0

def fetch_my_list(client, auth_headers):
    res = client.post('/video/my_list', headers=auth_headers)
    assert res.status_code == 200
    return res.json
