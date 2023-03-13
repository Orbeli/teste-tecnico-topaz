import requests
import json

from typing import Dict
from app.domain.usecases import GetGithubUserReports as GetGithubUserReportsContract
from app.domain.usecases import GetGithubUserReportsParams, GetGithubUserReportsResponse
from app.services.helpers.http import HttpResponse, HttpStatus
from app.services.helpers.github_user_reports_writer import generate_report_file
from app.services.helpers.envs import get_github_api_base_url


class GetGithubUserReports(GetGithubUserReportsContract):
    def __init__(
        self,
    ) -> None:
        pass

    def get_repositories(self, repositories_url: str) -> Dict:
        repositories_data = requests.get(repositories_url)

        # return a dict of user repositories
        return {data['name']: data['html_url'] for data in repositories_data.json()}

    def execute(self, params: GetGithubUserReportsParams) -> HttpResponse:
        url = f'{get_github_api_base_url()}/users/{params.username}'
        request = requests.get(url)
        user_basic_data = request.json()

        if request.status_code == 404:
            return HttpStatus.not_found_404(
                f"User {params.username} does not exist"
            )

        repositories_data = self.get_repositories(user_basic_data['repos_url'])

        github_user_report = GetGithubUserReportsResponse(
                name=user_basic_data['name'],
                profile=user_basic_data['html_url'],
                public_repositories=len(repositories_data),
                followers=user_basic_data['followers'],
                following=user_basic_data['following'],
                repositories=repositories_data
        )

        generate_report_file(
            self,
            file_name=params.username,
            report_data=github_user_report
        )

        return HttpStatus.ok_200(
            github_user_report
        )
