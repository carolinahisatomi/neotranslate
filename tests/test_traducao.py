import pytest
from backend.traducao import extrair_modelo

@pytest.mark.parametrize('texto,esperado', [
    ("Model No.: INV5000", "INV5000"),
    ("Model Number: XYZ-987", "XYZ-987"),
    ("Modelo: ABC_123", "ABC_123"),
    ("Sem modelo", "modelo"),
])
def test_extrair_modelo(texto, esperado):
    assert extrair_modelo(texto) == esperado