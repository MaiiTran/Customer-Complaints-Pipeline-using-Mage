from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_sheets import GoogleSheets
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_sheet(*args, **kwargs):
    """
    Template for loading data from a worksheet in a Google Sheet.
    Specify your configuration settings in 'io_config.yaml'.

    Sheet Name or ID may also be used instead of URL
    sheet_id = "1Mv1eDv0QVwKUYZT05FZ9XZfezgZQXAWJuNMVokkgiDM"
    sheet_name = "customer_complaint_data"

    Worksheet position or name may also be specified
    worksheet_position = 0
    worksheet_name = "Sheet1"

    Docs: [TODO]
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    header_rows = 1
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Mv1eDv0QVwKUYZT05FZ9XZfezgZQXAWJuNMVokkgiDM/edit?gid=0#gid=0'

    return GoogleSheets.with_config(ConfigFileLoader(config_path, config_profile)).load(
        sheet_url=sheet_url,
        header_rows=header_rows
    )


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
