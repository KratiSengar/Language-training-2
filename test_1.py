import pytest
def test_uppercase():
    assert "wassup".upper() == "WASSUP"

def test_reversed():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]

def test_for_greater():
    first = 10
    second = 100
    assert second,first

def test_for_greatervalue():
    first = 1923
    second = 100
    assert second,first

def test_for_in():
    l = 'cube' 
    k = 'cubexo'
    assert l,k

@pytest.mark.skip
def test_for_subset():
    assert {1,2,3},{1,2,3,4,5,6,7,8,9}


@pytest.mark.three
def test_split():
    assert 'hell' 'o' 'hello'

def funct(x):
    return x+5
@pytest.mark.four
def test_for_funct():
    assert funct(10)==15

@pytest.mark.xfail
def test_func():
    x = 6
    y = 1
    assert x == y

@pytest.mark.one
def test_fun():
    t = 15
    u = 20
    assert t + 5 == u

@pytest.fixture
def dict():
    data = {"key": "value"}
    return data
# Test using the fixture
def test_fixture_example(dict):
    assert "key" in dict
    assert dict["key"] == "value"

@pytest.fixture
def num():
    j = 10
    k = 23
    l = 12
    return [j,k,l]

def test_method1(num):
    p = 16
    assert num[0] == p
def test_method2(num):
    q = 23
    assert num[1] == q
def test_method3(num):
    r = 12
    assert num[2] == r

@pytest.mark.parametrize("o,s,d", [(10,20,200), (10,30,200)])
def test_param(o,s,d):
    assert o*s == d

def add(x, y):
    return x + y
test_data = [
    (1, 2, 3),  # Test case 1
    (0, 0, 0),  # Test case 2
    (-1, 1, 0),  # Test case 3
    (10, -5, 5),  # Test case 4
]
@pytest.mark.parametrize("input_a, input_b, expected", test_data)
def test_addition(input_a, input_b, expected):
    result = add(input_a, input_b)
    assert result == expected