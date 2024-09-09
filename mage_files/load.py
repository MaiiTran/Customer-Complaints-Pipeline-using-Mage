from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to an S3 bucket.
    """
    bucket_name = 'customer-complaint-project'
    object_key = 'customer_complaint_data.csv'

    # No need to specify credentials, AWS will handle it
    S3().export(
        df,
        bucket_name,
        object_key,
    )