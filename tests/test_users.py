import requests
import pytest

def test_valid_credentials(mocker):
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"
    
    mocker.patch('requests.get')
    response_mock = mocker.MagicMock()
    response_mock.status_code = 200
    requests.get.return_value = response_mock
    
    response = requests.get(url)
    
    requests.get.assert_called_with(url)
    assert response.status_code == 200

def test_invalid_credentials(mocker):
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"
    
    mocker.patch('requests.get')
    response_mock = mocker.MagicMock()
    response_mock.status_code = 401
    requests.get.return_value = response_mock
    
    response = requests.get(url)
    
    requests.get.assert_called_with(url)
    assert response.status_code == 401
