import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # I. USER_ADDRESS_DIM 
    user_address_dim = df[['zip_code', 'state']].drop_duplicates()

    # II. PRODUCT_DIM  
    product_dim = df[['product', 'sub_product']].drop_duplicates().reset_index(drop=True)
    product_dim = pd.DataFrame(product_dim)
    product_dim['sub_product_id'] = product_dim.index
    product_dim = product_dim[['sub_product_id', 'sub_product', 'product']]

    # III. ISSUE_DIM  
    issue_dim = df[['issue', 'sub_issue']].drop_duplicates().reset_index(drop=True)
    issue_dim = pd.DataFrame(issue_dim)
    issue_dim['sub_issue_id'] = issue_dim.index
    issue_dim = issue_dim[['sub_issue_id', 'sub_issue', 'issue']]

    # IV. FACT TABLE 
    fact_table = df.merge(product_dim, on = ['sub_product', 'product']) \
                .merge(issue_dim, on = ['sub_issue', 'issue']) \
                [['date_received', 'sub_product_id', 'sub_issue_id', 'consumer_complaint_narrative', 'company_public_response', 'company',
                'zip_code', 'tags', 'consumer_consent_provided?', 'submitted_via', 'date_sent_to_company', 'company_response_to_consumer',
                'timely_response?', 'consumer_disputed?', 'complaint_id']]
    print(fact_table)
    return "success" 


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
