import pytest
import pandas as pd
from definition_a3d37a98ba8b4ebfa23dac49634440ab import generate_performance_plot

@pytest.fixture
def mock_simulated_data():
    data = {
        'Model': ['ModelA', 'ModelB', 'ModelC', 'ModelA', 'ModelB'],
        'Prompt_Quality': ['Good', 'Good', 'Good', 'Bad', 'Bad'],
        'Simulated_Numerical_Accuracy': [0.9, 0.8, 0.7, 0.6, 0.5],
        'Simulated_Contextual_Accuracy': [0.85, 0.75, 0.65, 0.55, 0.45],
        'Simulated_Latency': [10, 15, 20, 25, 30]
    }
    return pd.DataFrame(data)

def test_generate_performance_plot_valid_data(mock_simulated_data, monkeypatch):
    # Test that the function runs without errors given valid data
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)  # Prevent plot from displaying during test
    try:
        generate_performance_plot(mock_simulated_data)
    except Exception as e:
        pytest.fail(f"generate_performance_plot raised an exception: {e}")

def test_generate_performance_plot_empty_data(monkeypatch):
    # Test that the function handles empty data gracefully
    empty_df = pd.DataFrame()
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    try:
        generate_performance_plot(empty_df)  # Should probably either return or handle gracefully. Can't assert much.
    except Exception as e:
        pytest.fail(f"generate_performance_plot raised an exception with empty data: {e}")

def test_generate_performance_plot_missing_columns(mock_simulated_data, monkeypatch):
    # Test that the function handles missing required columns
    data = mock_simulated_data.drop(columns=['Simulated_Numerical_Accuracy'])
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    with pytest.raises(KeyError):
        generate_performance_plot(data)

def test_generate_performance_plot_non_numeric_latency(mock_simulated_data, monkeypatch):
    #Test that a TypeError is returned if latency is non-numeric
    mock_simulated_data['Simulated_Latency'] = ['a', 'b', 'c', 'd', 'e']
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    with pytest.raises(TypeError):
            generate_performance_plot(mock_simulated_data)

def test_generate_performance_plot_inf_latency(mock_simulated_data, monkeypatch):
        #Test that inf latency gets handled gracefully
    mock_simulated_data['Simulated_Latency'] = [float('inf')] * len(mock_simulated_data)
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)
    try:
        generate_performance_plot(mock_simulated_data)
    except Exception as e:
        pytest.fail(f"generate_performance_plot raised an exception with inf latency: {e}")
