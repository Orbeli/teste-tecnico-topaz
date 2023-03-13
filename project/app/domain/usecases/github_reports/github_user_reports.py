from abc import abstractmethod

from pydantic import BaseModel
from typing import Dict

from app.domain.usecases.usecase import Usecase
from app.services.helpers.http import HttpResponse


class GetGithubUserReportsParams(BaseModel):
    username: str


class  GetGithubUserReportsResponse(BaseModel):
    name: str
    profile: str
    public_repositories: int
    followers: int
    following: int
    repositories: Dict[str, str]


class  GetGithubUserReports(Usecase):
    @abstractmethod
    def execute(self, params:  GetGithubUserReportsParams) -> HttpResponse:
        raise NotImplementedError()
