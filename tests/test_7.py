import pytest
import pandas as pd
from definition_2aa404395f8949019bcdfd5f66ee2236 import generate_comparison_table

def test_generate_comparison_table_empty_dataframe():
    df = pd.DataFrame()
    try:
        generate_comparison_table(df)
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_generate_comparison_table_typical_data():
    data = {'Model': ['A', 'B'], 'Accuracy': [0.8, 0.9], 'Latency': [1.2, 0.8]}
    df = pd.DataFrame(data)
    try:
        generate_comparison_table(df)
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"

def test_generate_comparison_table_missing_columns():
    data = {'Model': ['A', 'B'], 'Accuracy': [0.8, 0.9]}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        generate_comparison_table(df)

def test_generate_comparison_table_non_numeric_data():
    data = {'Model': ['A', 'B'], 'Accuracy': ['high', 'low'], 'Latency': ['fast', 'slow']}
    df = pd.DataFrame(data)
    try:
        generate_comparison_table(df)
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"
        
def test_generate_comparison_table_inf_and_nan():
    data = {'Model': ['A', 'B'], 'Accuracy': [float('inf'), float('nan')], 'Latency': [1.2, 0.8]}
    df = pd.DataFrame(data)
    try:
        generate_comparison_table(df)
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"
