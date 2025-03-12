from snowflake.snowpark import Session
import json

def structured_output_llm_call(
        session: Session,
        prompt: str,
        response_format: dict,
        model: str = 'claude-3-5-sonnet',
        max_tokens: int = 1000
    ) -> str:
    """
    Call an LLM with structured output.
    """
    # AI model configuration options, including response format constraints.
    options = {
        'temperature': 0,  # Setting temperature to 0 ensures deterministic responses.
        'max_tokens': max_tokens,  # Limits response size.
        'response_format': response_format  # Properly format JSON schema
    }
    
    # SQL query to invoke the AI model via Snowflake Cortex.
    query = f"""
    SELECT snowflake.cortex.complete(
        '{model}',
        [
            {{
                'role': 'user',
                'content': $${prompt}$$
            }}
        ],
        {options}
    )
    """
    # Execute the SQL query and collect the response.
    res = session.sql(query).collect()
    # Parse the AI response and extract structured output.
    output = json.loads(res[0][0]).get('structured_output')[0].get('raw_message')
    return output