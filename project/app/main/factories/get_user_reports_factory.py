from app.domain.usecases import Usecase
from app.services.usecases.github_reports import GetGithubUserReports


def get_user_reports_factory() -> Usecase:

    return GetGithubUserReports()
