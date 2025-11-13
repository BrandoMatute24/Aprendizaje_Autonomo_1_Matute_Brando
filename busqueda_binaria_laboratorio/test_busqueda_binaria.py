# Por Brando Matute

import pytest
from busqueda_binaria import busqueda_binaria

@pytest.mark.parametrize(
    "lista, objetivo, esperado",
    [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([], 3, -1),
        ([10], 10, 0),
        ([10], 5, -1)
    ]
)
def test_busqueda_binaria(lista, objetivo, esperado):
    resultado = busqueda_binaria(lista, objetivo)
    assert resultado == esperado
