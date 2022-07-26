import datetime
from typing import Union

from github import Github, Repository, PullRequest, PullRequestComment, PaginatedList

from config.config_service import ConfigService
from prti.config.items.project_config import ProjectConfig


class GithubCollectService:
    def __init__(self):
        self.access_token = ConfigService.get_github_access_token()
        self.github = Github(self.access_token)

    def get_reviews(self, project_config: ProjectConfig, since: datetime):
        repo = self._get_repo_(project_config.repo_name)
        comments = GithubCollectService._get_pull_comments_(repo, since)

    def _get_repo_(self, repo_name: Union[int, str]) -> Repository:
        return self.github.get_repo(repo_name)

    @staticmethod
    def _get_pull_request_(repo: Repository, pull_number: int) -> PullRequest:
        return repo.get_pull(pull_number)

    @staticmethod
    def _get_pull_comments_(repo: Repository, since: datetime) -> PaginatedList[PullRequestComment]:
        return repo.get_pulls_comments(sort='created', direction='asc', since=since)
