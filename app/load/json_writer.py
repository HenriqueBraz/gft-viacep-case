import json
from typing import List, Dict


def write_json(file_path: str, data: List[Dict]) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
