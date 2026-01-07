from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict
from app.transform.viacep_client import fetch_cep


def transform_ceps(ceps: List[str], max_workers=10) -> Tuple[List[Dict], List[str]]:
    """
    Enrich CEPs using ViaCEP API.
    Returns:
    - list of address dicts
    - list of CEPs that failed
    """
    addresses = []
    failed_ceps = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {}
        for cep in ceps:
            future = executor.submit(fetch_cep, cep)
            future_map[future] = cep

        for future in as_completed(future_map):
            cep = future_map[future]
            try:
                result = future.result()
                if result:
                    addresses.append(result)
                else:
                    failed_ceps.append(cep)
            except Exception:
                failed_ceps.append(cep)

    return addresses, failed_ceps
