import numeros_pares
import importlib

def test_output(capsys):
    importlib.reload(numeros_pares)
    captured = capsys.readouterr()
    assert captured.out == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n"
