import pytest
import random

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_success(client, auth_headers, video_num):
    upload_random_videos(client, auth_headers, video_num)

@pytest.mark.parametrize("video_num", map(lambda x: random.randint(1, 1000), range(0, 5)))
def test_duplicate(client, auth_headers, video_num):
    body = upload_random_videos(client, auth_headers, video_num)
    # upload again
    res = client.post('/video/upload', json=body, headers=auth_headers)
    assert res.status_code == 200
    assert res.json['errorMsg'] == 'video already exists'

def test_authorization(client):
    body = {
        'title': 'Awesome video',
        'description': 'blah blah blah',
        'aws_access': '<aws_access>',
        'aws_key': '<aws_key>',
        'is_public': 1,
    }
    # upload without authorization header
    res = client.post('/video/upload', json=body)
    assert res.status_code == 401


def test_upload_without_aws_key(client, auth_headers):
    body = {
        'title': 'Awesome video',
        'description': 'blah blah blah',
        'aws_access': '<aws_access>',
        'aws_key': '',
        'is_public': 1,
    }
    res = client.post('/video/upload', json=body, headers=auth_headers)
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'AWS key is empty'

def test_upload_without_aws_access(client, auth_headers):
    body = {
        'title': 'Awesome video',
        'description': 'blah blah blah',
        'aws_access': '',
        'aws_key': '<aws_key>',
        'is_public': 1,
    }
    res = client.post('/video/upload', json=body, headers=auth_headers)
    assert res.status_code == 200
    assert "errorMsg" in res.json
    assert res.json['errorMsg'] == 'AWS access is empty'




def upload_random_videos(client, auth_headers, video_num, is_public=1):
    body = {
        'title': f'Awesome video {video_num}',
        'description': f'This is random video: {video_num}',
        'aws_access': f'<aws_access_{video_num}>',
        'aws_key': f'<aws_key_{video_num}>',
        'is_public': is_public,
    }
    res = client.post('/video/upload', json=body, headers=auth_headers)
    assert res.status_code == 200
    return body
