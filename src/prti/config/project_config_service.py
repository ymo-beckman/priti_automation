import boto3

from boto3.dynamodb.table import BatchWriter

from dataclasses import asdict

from config.config_service import ConfigService
from prti.config.items.project_config import ProjectConfig


class ProjectConfigService:
    def __init__(self):
        self.project_list = []
        self.project_dict = {}

        dynamodb = boto3.resource('dynamodb')
        self.table: BatchWriter = dynamodb.Table(ConfigService.get_project_config_table_name())

    def fetch_projects(self):
        if len(self.project_list) == 0:
            response = self.table.scan()
            self.project_list = response['Items']

            self.project_dict = {}

            for project in self.project_list:
                project_key = project['project_key']

                project_config = ProjectConfig(**project)

                self.project_dict[project_key] = project_config

        return self.project_list

    def add_new_project(self, project: ProjectConfig):
        self.table.put_item(
            Item=asdict(project)
        )

        self.project_dict[project.project_key] = project
