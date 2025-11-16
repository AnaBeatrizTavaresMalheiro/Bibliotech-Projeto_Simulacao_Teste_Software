import pytest
from aplicacao.db.database import resetar_banco


# -------------------------------------------------------------------
# FIXTURE DE ROLLBACK
# -------------------------------------------------------------------
@pytest.fixture(autouse=True, scope="function")
def limpar_banco_antes_de_cada_teste():
    resetar_banco()


# -------------------------------------------------------------------
# TESTES
# -------------------------------------------------------------------

def test_reset_endpoint_exists(client):
    """
    Verifica se o endpoint público de reset está disponível.
    Deve retornar 200 ou 204.
    """
    r = client.post("/admin/resetar-banco")
    assert r.status_code in (200, 204)
