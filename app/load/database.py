import sqlite3
import json
from typing import List, Dict


def init_db(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS addresses (
            cep TEXT PRIMARY KEY,
            logradouro TEXT,
            bairro TEXT,
            localidade TEXT,
            uf TEXT,
            raw_payload TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def insert_addresses(db_path: str, addresses: List[Dict]) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for addr in addresses:
        cursor.execute(
            """
            INSERT OR REPLACE INTO addresses
            (
                cep,
                logradouro,
                bairro,
                localidade,
                uf,
                raw_payload
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                addr.get("cep"),
                addr.get("logradouro"),
                addr.get("bairro"),
                addr.get("localidade"),
                addr.get("uf"),
                json.dumps(addr, ensure_ascii=False),
            ),
        )

    conn.commit()
    conn.close()
