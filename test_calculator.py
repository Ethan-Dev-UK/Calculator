from calculator import add, subtract, multiply, divide, powers, circleArea, circleCircumference, triangleArea

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 3) == 7

def test_divide():
    assert divide(6, 2) == 3

def test_multiply():
    assert multiply(3, 2) == 6

def test_powers():
    assert powers(2, 2) == 4

def test_uneven_division():
    a, b = 5, 2
    result = divide(a, b)
    assert result == 2.5

def test_circleArea():
    assert circleArea(-4) == "NaN"

def test_circleCircumference():
    assert circleCircumference(0) == 0

def test_triangleArea():
    assert triangleArea(5, 4) == 10
