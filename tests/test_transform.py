from unittest.mock import patch

from app.transform.transformer import transform_ceps


@patch("app.transform.transformer.fetch_cep")
def test_transform_ceps_success(mock_fetch):
    mock_fetch.side_effect = [
        {"cep": "01001000", "logradouro": "Rua Teste"},
        None,
    ]
    ceps = ["01001000", "00000000"]
    addresses, errors = transform_ceps(ceps, max_workers=2)
    assert len(addresses) == 1
    assert addresses[0]["cep"] == "01001000"
    assert errors == ["00000000"]


@patch("app.transform.transformer.fetch_cep")
def test_transform_ceps_exception(mock_fetch):
    mock_fetch.side_effect = Exception("API error")
    ceps = ["01001000"]
    addresses, errors = transform_ceps(ceps, max_workers=1)
    assert addresses == []
    assert errors == ["01001000"]
