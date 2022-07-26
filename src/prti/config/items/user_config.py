from dataclasses import dataclass


@dataclass
class UserConfig:
    """
    Class to keep user config
    """
    github_login: str
    name: str
    email: str
