import pytest

from calculadora import suma,resta,multiplicacion,division

def test_suma ():
    resultado = suma (5,3)

    assert resultado == 8
    
def test_resta ():
    resultado = resta(10,4)

    assert resultado == 6