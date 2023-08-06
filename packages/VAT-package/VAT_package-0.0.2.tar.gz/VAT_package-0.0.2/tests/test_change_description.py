import pytest
import random
from .test_video_upload import upload_random_videos

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_success(client, auth_headers, video_num):
    video = upload_random_videos(client, auth_headers, video_num)
    post_description(client, auth_headers, video['aws_access'], video['aws_key'])
    res = client.get('/video/detail/1', headers=auth_headers)
    assert res.json['description'] == "testing"

def test_authorization(client, auth_headers):
    video = upload_random_videos(client, auth_headers, 1)
    body = {
        'aws_access': video['aws_access'],
        'aws_key': video['aws_key'],
        'description': "testing",
    }
    res = client.post('/video/changeDescription', json=body)
    assert res.status_code == 401

def test_non_existing_video(client, auth_headers):
    res = post_description(client, auth_headers, '1', '2')
    assert res.json['errorMsg'] == 'Video does not exist'

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_non_uploader(client, auth_headers, auth_headers2, video_num):
    video = upload_random_videos(client, auth_headers, video_num)
    res = post_description(client, auth_headers2, video['aws_access'], video['aws_key'])
    assert res.json['errorMsg'] == 'Video does not exist'


def test_wrong_aws_key(client, auth_headers):
    video = upload_random_videos(client, auth_headers, 1)
    res = post_description(client, auth_headers, video['aws_access'], 'aws_key')
    assert res.json['errorMsg'] == 'Video does not exist'

def test_wrong_aws_access(client, auth_headers):
    video = upload_random_videos(client, auth_headers, 1)
    res = post_description(client, auth_headers, 'aws_access', video['aws_key'])
    assert res.json['errorMsg'] == 'Video does not exist'



def post_description(client, auth_headers, aws_access, aws_key):
    body = {
        'aws_access': aws_access,
        'aws_key': aws_key,
        'description': "testing",
    }
    res = client.post('/video/changeDescription', json=body, headers=auth_headers)
    assert res.status_code == 200
    return res

