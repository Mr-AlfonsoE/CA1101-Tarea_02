import variables;

def test_monedas_encontradas():
    assert 'monedas_encontradas' in dir(variables)
def test_monedas_robadas():
    assert 'monedas_robadas' in dir(variables)
def test_monedas_magicas():
    assert 'monedas_magicas' in dir(variables)
def test_resultado():
    assert 3514 == variables.resultado
