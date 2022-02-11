import peso_lunar
import importlib

def test_output(capsys):
    importlib.reload(peso_lunar)
    captured = capsys.readouterr()
    assert captured.out == "12.375\n24.75\n37.125\n49.5\n61.875\n74.25\n86.625\n99.0\n111.375\n123.75\n136.125\n148.5\n160.875\n173.25\n185.625\n"
