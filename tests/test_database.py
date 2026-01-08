from app.load.database import init_db, insert_addresses
import sqlite3


def test_insert_addresses(tmp_path):
    db_path = tmp_path / "test.db"
    init_db(str(db_path))
    data = [
        {
            "cep": "01001000",
            "logradouro": "Rua Teste",
            "bairro": "Centro",
            "localidade": "São Paulo",
            "uf": "SP",
        }
    ]
    insert_addresses(str(db_path), data)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT cep FROM addresses")
    rows = cursor.fetchall()
    conn.close()
    assert rows == [("01001000",)]