import pytest
import pandas as pd
from definition_87c32102827a4a70858d104ca15b31c2 import evaluate_all_methods

@pytest.fixture
def sample_document_data():
    # Create a simple DataFrame for testing
    data = {'EmployeeID': [1, 2, 3],
            'Name': ['Alice', 'Bob', 'Charlie'],
            'HRA_Contribution': [100, 200, 150]}
    return pd.DataFrame(data)

@pytest.fixture
def sample_predefined_queries():
    # Define some sample queries and expected results
    return {
        "What is Alice's HRA contribution?": "100",
        "What is Bob's HRA contribution?": "200",
        "What is Charlie's HRA contribution?": "150"
    }

def test_evaluate_all_methods_returns_dataframe(sample_document_data, sample_predefined_queries):
    result = evaluate_all_methods(sample_document_data, sample_predefined_queries)
    assert isinstance(result, pd.DataFrame)

def test_evaluate_all_methods_empty_data(sample_predefined_queries):
    empty_df = pd.DataFrame()
    result = evaluate_all_methods(empty_df, sample_predefined_queries)
    assert isinstance(result, pd.DataFrame) # Should still return a DataFrame, even if empty

def test_evaluate_all_methods_empty_queries(sample_document_data):
    empty_queries = {}
    result = evaluate_all_methods(sample_document_data, empty_queries)
    assert isinstance(result, pd.DataFrame)

def test_evaluate_all_methods_correct_columns(sample_document_data, sample_predefined_queries):
     result = evaluate_all_methods(sample_document_data, sample_predefined_queries)
     expected_columns = ["Query"]  # Assuming 'Query' column will be present
     assert "Query" in result.columns

def test_evaluate_all_methods_handles_no_relevant_information(sample_document_data):
    queries = {"What is the capital of France?": "Unknown"} # Query unrelated to document
    result = evaluate_all_methods(sample_document_data, queries)
    assert isinstance(result, pd.DataFrame)
