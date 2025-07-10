import pytest
import pandas as pd
from definition_1fbdbed3a6344d4fb3a918cdde73c23c import simulate_query_response

@pytest.fixture
def sample_document_data():
    return pd.DataFrame({
        'Month': ['May', 'June'],
        'Coverage': ['You Only', 'Family'],
        'HRA Contribution': [100, 200]
    })

@pytest.mark.parametrize("method, expected_answer, expected_accuracy", [
    ("Traditional Textract (Simulated Low Accuracy)", "Sorry, I could not find relevant information...", 0.0),
    ("AWS Textract Visual Q&A (Simulated Moderate Accuracy)", "Simulated answer for moderate accuracy", 0.4),
    ("TalentMine (LLM-enhanced) (Simulated High Accuracy)", "Simulated answer for high accuracy", 1.0),
])
def test_simulate_query_response_different_methods(sample_document_data, method, expected_answer, expected_accuracy):
    answer, accuracy = simulate_query_response(sample_document_data, "What is the HRA contribution?", method)
    assert answer == expected_answer
    assert accuracy == expected_accuracy

def test_simulate_query_response_invalid_method(sample_document_data):
    answer, accuracy = simulate_query_response(sample_document_data, "What is the HRA contribution?", "Invalid Method")
    assert answer == "Sorry, I could not find relevant information..."
    assert accuracy == 0.0

def test_simulate_query_response_empty_document(sample_document_data):
    empty_df = pd.DataFrame()
    answer, accuracy = simulate_query_response(empty_df, "What is the HRA contribution?", "TalentMine (LLM-enhanced) (Simulated High Accuracy)")
    assert answer == "Sorry, I could not find relevant information..."
    assert accuracy == 0.0

def test_simulate_query_response_no_query(sample_document_data):
    answer, accuracy = simulate_query_response(sample_document_data, "", "TalentMine (LLM-enhanced) (Simulated High Accuracy)")
    assert answer == "Simulated answer for high accuracy"
    assert accuracy == 1.0
