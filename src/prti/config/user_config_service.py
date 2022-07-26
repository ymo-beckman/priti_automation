import boto3

from boto3.dynamodb.table import BatchWriter

from dataclasses import asdict

from config.config_service import ConfigService
from prti.config.items.user_config import UserConfig


class UserConfigService:
    def __init__(self):
        self.user_list = []
        self.user_dict = {}

        dynamodb = boto3.resource('dynamodb')
        self.table: BatchWriter = dynamodb.Table(ConfigService.get_user_config_table_name())

    def fetch_users(self):
        if len(self.user_list) == 0:
            response = self.table.scan()
            self.user_list = response['Items']

            self.user_dict = {}

            for user in self.user_list:
                github_login = user['github_login']

                user_config = UserConfig(**user)
                self.user_dict[github_login] = user_config

        return self.user_list

    def add_new_user(self, user: UserConfig):
        self.table.put_item(
            Item=asdict(user)
        )

        self.user_dict[user.github_login] = user
