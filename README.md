# Cortex Lazy Semantic

A tool to generate a semantic model for a pandas DataFrame. I am often lazy with this and you might be too.
I've done testing to get it valid with the JSON Schema for the SemanticModel - if you have any issues, please
submit an issue and I'll try to fix it.

## Usage

Say you have a pandas DataFrame and you want to generate a semantic model for it.
You may have a CSV file that you upload and want to ask questions about.

Maybe the data looks like this:

| date | revenue | cogs | forecasted_revenue | product_id | region_id |
|------|---------|---------|---------|---------|---------|
| 2022-11-09 15:07:24.446047 | 1175.18 | 2045.42 | 2438.94 | 3 | 1 |
| 2022-11-10 15:07:24.446047 | 4297.86 | 1199.4 | 2894.6 | 5 | 2 |
| 2022-11-11 15:07:24.446047 | 4755.99 | 1202.93 | 1353.3 | 3 | 2 |
| 2022-11-12 15:07:24.446047 | 1176.32 | 1674.98 | 1058.28 | 5 | 1 |

and so on.

You can generate a semantic model for this data by running the following code:

```python
from cortex_lazy_semantic.generator import generate_semantic_model

semantic_model = generate_semantic_model(
    session=session,
    data=data,
    database='DEMO_DB',
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



