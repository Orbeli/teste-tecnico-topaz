from http import HTTPStatus
from fastapi import Response

from app.main.main import app
from app.main.adapters import fast_api_adapter
from app.main.factories import (
    get_user_reports_factory,
)
from app.domain.usecases import (
    GetGithubUserReportsParams,
    GetGithubUserReportsResponse,
)

from app.main.routes.helpers import InternalServerError

@app.get("/teste/{id}")
def read_main():
    return {"msg": "Hello World"}

@app.get(
    '/github/get/{username}',
    responses={
        HTTPStatus.OK.value: {'model': GetGithubUserReportsResponse},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {
            'model': InternalServerError, 'description': 'Internal Server Error'
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Username not found'
        },
    },
    status_code=HTTPStatus.NO_CONTENT,
    tags=['Reports']
)
def get_github_user_reports(username: str, response: Response):
    request = {'body': GetGithubUserReportsParams(username=username), 'headers': None, 'query': None}
    result = fast_api_adapter(request, get_user_reports_factory())
    response.status_code = result.status_code
    return result.body
