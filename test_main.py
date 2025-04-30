import pytest
from main import black_red

def test_black_red(capsys):
    black_red()
    captured = capsys.readouterr()
    output = captured.out.split('\n')[:-1]  # Remove last empty line
    
    # Check total lines (1-100)
    assert len(output) == 100
    
    # Check specific cases
    assert output[2] == "Black"      # 3
    assert output[4] == "Red"        # 5
    assert output[14] == "BlackRed"  # 15
    assert output[29] == "BlackRed"  # 30
    assert output[99] == "Red"       # 100 (since 100 % 5 == 0)
    assert output[0] == "1"          # 1
    assert output[6] == "7"          # 7 (not divisible by 3 or 5)