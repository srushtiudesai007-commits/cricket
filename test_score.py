from score import add_runs, strike_rate, required_runs


def test_add_runs_valid():
    assert add_runs(50, 4) == 54


def test_add_runs_zero():
    assert add_runs(50, 0) == 50


def test_strike_rate_valid():
    assert strike_rate(50, 25) == 200.0


def test_strike_rate_zero():
    assert strike_rate(50, 0) == 0.0


def test_required_runs_valid():
    assert required_runs(200, 150, 30) == 50


def test_required_runs_exceeded():
    assert required_runs(150, 160, 10) == 0