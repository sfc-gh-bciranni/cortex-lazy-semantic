from cortex_lazy_semantic.generator import generate_semantic_model
from snowflake.snowpark import Session
import pandas as pd
import yaml

session = Session.builder.config("connection_name", "<your_connection_name>").create()

data = pd.read_csv('sample_data/daily_revenue.csv')

semantic_model = generate_semantic_model(
    session=session,
    data=data,
    database='DEMO_DB',
    schema='DEMO_SCHEMA',
    table='DAILY_REVENUE'
)

with open('semantic_model.yaml', 'w') as f:
    yaml.dump(semantic_model, f, indent=4)

print(yaml.dump(semantic_model, indent=4))

