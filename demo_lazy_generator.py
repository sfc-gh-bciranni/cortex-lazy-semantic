from cortex_lazy_semantic.generator import generate_semantic_model_from_dataframe, generate_semantic_model_from_table
from snowflake.snowpark import Session
import pandas as pd
import yaml

session = Session.builder.config("connection_name", "<your_connection_name>").create()

# Sample data from a CSV file
data = pd.read_csv('sample_data/daily_revenue.csv')

semantic_model = generate_semantic_model_from_dataframe(
    session=session,
    data=data,
    database='DEMO',
    schema='DEMO_SCHEMA',
    table='DAILY_REVENUE'
)

with open('example_semantic_model_from_dataframe.yaml', 'w') as f:
    yaml.dump(semantic_model, f, indent=4)

print(yaml.dump(semantic_model, indent=4))

# Generate a semantic model from a table
semantic_model = generate_semantic_model_from_table(
    session=session,
    database='DEMO',
    schema='DEMO_SCHEMA',
    table='DAILY_REVENUE'
)

with open('example_semantic_model_from_table.yaml', 'w') as f:
    yaml.dump(semantic_model, f, indent=4)

print(yaml.dump(semantic_model, indent=4))

