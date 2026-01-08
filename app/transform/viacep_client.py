import os
import time
import requests
from typing import Dict, Optional

VIACEP_URL = "https://viacep.com.br/ws/"
USE_MOCK = os.getenv("USE_MOCK_VIACEP", "false").lower() == "true"


def fetch_cep(
    cep: str,
    timeout: int = 3,
    retries: int = 2,
    backoff: float = 0.5,
) -> Optional[Dict]:
    """
    Fetch address data from ViaCEP API with retry and backoff.
    """
    if USE_MOCK:
        return {
            "cep": cep,
            "logradouro": "Rua Exemplo",
            "bairro": "Centro",
            "localidade": "São Paulo",
            "uf": "SP",
            "estado": "São Paulo",
            "regiao": "Sudeste",
            "ibge": "3550308",
            "ddd": "11",
        }
    for attempt in range(retries + 1):
        try:
            response = requests.get(f"{VIACEP_URL}{cep}/json/",
                                    timeout=timeout)
            response.raise_for_status()
            data = response.json()
            if data.get("erro"):
                return None

            return data

        except requests.Timeout:
            if attempt == retries:
                return None
            time.sleep(backoff * attempt)

        except requests.RequestException as e:
            print(f"via_cep error: {e}")
            return None
