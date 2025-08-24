from game_logic import check_guess, toggle_mode, move_number, generate_number

def test_check_guess():
    assert check_guess(5, 10) == -1
    assert check_guess(15, 10) == 1
    assert check_guess(10, 10) == 0

def test_toggle_mode():
    assert toggle_mode(True) is False
    assert toggle_mode(False) is True

def test_generate_number_range():
    for _ in range(100):
        num = generate_number()
        assert 1 <= num <= 20

def test_move_number_stays_in_bounds():
    for _ in range(100):
        assert 1 <= move_number(1) <= 20
        assert 1 <= move_number(20) <= 20
        assert 1 <= move_number(10) <= 20
