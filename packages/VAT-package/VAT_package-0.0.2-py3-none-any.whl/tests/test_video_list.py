import pytest
import random
from .test_video_upload import upload_random_videos
from .conftest import create_auth_header
from .test_user_detail import findCommonKeys

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_success(client, auth_headers2, video_num):

    email = 'test@illinois.edu'
    password = '123456'
    auth_headers = create_auth_header(client, email=email, password=password)

    # upload a video
    video = upload_random_videos(client, auth_headers, video_num)

    # fetch video list by different user
    body = fetch_video(client, auth_headers2, 0, 50)

    video_list = body['video_list']
    assert len(video_list) == 1
    for key in findCommonKeys(video_list[0], video):
        assert video_list[0][key] == video[key]


def test_empty(client, auth_headers):
    # fetch video list
    body = fetch_video(client, auth_headers, 0, 50)
    video_list = body['video_list']
    assert len(video_list) == 0

def test_authorization(client):
    body = {
        'pageNo': 0,
        'pageSize': 50,
    }
    # without authorization header
    res = client.post('/video/list', json=body)
    assert res.status_code == 401

@pytest.mark.parametrize("count", map(lambda x: random.randint(10, 20), range(0, 5)))
def test_pagination(client, auth_headers, count):
    upload_many_random_videos(client, auth_headers, count)
    body = fetch_video(client, auth_headers, 0, 10)
    assert len(body['video_list']) == 10
    body = fetch_video(client, auth_headers, 1, 10)
    assert len(body['video_list']) == count - 10

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_no_private_video_in_list(client, auth_headers, auth_headers2, video_num):
    upload_random_videos(client, auth_headers, video_num, 0)
    body = fetch_video(client, auth_headers2, 0, 10)
    video_list = body['video_list']
    assert len(video_list) == 0



def fetch_video(client, auth_headers, pageNo, pageSize):
    body = {
        'pageNo': pageNo,
        'pageSize': pageSize,
    }
    res = client.post('/video/list', json=body, headers=auth_headers)
    assert res.status_code == 200
    return res.json


def upload_many_random_videos(client, auth_headers, count):
    for num in range(count):
        upload_random_videos(client, auth_headers, num)
