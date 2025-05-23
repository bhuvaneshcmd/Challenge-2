import pytest
from main import black_red

def test_black_red(capsys):
    black_red()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    
    assert output[2] == "Black"     # 3 → "Black"
    assert output[4] == "Red"       # 5 → "Red"
    assert output[14] == "BlackRed" # 15 → "BlackRed"
    assert output[0] == "1"         # 1 → "1"