import pandas as pd
from typing import List, Tuple


def normalize_cep(cep: str) -> str:
    """
    Remove non-numeric characters from the postal code.
    Ex: '58348-000' -> '58348000'
    """
    return cep.replace("-", "").strip()


def is_valid_cep(cep: str) -> bool:
    """
    Checks if the postal code has exactly 8 numeric digits.
    """
    return cep.isdigit() and len(cep) == 8


def extract_ceps(csv_path: str) -> Tuple[List[str], List[str]]:
    """
    Reads a CSV file containing postal codes and separates valid and invalid postal codes.
    Returns:
    - list of valid postal codes
    - list of invalid postal codes
    """
    df = pd.read_csv(csv_path)
    valid_ceps = []
    invalid_ceps = []
    for raw_cep in df['cep']:
        cep = normalize_cep(str(raw_cep))
        if is_valid_cep(cep):
            valid_ceps.append(cep)
        else:
            invalid_ceps.append(raw_cep)

    return valid_ceps, invalid_ceps

