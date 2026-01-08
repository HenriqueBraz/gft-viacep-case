import pandas as pd
from pathlib import Path
from app.extract.extractor import (
    normalize_cep,
    is_valid_cep,
    extract_ceps,
)


def test_normalize_cep_removes_hyphen():
    assert normalize_cep("58348-000") == "58348000"


def test_is_valid_cep():
    assert is_valid_cep("58348000") is True
    assert is_valid_cep("123") is False
    assert is_valid_cep("abcdefgh") is False


def test_extract_ceps_separates_valid_and_invalid(tmp_path: Path):
    csv_path = tmp_path / "ceps.csv"

    df = pd.DataFrame(
        {
            "cep": [
                "58348-000",
                "000",
                "01001-000",
            ]
        }
    )
    df.to_csv(csv_path, index=False)

    valid, invalid = extract_ceps(str(csv_path))
    assert valid == ["58348000", "01001000"]
    assert invalid == ["000"]
