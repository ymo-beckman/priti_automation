import os

import yaml

from config.config_item import ConfigItem


class ConfigService:
    config_item: ConfigItem = None

    @classmethod
    def load_config_from_file(cls):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(cur_path, "config.yaml")

        with open(yaml_path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            yaml_dict = yaml.load(cfg, Loader=yaml.FullLoader)

            config_table_dict = yaml_dict['config']['tables']
            config_github_dict = yaml_dict['config']['github']

            cls.config_item = ConfigItem(
                _user_config_table=config_table_dict['user'],
                _project_config_table=config_table_dict['project'],
                _collect_record_table=config_table_dict['collect_record'],

                _github_access_token=config_github_dict['access_token'],
            )

    @classmethod
    def get_user_config_table_name(cls):
        if cls.config_item is None:
            cls.load_config_from_file()

        return cls.config_item.get_user_config_table_name()

    @classmethod
    def get_project_config_table_name(cls):
        if cls.config_item is None:
            cls.load_config_from_file()

        return cls.config_item.get_project_config_table_name()

    @classmethod
    def get_collect_record_table_name(cls):
        if cls.config_item is None:
            cls.load_config_from_file()

        return cls.config_item.get_collect_record_table_name()

    @classmethod
    def get_github_access_token(cls):
        if cls.config_item is None:
            cls.load_config_from_file()

        return cls.config_item.get_github_access_token()
