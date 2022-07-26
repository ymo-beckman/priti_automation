from dataclasses import dataclass


@dataclass
class ConfigItem:
    _user_config_table: str
    _project_config_table: str
    _collect_record_table: str

    _github_access_token: str

    def get_user_config_table_name(self):
        return self._user_config_table

    def get_project_config_table_name(self):
        return self._project_config_table

    def get_collect_record_table_name(self):
        return self._collect_record_table

    def get_github_access_token(self):
        return self._github_access_token
