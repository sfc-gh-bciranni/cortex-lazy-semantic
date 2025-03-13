from .common.cortex_utils import structured_output_llm_call
from .common.schema_utils import get_semantic_model_spec_schema
from snowflake.snowpark import Session
from typing import Dict, Any
import pandas as pd


def generate_semantic_model_from_dataframe(
        session: Session,
        data: pd.DataFrame,
        database: str,
        schema: str,
        table: str,
        model: str = 'claude-3-5-sonnet',
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
    """
    Generate a semantic model from a pandas DataFrame.

    Args:
        session: The Snowflake session.
        data: The pandas DataFrame to generate the semantic model from.
        database: The database name.
        schema: The schema name.
        table: The table name.
        model: The model to use for the semantic model.
        max_tokens: The maximum number of tokens to use for the semantic model.

    Returns:
        The semantic model as a dictionary.
    """
    # Generate the JSON Schema
    semantic_model_spec_schema = get_semantic_model_spec_schema()
    # Generate the prompt
    prompt = '''
    Generate a semantic model from the following data
    (Showing represenatative sample (first 50 rows) of the data):
    {data}

    The Database, Schema, and Table names for the base table are:
    {database}, {schema}, {table}
    '''.format(data=data[:50], database=database, schema=schema, table=table)
    # Generate the semantic model
    semantic_model = structured_output_llm_call(
        session,
        prompt,
        semantic_model_spec_schema,
        model,
        max_tokens
    )
    return semantic_model

def generate_semantic_model_from_table(
        session: Session,
        database: str,
        schema: str,
        table: str,
        model: str = 'claude-3-5-sonnet',
        max_tokens: int = 4000
) -> Dict[str, Any]:
    """
    Generate a semantic model from a table in Snowflake.

    Args:
        session: The Snowflake session.
        database: The database name.
        schema: The schema name.
        table: The table name.
        model: The model to use for the semantic model.
        max_tokens: The maximum number of tokens to use for the semantic model.

    Returns:
        The semantic model as a dictionary.
    """
    table_sample = session.table(f"{database}.{schema}.{table}").sample(n=50).to_pandas()
    return generate_semantic_model_from_dataframe(
        session,
        table_sample,
        database,
        schema,
        table,
        model,
        max_tokens
    )