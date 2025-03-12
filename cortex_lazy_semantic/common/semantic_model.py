from typing import List, Optional
from pydantic import BaseModel, Field

# Base Table
class BaseTable(BaseModel):
    database: str = Field(..., description="The database name")
    schema: str = Field(..., description="The schema name")
    table: str = Field(..., description="The table name")

# Primary Key
class PrimaryKey(BaseModel):
    columns: List[str]

# # Dimension
# class CortexSearchService(BaseModel):
#     service: str
#     literal_column: Optional[str]
#     database: Optional[str]
#     schema: Optional[str]

class Dimension(BaseModel):
    name: str
    expr: str
    data_type: str = Field(..., description="The snowflake-compatible data type of the dimension")
    synonyms: Optional[List[str]]
    description: Optional[str]
    unique: Optional[bool] 
    sample_values: Optional[List[str]] 
    # cortex_search_service: Optional[CortexSearchService] 
    is_enum: Optional[bool] 

# Time Dimension
class TimeDimension(BaseModel):
    name: str
    expr: str
    data_type: str = Field(..., description="The snowflake-compatible data type of the time dimension")
    synonyms: Optional[List[str]] 
    description: Optional[str] 
    unique: Optional[bool] 
    sample_values: Optional[List[str]] 

# Fact
class Fact(BaseModel):
    name: str
    expr: str
    data_type: str = Field(..., description="The snowflake-compatible data type of the fact")
    synonyms: Optional[List[str]] 
    description: Optional[str] 
    sample_values: Optional[List[str]] 

# Filter
class Filter(BaseModel):
    name: str
    expr: str
    synonyms: Optional[List[str]] 
    description: Optional[str] 

# Metric
class Metric(BaseModel):
    name: str
    expr: str = Field(..., description="The expression to calculate the metric. Metrics must be defined with aggregates, otherwise use measures.")
    synonyms: Optional[List[str]] 
    description: Optional[str] 

# Logical Table
class LogicalTable(BaseModel):
    name: str
    base_table: BaseTable
    synonyms: Optional[List[str]] 
    description: Optional[str] 
    primary_key: Optional[PrimaryKey]
    dimensions: Optional[List[Dimension]] = Field(None, description="The dimensions of the logical table if they exist (e.g. product category, customer type, etc.)")
    time_dimensions: Optional[List[TimeDimension]] = Field(None, description="The time dimensions of the logical table if they exist (e.g. date, month, year, etc.)")
    facts: Optional[List[Fact]] = Field(None, description="The facts of the logical table if they exist (e.g. revenue, quantity, etc.)")
    metrics: Optional[List[Metric]] = Field(None, description="The metrics of the logical table if they exist (e.g. revenue, quantity, etc.)")
    filters: Optional[List[Filter]] = Field(None, description="The filters of the logical table if it makes sense to filter on the logical table")

# Relationship
# class Relationship(BaseModel):
#     name: str
#     left_table: str
#     right_table: str
#     relationship_columns: List[str]
#     join_type: str  # left_outer or inner
#     relationship_type: str  # many_to_one or one_to_one

# Semantic Model
class SemanticModel(BaseModel):
    name: str
    description: Optional[str]
    tables: Optional[List[LogicalTable]] 
    # relationships: Optional[List[Relationship]] 