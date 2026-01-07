import requests
from typing import Dict, Optional

VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"


def fetch_cep(cep: str, timeout: int = 5) -> Optional[Dict]:
    """
    Fetch address data from ViaCEP API.
    Returns a dict with address data or None if CEP
    is invalid or request fails.
    """
    try:
        response = requests.get(VIACEP_URL.format(cep=cep), timeout=timeout)
        response.raise_for_status()
        data = response.json()
        if data.get("erro"):
            return None
        return data

    except requests.RequestException:
        return None
