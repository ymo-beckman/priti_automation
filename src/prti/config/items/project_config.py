from dataclasses import dataclass


@dataclass
class ProjectConfig:
    """
    Class to keep project config
    """
    project_key: str
    repo_name: str
    branch: str
    label: str
    display_name: str
    active: bool

    def __int__(self, repo_name, branch, label, display_name, active=True, project_key=None):
        self.project_key = project_key if project_key else f"_{repo_name}_{branch}_{label}_"
        self.repo_name = repo_name
        self.branch = branch
        self.label = label
        self.display_name = display_name
        self.active = active
