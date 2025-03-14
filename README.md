# Cortex Lazy Semantic

Quickly go from sample of your table, to semantic model.

Cortex Lazy Semantic generates a semantic model for any table in Snowflake, or a pandas dataframe you'll put there. Behind the scenes, it uses claude and snowflake's structured outputs, along with a sample of the data in question, to build a dictionary with all the required fields for an Analyst semantic model.

For output examples, see:
- `example_semantic_model_from_dataframe.yaml`
- `example_semantic_model_from_table.yaml`

## Usage

Say you have either a table in Snowflake, or a pandas DataFrame and you want to generate a semantic model for it.
You may have a table you want to point Analyst at, but want a simple starting point for the model - or you may just have a CSV file that you want to upload and want to ask questions about.

Maybe the data looks like this:

| date | revenue | cogs | forecasted_revenue | product_id | region_id |
|------|---------|---------|---------|---------|---------|
| 2022-11-09 15:07:24.446047 | 1175.18 | 2045.42 | 2438.94 | 3 | 1 |
| 2022-11-10 15:07:24.446047 | 4297.86 | 1199.4 | 2894.6 | 5 | 2 |
| 2022-11-11 15:07:24.446047 | 4755.99 | 1202.93 | 1353.3 | 3 | 2 |
| 2022-11-12 15:07:24.446047 | 1176.32 | 1674.98 | 1058.28 | 5 | 1 |

and so on.

You can generate a semantic model for this data from a table in Snowflake (`DEMO.DEMO_SCHEMA.DAILY_REVENUE`):

```python
from cortex_lazy_semantic.generator import generate_semantic_model_from_table

semantic_model = generate_semantic_model_from_table(
    session=session,
    database='DEMO',
    schema='DEMO_SCHEMA',
    table='DAILY_REVENUE'
)
```

or if you have a pandas DataFrame, you can also generate a semantic model for it. Note here that the table
name is not used in the generation process - it's where you would put the table if you were to save it to Snowflake for use in Analyst.

```python
from cortex_lazy_semantic.generator import generate_semantic_model_from_dataframe

semantic_model = generate_semantic_model_from_dataframe(
    session=session,
    data=data,
    database='DEMO',
    schema='DEMO_SCHEMA',
    table='DAILY_REVENUE'
)
```

This takes advantage of the structured outputs from LLMs to generate a semantic model that looks like this:

```yaml
description: A semantic model for analyzing daily revenue, costs, and forecasts across
    products and regions
name: Daily Revenue Model
tables:
-   base_table:
        database: DEMO_DB
        schema: DEMO_SCHEMA
        table: DAILY_REVENUE
    description: Daily revenue, costs, and forecasts by product and region
    dimensions:
    ... and so on ...
```



