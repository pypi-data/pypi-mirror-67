from google.cloud.bigquery import Client as GoogleBigQueryClient
from google.cloud import bigquery


class Client(GoogleBigQueryClient):
    def __init__(self, project=None, credentials=None, _http=None):
        super().__init__(project=project, credentials=credentials, _http=_http)

    def create_bq_dataset(self, dataset_name: str, location: str = 'US'):
        dataset_ref = self.dataset(dataset_name)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = location
        dataset = self.create_dataset(dataset)
