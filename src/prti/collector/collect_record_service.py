import boto3

from boto3.dynamodb.conditions import Key
from boto3.dynamodb.table import BatchWriter

from dataclasses import asdict

from config.config_service import ConfigService
from prti.collector.items.pr_ti_record import PrTiRecord


class CollectRecordService:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table_name = ConfigService.get_collect_record_table_name()
        self.table: BatchWriter = dynamodb.Table(self.table_name)

    def add_new_project(self, record: PrTiRecord):
        self.table.put_item(
            Item=asdict(record)
        )

    def fetch_prti_records(self, start_time: str, end_time: str):
        response = self.table.scan(
            FilterExpression=Key('review_time').between(start_time, end_time)
        )
        records = response['Items']

        record_list = [PrTiRecord(**record) for record in records]

        return record_list
