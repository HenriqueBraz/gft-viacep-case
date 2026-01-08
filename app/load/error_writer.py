import csv
from typing import List


def write_errors(file_path: str, errors: List[str]) -> None:
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cep"])
        for cep in errors:
            writer.writerow([cep])
