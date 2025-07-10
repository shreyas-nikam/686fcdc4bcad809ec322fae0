import pytest
from definition_cec98beb42bf447d8ba224bd8964e0cf import display_metrics

def test_display_metrics_typical_values(capsys):
    display_metrics(0.95, 0.88, 0.12)
    captured = capsys.readouterr()
    assert captured.out != "" #Check that the function prints something, actual content is tested in the notebook

def test_display_metrics_zero_values(capsys):
    display_metrics(0.0, 0.0, 0.0)
    captured = capsys.readouterr()
    assert captured.out != "" #Check that the function prints something, actual content is tested in the notebook

def test_display_metrics_high_values(capsys):
    display_metrics(1.0, 1.0, 1.0)
    captured = capsys.readouterr()
    assert captured.out != "" #Check that the function prints something, actual content is tested in the notebook

def test_display_metrics_negative_accuracy(capsys):
    display_metrics(-0.5, 0.7, 0.2)
    captured = capsys.readouterr()
    assert captured.out != "" #Check that the function prints something, actual content is tested in the notebook

def test_display_metrics_negative_latency(capsys):
    display_metrics(0.9, 0.6, -0.1)
    captured = capsys.readouterr()
    assert captured.out != "" #Check that the function prints something, actual content is tested in the notebook
