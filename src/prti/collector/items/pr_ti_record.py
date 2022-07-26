from dataclasses import dataclass


@dataclass
class PrTiRecord:
    record_key: str
    project_key: str
    user_github_login: str
    type: str
    pr_or_ti: str
    defects: int
    time_in_min: int
    LOC: int
    review_time: str
