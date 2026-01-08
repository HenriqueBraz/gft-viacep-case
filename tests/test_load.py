from app.load.json_writer import write_json
from app.load.xml_writer import  write_xml
from app.load.error_writer import  write_errors

def test_write_json(tmp_path):
    file_path = tmp_path / "data.json"
    data = [{"cep": "01001000"}]
    write_json(str(file_path), data)
    assert file_path.exists()


def test_write_xml(tmp_path):
    file_path = tmp_path / "data.xml"
    data = [{"cep": "01001000"}]
    write_xml(str(file_path), data)
    assert file_path.exists()

def write_errors(tmp_path):
    file_path = tmp_path / "data.csv"
    data = [{"cep": "01001000"}]
    write_errors(str(file_path), data)
    assert file_path.exists()
