from calculator import add, factorial, sin, divide, circumference, multiply
import math as ma
import pytest

@pytest.mark.parametrize("x,y", [[(0, 0), 0], [(1, 2), 3], [(-2, 6), 4]])
def test_add1(x,y):
    assert add(x[0], x[1]) == y

@pytest.mark.parametrize("x,y", [[(0.0, 0.0), 0.0], [(0.1, 0.2), 0.3], [(-0.2, 0.6), 0.4]])
def test_add2(x,y):
    assert ma.isclose(add(x[0], x[1]),y)
    
@pytest.mark.parametrize(
        "x, y", [[add("Hello ","World"), "Hello World"], 
                 [add("Oslo, ","Norway"), "Oslo, Norway"], 
                 [add("Naturvitenskapelige ","programmering"), "Naturvitenskapelige programmering"]]
)
def test_add3(x,y):
    assert x == y

@pytest.mark.parametrize("x,y", [(factorial(7),ma.factorial(7)), (factorial(22),ma.factorial(22)), (factorial(8),ma.factorial(8))])
def test_factorial(x,y):
    assert x == y
    
@pytest.mark.parametrize("x,y", [(ma.sin(7), sin(7,100)), (ma.sin(12), sin(12,100)), (ma.sin(18), sin(18,100))])
def test_sin(x,y):
   assert ma.isclose(x,y)

@pytest.mark.parametrize("x,y", [(43/5, divide(43,5)), (67/3, divide(67,3)), (1465/22, divide(1465,22))])
def test_divide(x,y):
    assert ma.isclose(x,y)
   
@pytest.mark.parametrize("x,y", [(2*ma.pi*7, circumference(7)), (2*ma.pi*12, circumference(12)), (2*ma.pi*25, circumference(25))])
def test_circumference(x,y):
    assert ma.isclose(x,y)
    
@pytest.mark.parametrize("x,y", [(43*5, multiply(43,5)), (67*3, multiply(67,3)), (1465*22, multiply(1465,22))])
def test_multiply(x,y):
    assert ma.isclose(x,y)
    
@pytest.mark.parametrize("x,y", [("Hello", 5), (2, "Yellow"), ("Jello", 9)])
def test_add_raises_TypeError(x,y):
    with pytest.raises(TypeError):
        add(x,y)

@pytest.mark.parametrize("x,y", [(42,0), (23, 0), (7, 0)])
def test_divide_raises_ZeroDivisionError(x,y):
    with pytest.raises(ZeroDivisionError):
        divide(x,y)  
