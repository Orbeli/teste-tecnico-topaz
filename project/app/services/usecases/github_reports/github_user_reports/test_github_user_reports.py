import pytest
import random

from fastapi.testclient import TestClient

from unittest.mock import patch
from faker import Faker

from app.main.main import app

from app.domain.usecases import GetGithubUserReportsResponse

client = TestClient(app)
fake = Faker()

@pytest.fixture()
def github_user_reports_response():
    return GetGithubUserReportsResponse(
        name=fake.name(),
        profile=fake.pystr(),
        public_repositories=fake.pyint(),
        followers=fake.pyint(),
        following=fake.pyint(),
        repositories=fake.pydict()
    )


@patch.object(GetGithubUserReportsResponse, '__new__')
@patch('app.services.usecases.github_reports.github_user_reports.github_user_reports.generate_report_file', return_value=None)
def test_return_200_ok_when_successful(github_user_reports_response, mock_func):
    user = random.choice(['Orbeli', 'renantescaro', 'UlissesSRosa', 'edddjunior'])
    url = f'/github/get/{user}'
    response = client.get(url)
    mock_func.assert_called_once()
    assert response.status_code == 200


def test_must_return_404_when_user_does_not_exist():
    response = client.get('/github/get/Orbeli!###')
    assert response.status_code == 404
