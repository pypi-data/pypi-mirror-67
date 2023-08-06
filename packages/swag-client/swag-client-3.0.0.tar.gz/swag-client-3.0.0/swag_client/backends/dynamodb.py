import logging

import boto3
from botocore.exceptions import ClientError
from dogpile.cache import make_region

from swag_client.backend import SWAGManager

logger = logging.getLogger(__file__)

dynamodb_region = make_region()


class DynamoDBSWAGManager(SWAGManager):
    def __init__(self, namespace, **kwargs):
        """Create a DynamoDb based SWAG backend."""
        self.namespace = namespace
        resource = boto3.resource('dynamodb', region_name=kwargs['region'])
        self.table = resource.Table(namespace)

        if not dynamodb_region.is_configured:
            dynamodb_region.configure(
                'dogpile.cache.memory',
                expiration_time=kwargs['cache_expires']
            )

    def create(self, item, dry_run=None):
        """Creates a new item in file."""
        logger.debug('Creating new item. Item: {item} Table: {namespace}'.format(
            item=item,
            namespace=self.namespace
        ))

        if not dry_run:
            self.table.put_item(Item=item)

        return item

    def delete(self, item, dry_run=None):
        """Deletes item in file."""
        logger.debug('Deleting item. Item: {item} Table: {namespace}'.format(
            item=item,
            namespace=self.namespace
        ))

        if not dry_run:
            self.table.delete_item(Key={'id': item['id']})

        return item

    def update(self, item, dry_run=None):
        """Updates item info in file."""
        logger.debug('Updating item. Item: {item} Table: {namespace}'.format(
            item=item,
            namespace=self.namespace
        ))

        if not dry_run:
            self.table.put_item(Item=item)

        return item

    @dynamodb_region.cache_on_arguments()
    def get_all(self):
        """Gets all items in file."""
        logger.debug('Fetching items. Table: {namespace}'.format(
            namespace=self.namespace
        ))

        rows = []

        result = self.table.scan()

        while True:
            next_token = result.get('LastEvaluatedKey', None)
            rows += result['Items']

            if next_token:
                result = self.table.scan(ExclusiveStartKey=next_token)
            else:
                break

        return rows

    def health_check(self):
        """Gets a single item to determine if Dynamo is functioning."""
        logger.debug('Health Check on Table: {namespace}'.format(
            namespace=self.namespace
        ))

        try:
            self.get_all()
            return True

        except ClientError as e:
            logger.exception(e)
            logger.error('Error encountered with Database. Assume unhealthy')
            return False
