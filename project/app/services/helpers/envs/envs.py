from os import getenv


def get_github_api_base_url() -> str:
    return getenv('GITHUB_API_BASE_URL', '')
